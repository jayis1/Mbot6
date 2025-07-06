# config.py

# It is recommended to use environment variables for sensitive data.
# However, you can hardcode the values here for simplicity.
import os

DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN", "Discord_bot_token_here")  # Replace with your Discord Bot Token
YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY", "Youtube_api_key_here")
BOT_OWNER_ID = int(os.environ.get("BOT_OWNER_ID", "Bot_owner_id_here")) # Replace with your Discord User ID

# You can change the bot's command prefix here
COMMAND_PREFIX = "?"

# Emojis for UI
PLAY_EMOJI = '▶️'
PAUSE_EMOJI = '⏸️'
SKIP_EMOJI = '⏭️'
QUEUE_EMOJI = '🎵'
ERROR_EMOJI = '❌'
SUCCESS_EMOJI = '✅'

# Discord Channel ID for sending bot logs (errors, warnings)
LOG_CHANNEL_ID = int(os.environ.get("LOG_CHANNEL_ID", "Log_channel_id_here")) # Replace with your desired log channel ID
