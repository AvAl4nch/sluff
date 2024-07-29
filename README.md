# Sluff

<div style="text-align: center;">
  <img src="./logo.png" alt="logo" width="400"/>
</div>

## Overview

Sluff is a Python-based Discord bot that allows you to play YouTube videos in a voice channel. This bot needs to be self-hosted.

## Features

- Play any YouTube video directly in a Discord voice channel.

## Setup

### Method 1: Manual Installation

1. **Install Required Packages:**
   ```bash
   pip install discord yt-dlp
   ```

2. **Set the `DISCORD_BOT_TOKEN` Environment Variable:**

   On Linux:
   ```bash
   export DISCORD_BOT_TOKEN="YOUR_BOT_TOKEN"
   ```

3. **Run Sluff:**
   ```bash
   python sluff.py
   ```
> you can run it with docker

## Configuration

- **Set Up Your Discord Bot:**
  - Go to the [Discord Developer Portal](https://discord.com/developers/applications).
  - In the **OAuth2 URL Generator**, select `bot` and `applications.commands`.
  - Grant the bot the following permissions:
    - Connect
    - Speak
    - Send Messages

  - Alternatively, you can give the bot administrator permissions (not recommended for security reasons).

## Support

If you need any help, feel free to dm me!
