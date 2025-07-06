# 🎶 Discord Music Bot

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python" alt="Python Version">
  <img src="https://img.shields.io/badge/discord.py-2.3.2-blue?style=for-the-badge&logo=discord" alt="discord.py Version">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License"></a>
</p>

A self-contained Discord music bot built with Python and `discord.py`. It's designed for easy setup and robust performance, running as a background service using `screen`. The included `launch.sh` script handles the complete setup, including dependency installation, environment configuration, and automatic generation of necessary files like `__init__.py`.

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

1.  **Clone the Repository**
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  **Configure the Bot**
    Create a `.env` file by copying the example file.
    ```bash
    cp .env.example .env
    ```
    Now, edit the `.env` file with your credentials. See the **Configuration Details** section below for more information.

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

## 🔧 Configuration Details

-   **`DISCORD_TOKEN`**: Your Discord bot's authentication token. You can get this from the [Discord Developer Portal](https://discord.com/developers/applications) by creating an application and adding a bot.
-   **`YOUTUBE_API_KEY`**: Your YouTube Data API v3 key. This is required for the `?search` command. You can obtain one from the [Google Cloud Console](https://console.cloud.google.com/apis/library/youtube.googleapis.com).
-   **`BOT_OWNER_ID`**: Your personal Discord User ID. This is used for owner-only commands. To get your ID, enable Developer Mode in Discord's settings, then right-click your username and select "Copy User ID".
-   **`LOG_CHANNEL_ID`**: The ID of the Discord channel where the bot will send logs. Get this by enabling Developer Mode, right-clicking the channel, and selecting "Copy Channel ID".

---

## 📁 Project Structure

```
.
├── cogs/               # Contains the command modules (cogs) for the bot
│   ├── admin.py
│   ├── music.py
│   └── ...
├── utils/              # Utility scripts and helper functions
│   └── ...
├── .env.example        # Example environment file
├── bot.py              # Main bot script
├── config.py           # Bot configuration loader
├── launch.sh           # Main script for managing the bot
├── requirements.txt    # Python dependencies
└── README.md           # This file
```

---

## ⁉️ Troubleshooting

-   **Bot is offline or not responding:**
    -   Ensure the bot is running with `./launch.sh attach`. If the session is not active, start it with `./launch.sh start`.
    -   Check the `bot.log` file for any errors.
    -   Verify that your `DISCORD_TOKEN` is correct.

-   **No audio is playing:**
    -   Make sure `ffmpeg` is installed correctly. The setup script attempts to install it, but it might fail.
    -   Check the bot's logs for any `ffmpeg` or `opus` related errors.

-   **`?search` command is not working:**
    -   Ensure your `YOUTUBE_API_KEY` is correct and that the YouTube Data API v3 is enabled in your Google Cloud project.

---

## 🤝 Contributing

Contributions are welcome! If you have a feature request, bug report, or want to improve the code, please feel free to open an issue or submit a pull request.

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/YourFeature`).
3.  Commit your changes (`git commit -m 'Add some feature'`).
4.  Push to the branch (`git push origin feature/YourFeature`).
5.  Open a Pull Request.

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
