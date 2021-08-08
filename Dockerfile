FROM python:3.9.5-slim

LABEL maintainer="samedamci@disroot.org"
LABEL org.opencontainers.image.source https://github.com/samedamci/telegrifybot

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ENV TOKEN TOKEN
ENV CLIENT_ID CLIENT_ID
ENV CLIENT_SECRET CLIENT_SECRET

COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /bot
COPY . /bot

RUN adduser -u 5678 --disabled-password --gecos "" botuser && chown -R botuser /bot
USER botuser

CMD ["python3", "run.py"]
