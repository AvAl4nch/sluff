# Sluff
<div style="text-align: center;">
  <img src="./logo.png" alt="logo" width="400"/>
</div>


# info
- This is a simple python bot that you need to self-host.
- this bot can run any video from Youtube in a vc.

# setup
Method 1 
1.  install the packages.
```
pip install discord yt-dlp
```
2. set the `DISCORD_BOT_TOKEN` environment variable.
lunux:
```
export DISCORD_BOT_TOKEN="YOUR_BOT_TOKEN"
```
3. run sluff
```
python sluff.py
```

Method 2  Docker
1. Pull the docker image.
```
docker pull aval4nch/sluff
```
   
2. run the docker image.
```
docker run -d --name sluff -e DISCORD_BOT_TOKEN=<your_bot_token> aval4nch/sluff
```

Method 3 Docker compose

1. Create a `.env` file with your discord bot toket.
```
echo "DISCORD_BOT_TOKEN=<your_bot_token>" > .env
```
2. Run the container.
```
docker-compose up -d
```



# notes
- You need to setup your dicord bot in the [Discord Developer Portal](https://discord.com/developers/applications)
- In `OAuth2 URL Generator` pick `bot` and `applications.commands`.
- give the bot the following privs:
    - connect
    - speak
    - Send Messages
- You can also just give the bot administrator (not recommended)
   
> dm me if you need any help :)


