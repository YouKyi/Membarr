# Membarr

[![Docker](https://img.shields.io/badge/Docker-GHCR-%23099cec?style=for-the-badge&logo=docker)](https://ghcr.io/youkyi/membarr)
[![GitHub Actions](https://img.shields.io/github/actions/workflow/status/YouKyi/Membarr/docker-build.yml?style=for-the-badge&logo=github)](https://github.com/YouKyi/Membarr/actions)

Membarr is a Discord bot that invites users to Plex and Jellyfin. You can automate this bot to invite discord users to a media server once a certain role is given to a user, or add users manually.

> **Fork maintained by [YouKyi](https://github.com/YouKyi)** - Originally forked from [Invitarr](https://github.com/Sleepingpirates/Invitarr) by Sleepingpirates, then [Membarr](https://github.com/Yoruio/Membarr) by Yoruio.

## Features

- 🎬 Invite users to **Plex** and **Jellyfin** from Discord
- 🤖 Fully automatic invites using Discord roles
- 🚪 Auto-remove users from Plex/Jellyfin when they leave the server or lose their role
- 📊 View and edit the database directly from Discord
- 🌐 **Bilingual messages** - All user messages are sent in English 🇬🇧 and French 🇫🇷
- 🎥 **Seer Request URL** - Optionally send users a link to your Overseerr/Jellyseerr instance

## Commands

```
/plex invite <email>          - Add an email to Plex
/plex remove <email>          - Remove an email from Plex
/jellyfin invite <username>   - Add a user to Jellyfin
/jellyfin remove <username>   - Remove a user from Jellyfin
/membarr dbls                 - List Membarr's database
/membarr dbadd <@user> <email> <jellyfin_username>  - Add existing users to DB
/membarr dbrm <position>      - Remove a record from the DB
```

## Quick Start with Docker

### Docker Compose (Recommended)

```yaml
services:
  membarr:
    image: ghcr.io/youkyi/membarr:latest
    container_name: membarr
    volumes:
      - membarr_config:/app/app/config
    environment:
      - token=YOUR_DISCORD_BOT_TOKEN
      - seer_request_url=https://your-overseerr-url.com  # Optional
      - discord_language=both  # Options: both, en, fr
    restart: unless-stopped

volumes:
  membarr_config:
```

### Docker Run

```bash
docker run -d \
  --name membarr \
  --restart unless-stopped \
  -v /path/to/config:/app/app/config \
  -e "token=YOUR_DISCORD_BOT_TOKEN" \
  -e "seer_request_url=https://your-overseerr-url.com" \
  -e "discord_language=both" \
  ghcr.io/youkyi/membarr:latest
```

## Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `token` | ✅ Yes | Discord bot token |
| `seer_request_url` | ❌ No | URL to your Overseerr/Jellyseerr for movie requests |
| `discord_language` | ❌ No | Language mode: `both` (EN+FR), `en` (English only), `fr` (French only). Default: `both` |

## Creating a Discord Bot

1. Go to [Discord Developer Portal](https://discord.com/developers/applications) and click 'New Application'
2. Go to **Bot** section → Uncheck 'Public Bot'
3. Enable all 3 **Privileged Gateway Intents**: Presence, Server Members, Message Content
4. Copy the bot token
5. Go to **OAuth2** → **URL Generator**
6. Check `bot` and `applications.commands` scopes
7. Copy the generated URL and add the bot to your server

## Setup Commands

### Plex Setup

```
/plexsettings setup <username> <password> <server name>
/plexsettings addrole <@role>       - Set auto-invite role
/plexsettings removerole <@role>    - Remove auto-invite role
/plexsettings setuplibs <libraries> - Set libraries (comma-separated)
/plexsettings enable                - Enable Plex integration
/plexsettings disable               - Disable Plex integration
```

### Jellyfin Setup

```
/jellyfinsettings setup <server url> <api key> <optional: external url>
/jellyfinsettings addrole <@role>       - Set auto-invite role
/jellyfinsettings removerole <@role>    - Remove auto-invite role
/jellyfinsettings setuplibs <libraries> - Set libraries (comma-separated)
/jellyfinsettings enable                - Enable Jellyfin integration
/jellyfinsettings disable               - Disable Jellyfin integration
```

## Manual Setup

1. Clone the repository
2. Add your Discord bot token to `bot.env`:
   ```
   discord_bot_token=YOUR_TOKEN_HERE
   seer_request_url=https://your-overseerr-url.com
   ```
3. Install dependencies: `pip3 install -r requirements.txt`
4. Start the bot: `python3 run.py`

## Migration from Invitarr

Membarr uses a slightly different database table than Invitarr. The migration is automatic, but **backup your app.db before running Membarr** as the new format is not backwards compatible.

You will also need to reinvite your Discord bot with both `bot` and `applications.commands` scopes.

## Contributing

Contributions are welcome! Fork the `dev` branch, make your changes, and open a pull request.

## Credits

- Original [Invitarr](https://github.com/Sleepingpirates/Invitarr) by Sleepingpirates
- [Membarr](https://github.com/Yoruio/Membarr) by Yoruio
- Named by lordfransie
