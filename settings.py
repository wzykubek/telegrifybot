#!/usr/bin/env python3

import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "environment")
load_dotenv(dotenv_path)

TOKEN = os.getenv("TOKEN")
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

SOURCE_URL = "https://github.com/samedamci/telegrifybot"
