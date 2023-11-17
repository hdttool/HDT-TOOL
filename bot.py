import requests
import random
from datetime import datetime, timedelta
from threading import Thread, Timer
import os
import telebot
import re
import sqlite3
import webbrowser
from telebot import types
import time
import base64
import subprocess

bot_start_time = datetime.now()
current_time = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
def poll_bot():
    while True:
        try:
            bot.polling(timeout=500000)
        except Exception as e:
            print(f"Có lỗi xảy ra: {e}")
            print("Thử lại sau 5 giây...")
            time.sleep(5)

os.system('clear')
logo=f"""
\033[1;34m╔═════════════════════════════════════════════════════════════════╗
\033[1;34m║\033[1;31m██╗░░██╗██████╗░████████╗░░░░░░████████╗░█████╗░░█████╗░██╗░░░░░ \033[1;34m║
\033[1;34m║\033[1;33m██║░░██║██╔══██╗╚══██╔══╝░░░░░░╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░ \033[1;34m║
\033[1;34m║\033[1;34m███████║██║░░██║░░░██║░░░█████╗░░░██║░░░██║░░██║██║░░██║██║░░░░░ \033[1;34m║
\033[1;34m║\x1b[38;5;46m██╔══██║██║░░██║░░░██║░░░╚════╝░░░██║░░░██║░░██║██║░░██║██║░░░░░ \033[1;34m║
\033[1;34m║\033[1;36m██║░░██║██████╔╝░░░██║░░░░░░░░░░░░██║░░░╚█████╔╝╚█████╔╝███████╗ \033[1;34m║
\033[1;34m║\x1b[38;5;208m╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░░░░░░░░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝ \033[1;34m║
\033[1;34m╠═════════════════════════════════════════════════════════════════╣
\033[1;34m║\x1b[38;5;46m➢ Author   : \x1b[38;5;208mHDT - TOOL                                          \033[1;34m║
\033[1;34m║\x1b[38;5;46m➢ Youtube  : \x1b[38;5;208mhttps://youtube.com/@HDT-TOOL                       \033[1;34m║
\033[1;34m║\x1b[38;5;46m➣ Nhóm Zalo  : \x1b[38;5;208mhttps://zalo.me/g/bprmyn080                       \033[1;34m║
\033[1;34m║\x1b[38;5;46m➣ Website  : \x1b[38;5;208mhttps://hdt-tool.blogspot.com                      \033[1;34m ║
\033[1;34m╚═════════════════════════════════════════════════════════════════╝
\033[1;32m ➣ ➣ ➣ ➣ ➣ ➣ \033[1;33mĐang Chạy Bot 🍁 HDT - TOOL🍁 \033[1;32m➣ ➣ ➣ ➣ ➣ ➣"""
  
print(logo)
bot_token = '6371697348:AAHbr8iJD0CgV0kL8Pg6TpwHBlGuBLFBEJw' #thay token bot nha ae token lấy ở botfather 

header = {"Accept": "application/json", "Content-Type": "application/json"}

bot = telebot.TeleBot(bot_token)
session = requests.Session()

allowed_users = []
processes = []
ADMIN_ID = 6371697348 

allowed_users.extend([ADMIN_ID])

import requests
import random
from datetime import datetime
video_links = [
    "https://hdttool2023.000webhostapp.com/_.mp4",
    "https://hdttool2023.000webhostapp.com/+.mp4",
    "https://baohayhomnay24h.000webhostapp.com/video/3.mp4",
    "https://baohayhomnay24h.000webhostapp.com/video/4.mp4",
    "https://baohayhomnay24h.000webhostapp.com/video/5.mp4",
    "https://baohayhomnay24h.000webhostapp.com/video/6.mp4",
    "https://baohayhomnay24h.000webhostapp.com/video/7.mp4",
    "https://baohayhomnay24h.000webhostapp.com/video/8.mp4",
]

user_key_count = {}
@bot.message_handler(commands=['get_key'])
def get_key(message):
    ngay = int(datetime.now().strftime('%d'))
    key1=str(ngay*1246881818+2888181472)
    key = 'HDT-' + key1
    url = 'http://off-vn.x10.mx/index.html?key=' + key
    print(key)
    like4m = requests.get(f'https://link4m.co/api-shorten/v2?api=64dede03981c99475d22f97f&url={url}').json()
    web1s = requests.get(f'https://link4m.co/api-shorten/v2?api=64dede03981c99475d22f97f&url={url}').json()
    if like4m['status'] == "error":
        bot.reply_to(message, like4m['message'])
    else:
        link_key1 = like4m['shortenedUrl']
        
    if web1s['status'] == "error":
        bot.reply_to(message, web1s['message'])
    else:
        link_key2 = web1s['shortenedUrl']
        random_video_url = random.choice(video_links)
        current_time = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        user_id = message.from_user.id
        if user_id not in user_key_count:
            user_key_count[user_id] = 1
        else:
            user_key_count[user_id] += 1
        
        key_count = user_key_count[user_id]
        message_text = f'🌺Admin Tool: HDT-TOOL 🌺\nLưu ý 🚨: Đây là key Tool không phải key bot\nBot 🔑: https://t.me/hdttoolbot\nChủ sở hữu 👑: https://t.me/hdttoolbot\nLấy key lúc🔑: {current_time}\nNhóm Zalo📨: https://zalo.me/g/bprmyn080\nLink Key 1 🔑: {link_key1}'

        bot.send_video(message.chat.id, random_video_url, caption=message_text, parse_mode='html')

@bot.message_handler(commands=['start'])
def check_uptime(message):
    current_time = datetime.now()
    uptime = current_time - bot_start_time
    days = uptime.days
    hours, remainder = divmod(uptime.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    uptime_str = f"{days} days, {hours}:{minutes:02}:{seconds:02}"
    bot.reply_to(message, f"Chào mừng bạn đã đến với 💸 TOOL- Server Minecraft 💸. Nhập /get_key để lấy key.\n🤖 Bot đã hoạt động trong {uptime_str}. 🤖")

bot.polling()

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, '🚀Lệnh không hợp lệ. Vui lòng sử dụng lệnh /start để xem danh sách lệnh.🚀')

if __name__ == "__main__":
  bot.polling()