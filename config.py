# Copyright (c) 2025 Nand Yaduwanshi <NoxxOP>
# Location: Supaul, Bihar
#
# All rights reserved.
#
# This code is the intellectual property of Nand Yaduwanshi.
# You are not allowed to copy, modify, redistribute, or use this
# code for commercial or personal projects without explicit permission.
#
# Allowed:
# - Forking for personal learning
# - Submitting improvements via pull requests
#
# Not Allowed:
# - Claiming this code as your own
# - Re-uploading without credit or permission
# - Selling or using commercially
#
# Contact for permissions:
# Email: neethalwa720@gmail.com


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#     ⚙️ CONFIGURATION FILE | Powered By @VIP_MusicxBot & @SmartBoy_ApnaMS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

import os
import re
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📲 Telegram & API Credentials
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER_ID = int(os.getenv("OWNER_ID", None))
OWNER_USERNAME = os.getenv("OWNER_USERNAME", "SmartBoy_ApnaMS")
BOT_USERNAME = os.getenv("BOT_USERNAME", "VIP_MusicxBot")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🛠️ Database & Deployment Configs
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

MONGO_DB_URI = os.getenv("MONGO_DB_URI", None)
LOG_GROUP_ID = int(os.getenv("LOG_GROUP_ID", None))
HEROKU_APP_NAME = os.getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = os.getenv("HEROKU_API_KEY")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🔄 Git & Update Settings
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

UPSTREAM_REPO = os.getenv("UPSTREAM_REPO", "https://github.com/NoxxOP/ShrutiMusic")
UPSTREAM_BRANCH = os.getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = os.getenv("GIT_TOKEN", None)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🔗 Support Links
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SUPPORT_CHANNEL = os.getenv("SUPPORT_CHANNEL", "https://t.me/NEET_Saathi")
SUPPORT_GROUP = os.getenv("SUPPORT_GROUP", "https://t.me/Neet_Saathi_Counter")
INSTAGRAM = os.getenv("INSTAGRAM", "https://www.instagram.com/smartboy_apnams?igsh=MXJucDJhOTF2b3g1Yg==")
YOUTUBE = os.getenv("YOUTUBE", "https://youtube.com/@smartyms-1?si=Graz2DXs52kq_Mjo")
GITHUB = os.getenv("GITHUB", "https://github.com/NoxxOP")
DONATE = os.getenv("DONATE", "https://t.me/NEET_Saathi")
PRIVACY_LINK = os.getenv("PRIVACY_LINK", "https://graph.org/Privacy-Policy-05-01-30")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ⏱️ Duration & Playlist Settings
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

DURATION_LIMIT_MIN = int(os.getenv("DURATION_LIMIT", 300))
PLAYLIST_FETCH_LIMIT = int(os.getenv("PLAYLIST_FETCH_LIMIT", 25))

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📦 File Size Limits (in bytes)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

TG_AUDIO_FILESIZE_LIMIT = int(os.getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(os.getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496))

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🎧 Spotify Developer Credentials
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET", None)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🧵 Session Strings (Pyrogram V2)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STRING1 = os.getenv("STRING_SESSION", None)
STRING2 = os.getenv("STRING_SESSION2", None)
STRING3 = os.getenv("STRING_SESSION3", None)
STRING4 = os.getenv("STRING_SESSION4", None)
STRING5 = os.getenv("STRING_SESSION5", None)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ⚙️ Runtime Configurations
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

AUTO_LEAVING_ASSISTANT = bool(os.getenv("AUTO_LEAVING_ASSISTANT", False))

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🖼️ Image URLs (Can be customized)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

START_IMG_URL = os.getenv("START_IMG_URL", "https://graph.org/file/29dfb41748ec7561eac20-45780a2f354a627bda.jpg")
PING_IMG_URL = "https://graph.org/file/b9f4ac553ba9975d7310d-ceca3a3be736f769a1.jpg"
PLAYLIST_IMG_URL = "https://graph.org/file/3a563ac34a097dfd05748-db44ef6b00fdf45615.jpg"
STATS_IMG_URL = "https://graph.org/file/d63cb61f334951ef61b1b-9dcace3e89dc0f79fb.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/65bee91f058d5dd83319f-e2758fbd86bd4fb890.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/e7b85af0129633342e319-88358f7442535860fb.jpg"
STREAM_IMG_URL = "https://graph.org/file/11775f70848825604e558-83e2d0e2b563321ca4.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/fe802bf918ba1828de32a-e82fc2c9af7af46904.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/95d7b9bacbde8cb91b892-e37407d3868445138f.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/443787846a2b43a108d47-9f897aeca88db0801e.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/f94c695f2e8665aab70c7-f6bd332b661f653dc1.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/8cb276fcdb1863e14984d-6f0b70874587011817.jpg"

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🔐 User & Bot State Stores
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

TEMP_DB_FOLDER = "tempdb"
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ⏳ Time Conversion Utility
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))

DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ❌ Validate Support Links
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

if SUPPORT_CHANNEL:
    if not re.match(r"(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - SUPPORT_CHANNEL URL is invalid. It must start with https://"
        )

if SUPPORT_GROUP:
    if not re.match(r"(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - SUPPORT_GROUP URL is invalid. It must start with https://"
        )

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#     ✅ CONFIG LOADED SUCCESSFULLY | Designed By @VIP_MusicxBot
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


# ©️ Copyright Reserved - @NoxxOP  Nand Yaduwanshi

# ===========================================
# ©️ 2025 Nand Yaduwanshi (aka @NoxxOP)
# 🔗 GitHub : https://github.com/NoxxOP/ShrutiMusic
# 📢 Telegram Channel : https://t.me/ShrutiBots
# ===========================================


# ❤️ Love From ShrutiBots 
