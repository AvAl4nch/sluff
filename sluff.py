import discord
from discord.ext import commands
import yt_dlp as youtube_dl
import os
import asyncio
from asyncio import Queue, QueueEmpty
import re

intents = discord.Intents.default()
intents.message_content = True  

bot = commands.Bot(command_prefix='!!', intents=intents)

# Create a queue to hold the songs
song_queue = Queue()
queue_titles = []  

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

async def play_next(ctx):
    try:
        
        next_song = await song_queue.get()
    except QueueEmpty:
        return

    voice_client = discord.utils.get(bot.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'noplaylist': True,
        'quiet': True,
        'extractaudio': True,
        'nocheckcertificate': True,
        'skip_download': True
    }

    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(next_song, download=False)
            if 'entries' in info:
                info = info['entries'][0]
            url = info.get('url')
            title = info.get('title', 'Unknown Title')

        if not url:
            await ctx.send(f"Failed to extract URL for {next_song}. Skipping...")
            await play_next(ctx)
            return

        def after_playing(error):
            fut = asyncio.run_coroutine_threadsafe(play_next(ctx), bot.loop)
            try:
                fut.result()
            except Exception as e:
                print(f'Error in after_playing: {e}')

        if voice_client.is_playing():
            voice_client.stop()

        voice_client.play(discord.FFmpegPCMAudio(url), after=after_playing)
        await ctx.send(f'Now playing: {title}')


        queue_titles.pop(0)

    except Exception as e:
        await ctx.send(f"An error occurred while trying to play the next song: {e}")

@bot.command(name='p')
async def play(ctx, *, search: str):
    """Plays a song or adds it to the queue. Accepts YouTube URLs or search terms."""
    if not ctx.author.voice:
        await ctx.send("You need to be in a voice channel to play music!")
        return

    voice_channel = ctx.author.voice.channel
    voice_client = discord.utils.get(bot.voice_clients, guild=ctx.guild)

    if voice_client is None:
        voice_client = await voice_channel.connect()
    elif voice_client.channel != voice_channel:
        await voice_client.move_to(voice_channel)

    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'noplaylist': True,
            'quiet': True,
            'extractaudio': True,
            'nocheckcertificate': True,
            'skip_download': True
        }

        # Check if the input is a YouTube URL
        url_regex = re.compile(
            r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/'
            r'(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})')
        if url_regex.match(search):
            url = search
        else:
            url = f"ytsearch:{search}"

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            if 'entries' in info:
                info = info['entries'][0]
            title = info.get('title', 'Unknown Title')

        await song_queue.put(url)
        queue_titles.append(title)

        if not voice_client.is_playing():
            await play_next(ctx)
        else:
            await ctx.send(f'Added to queue: {title}')

    except Exception as e:
        await ctx.send(f"An error occurred while trying to search for the song: {e}")

@bot.command(name='stop')
async def stop(ctx):
    """Stops playing and disconnects the bot from the voice channel."""
    voice_client = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice_client and voice_client.is_connected():
        await voice_client.disconnect()
        await ctx.send("Stopped playing and disconnected from the voice channel.")
    else:
        await ctx.send("I'm not in a voice channel.")

@bot.command(name='pause')
async def pause(ctx):
    """Pauses the currently playing song."""
    voice_client = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice_client and voice_client.is_playing():
        voice_client.pause()
        await ctx.send("Paused the playback.")
    else:
        await ctx.send("I'm not playing any audio.")

@bot.command(name='resume')
async def resume(ctx):
    """Resumes the currently paused song."""
    voice_client = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice_client and voice_client.is_paused():
        voice_client.resume()
        await ctx.send("Resumed the playback.")
    else:
        await ctx.send("The playback is not paused.")

@bot.command(name='skip')
async def skip(ctx):
    """Skips the currently playing song."""
    voice_client = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice_client and voice_client.is_playing():
        voice_client.stop()
        await play_next(ctx)
        await ctx.send("Skipped the current song.")
    else:
        await ctx.send("I'm not playing any audio.")

@bot.command(name='queue')
async def queue(ctx):
    """Displays the current song queue."""
    if song_queue.empty():
        await ctx.send("The queue is empty.")
    else:
        queue_list = "\n".join([f"{i + 1}. {title}" for i, title in enumerate(queue_titles)])
        embed = discord.Embed(title="Song Queue", description=queue_list, color=discord.Color.blue())
        await ctx.send(embed=embed)

@bot.command(name='commands')
async def help_command(ctx):
    """Displays this help message."""
    help_text = """
    **Bot Commands:**
    `!!p <song name or YouTube URL>` - Plays a song or adds it to the queue.
    `!!stop` - Stops playing and disconnects the bot from the voice channel.
    `!!pause` - Pauses the currently playing song.
    `!!resume` - Resumes the currently paused song.
    `!!skip` - Skips the currently playing song.
    `!!queue` - Displays the current song queue.
    `!!commands` - Displays this help message.
    """
    embed = discord.Embed(title="Help", description=help_text, color=discord.Color.green())
    await ctx.send(embed=embed)

# Get the bot token from the environment variable
TOKEN = os.getenv('DISCORD_BOT_TOKEN')
if not TOKEN:
    raise ValueError("No token found. Please set the DISCORD_BOT_TOKEN environment variable.")

bot.run(TOKEN)