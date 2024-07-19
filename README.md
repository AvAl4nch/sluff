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

### Method 2: Using Docker

1. **Pull the Docker Image:**
   ```bash
   docker pull aval4nch/sluff
   ```

2. **Run the Docker Container:**
   ```bash
   docker run -d --name sluff -e DISCORD_BOT_TOKEN=<your_bot_token> aval4nch/sluff
   ```

### Method 3: Using Docker Compose

1. **Create a `.env` File with Your Discord Bot Token:**
   ```bash
   echo "DISCORD_BOT_TOKEN=<your_bot_token>" > .env
   ```

2. **Run the Docker Container:**
   ```bash
   docker-compose up -d
   ```

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

If you need any help, feel free to send me a direct message!

---

Feel free to adjust any details as needed!
