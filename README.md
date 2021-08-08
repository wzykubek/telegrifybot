# Telegrify Bot

Telegram bot to find songs on Spotify and download 30 seconds 
preview with link to song in your chat.

Official instance: [@telegrifybot](https://t.me/telegrifybot)

## Installing with Docker Compose

- Clone repo to your machine
- Create `.env` file with `TOKEN`, `CLIENT_ID` and `CLIENT_SECRET` variables
    - `TOKEN` - bot API token from `@BotFather`
    - `CLIENT_ID` - Spotify API client ID*
    - `CLIENT_SECRET` - Spotify API client secret value*
- Run `docker-compose up` command
- Start using bot

\* Create new application on [Spotify Dashboard](https://developer.spotify.com/dashboard/applications) and copy Client ID and Client Secret (you need to click button to view it) values.