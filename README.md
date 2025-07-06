# Discord Music Bot

This is a self-contained Discord music bot that can play music from YouTube, search for songs, manage a queue, and more. It is built with Python using the `discord.py` library. The included `launch.sh` script handles the setup of the environment and all dependencies automatically.

## Features

- Play music from YouTube URLs and search queries
- Playlist support
- Song queue management (add, remove, clear, shuffle)
- Playback controls (pause, resume, skip, stop)
- Volume control
- Looping
- Playback speed control
- Administrative commands (shutdown, restart)

## Commands

### Music Commands

- `?join`: Makes the bot join your current voice channel.
- `?leave`: Disconnects the bot from the voice channel.
- `?search <query>`: Searches YouTube for a song.
- `?play <URL or search query>`: Plays a song from a URL or search query.
- `?playlist <URL>`: Adds a playlist to the queue.
- `?volume <0-200>`: Sets the music volume.
- `?nowplaying`: Shows the currently playing song.
- `?queue`: Shows the current song queue.
- `?skip`: Skips the current song.
- `?stop`: Stops the music and clears the queue.
- `?pause`: Pauses the music.
- `?resume`: Resumes the music.
- `?clear`: Clears the song queue.
- `?remove <song number>`: Removes a song from the queue by its number.
- `?loop`: Toggles looping for the current song.
- `?speedhigher`: Increases the playback speed.
- `?speedlower`: Decreases the playback speed.
- `?shuffle`: Shuffles the song queue.

### Admin Commands (Owner Only)

- `?fetch_and_set_cookies <URL>`: Fetches cookies from a URL and saves them for yt-dlp.
- `?shutdown`: Shuts down the bot.
- `?restart`: Restarts the bot.

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  **Configuration:**

    Create a `.env` file in the project root and add the following variables:

    ```
    DISCORD_TOKEN="your_discord_bot_token"
    YOUTUBE_API_KEY="your_youtube_api_key"
    BOT_OWNER_ID="your_discord_user_id"
    LOG_CHANNEL_ID="your_discord_log_channel_id"
    ```

    Alternatively, you can hardcode these values in `config.py`.

3.  **Run the setup script:**

    This will create a virtual environment, install dependencies, and set up the necessary files.

    ```bash
    ./launch.sh setup
    ```

## Usage

-   **Start the bot:**
    ```bash
    ./launch.sh start
    ```

-   **Stop the bot:**
    ```bash
    ./launch.sh stop
    ```

-   **Restart the bot:**
    ```bash
    ./launch.sh restart
    ```

-   **Attach to the bot's console:**
    ```bash
    ./launch.sh attach
    ```

## Dependencies

-   `discord.py`
-   `google-api-python-client`
-   `yt-dlp`
-   `aiohttp`
-   `ffmpeg`
-   `libopus-dev`
