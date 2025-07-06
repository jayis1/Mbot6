# 🎶 Discord Music Bot

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python" alt="Python Version">
  <img src="https://img.shields.io/badge/discord.py-2.3.2-blue?style=for-the-badge&logo=discord" alt="discord.py Version">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License">
</p>

A self-contained Discord music bot built with Python and `discord.py`. It's designed for easy setup and robust performance, running as a background service using `screen`. The included `launch.sh` script handles the complete setup, including dependency installation and environment configuration.

---

## ✨ Features

- ✅ **Self-Contained Installation**: The `launch.sh` script automatically sets up a virtual environment and installs all dependencies.
- ✅ **Background Operation**: Runs in a `screen` session, ensuring the bot stays online.
- ✅ **YouTube Integration**: Play audio from YouTube URLs, playlists, and search queries.
- ✅ **Full Playback Control**: `play`, `pause`, `resume`, `skip`, `stop`.
- ✅ **Queue Management**: `add`, `remove`, `clear`, `shuffle`, and `view queue`.
- ✅ **Audio Controls**: Adjust `volume` and playback `speed`.
- ✅ **Looping**: Toggle looping for the currently playing song.
- ✅ **Admin Commands**: `shutdown` and `restart` the bot remotely.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- `git`
- `ffmpeg` and `libopus-dev` (The setup script will attempt to install these on Debian-based systems).

### ⚙️ Installation & Setup

The bot is designed for a quick and easy setup.

1.  **Clone the Repository**
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  **Configure the Bot**
    Create a `.env` file in the project root. You can use the example file as a template.
    ```bash
    cp .env.example .env
    ```
    Now, edit the `.env` file with your credentials:
    ```dotenv
    DISCORD_TOKEN="your_discord_bot_token"
    YOUTUBE_API_KEY="your_youtube_api_key"
    BOT_OWNER_ID="your_discord_user_id"
    LOG_CHANNEL_ID="your_discord_log_channel_id"
    ```

3.  **Run the Setup Script**
    This command prepares the environment, installs all Python packages, and makes the scripts executable.
    ```bash
    ./launch.sh setup
    ```

---

## 🤖 Usage

The `launch.sh` script is your control center for the bot.

| Command               | Description                                                              |
| --------------------- | ------------------------------------------------------------------------ |
| `./launch.sh start`   | Starts the bot in a new `screen` session.                                |
| `./launch.sh stop`    | Stops the bot and closes the `screen` session.                           |
| `./launch.sh restart` | Restarts the bot.                                                        |
| `./launch.sh attach`  | Attaches to the bot's console to view live logs. (Press `Ctrl+A` then `D` to detach). |

---

## 🎵 Commands

The default command prefix is `?`.

### Music Commands

| Command                          | Description                                      |
| -------------------------------- | ------------------------------------------------ |
| `?join`                          | Joins your current voice channel.                |
| `?leave`                         | Disconnects from the voice channel.              |
| `?search <query>`                | Searches YouTube for a song.                     |
| `?play <URL or search query>`    | Plays a song or adds it to the queue.            |
| `?playlist <URL>`                | Adds a YouTube playlist to the queue.            |
| `?queue`                         | Displays the current song queue.                 |
| `?skip`                          | Skips the current song.                          |
| `?stop`                          | Stops playback and clears the queue.             |
| `?pause`                         | Pauses the music.                                |
| `?resume`                        | Resumes the music.                               |
| `?clear`                         | Clears the song queue.                           |
| `?remove <song number>`          | Removes a specific song from the queue.          |
| `?nowplaying`                    | Shows the currently playing song.                |
| `?volume <0-200>`                | Sets the music volume.                           |
| `?loop`                          | Toggles looping for the current song.            |
| `?speedhigher` / `?speedlower`   | Increases or decreases the playback speed.       |
| `?shuffle`                       | Shuffles the song queue.                         |

### Admin Commands (Bot Owner Only)

| Command                             | Description                                      |
| ----------------------------------- | ------------------------------------------------ |
| `?fetch_and_set_cookies <URL>`      | Fetches and sets cookies for `yt-dlp`.           |
| `?shutdown`                         | Shuts down the bot.                              |
| `?restart`                          | Restarts the bot.                                |

---

## 🛠️ Dependencies

-   `discord.py`
-   `google-api-python-client`
-   `yt-dlp`
-   `aiohttp`
-   `python-dotenv`
