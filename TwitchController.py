import twitchlogo
import socket
import threading
import keyboard
import pyautogui
import os
from dotenv import load_dotenv
load_dotenv()


# importing env settings
SERVER = os.getenv("SERVER")
PORT = os.getenv("PORT")
PASS = os.getenv("PASS")
BOT = os.getenv("BOT")
CHANNEL = os.getenv("CHANNEL")
OWNER = os.getenv("OWNER")


def program():

    twitchlogo.print_twitch_logo()