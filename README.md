# Telegrify

[Telegram bot](https://t.me/telegrifybot) to find songs on Spotify and download 30 seconds preview with link to your chat.

## Usage

Use `/start` or `/help` option to display available commands.

## Self-hosting

+ Clone this repo.
```
$ git clone https://github.com/samedamci/telegrifybot && cd telegrifybot
```
+ Install required modules.
```
$ pip3 install --user -r requirements.txt
```
+ Create `environment` file with your bot token and instance URL.
```
TOKEN=your_token_here
```
+ Start bot with `python3 main.py`.

### With Docker

+ Build image itself.
```
# docker build -t samedamci/searx_bot .
```
+ Run bot in container.
```
# docker run --rm -d -e TOKEN='your_token_here' --name telegrifybot samedamci/telegrifybot
```
