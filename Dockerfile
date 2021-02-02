FROM python:3.9-alpine

LABEL maintainer="samedamci@disroot.org"

ENV TOKEN TOKEN
ENV CLIENT_ID CLIENT_ID
ENV CLIENT_SECRET CLIENT_SECRET

RUN apk add --no-cache gcc musl-dev linux-headers libc-dev libffi-dev libressl-dev && \
	pip3 install python-telegram-bot python-dotenv spotipy && \
	mkdir /opt/bot && \
	apk del gcc musl-dev linux-headers libc-dev libressl-dev

COPY . /opt/bot/

RUN cd /opt/bot && \
    rm -rf README.md LICENSE requirements.txt .git*

CMD cd /opt/bot/ && python3 main.py
