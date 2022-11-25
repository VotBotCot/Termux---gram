import colorama
from colorama import Fore , Back , Style

import os
os.system('pip install pyrogram')
from pyrogram import Client, filters
from pyrogram.errors import FloodWait

from pyrogram.types import ChatPermissions

import time
from time import sleep

import random
user_text = ""
#регестрация

os.system('clear')

api_id = input("API_ID: ")
api_hash = input("API_HASH: ")

app = Client("my_account", api_id=api_id, api_hash=api_hash, lang_code="ru")
def rest():
    os.system('clear')
    print (Fore. RED+ "Termux - gram" )
    print(Fore. BLUE+ "V 1.4 (BETA)")
    print(Fore. GREEN+ "-----------------")
    print(" 1. Message")
    print(" 2. Contacts")
    print(" 3. Message (photo)")
    print(" 4. Get user")
    print(" 99. Exit")
    print(Fore. GREEN+ "-----------------")
    user_text = input(": ")
    user_text = str(user_text)

    # сообщение
    if user_text == "1" or user_text == "01":
        in_put = input("User: ")
        mes_s = input("Text: ")
        if not mes_s == "":
            if mes_s == ".":
                in_put = input("User: ")
            else:
                with app:
                    app.send_message(in_put, mes_s)
                    rest()
    else:
        if user_text == "99":
            exit()
        else:
            if user_text == "2" or user_text == "02":
                contacts = app.get_contacts()
                print(contacts)
                input("ENTER to continue")
                rest()
            else:
                if user_text == "3" or user_text == "03":
                    in_put = input("User: ")
                    mes_s = input("Photo: ")
                    if not mes_s == "":
                        if mes_s == ".":
                            in_put = input("User: ")
                        else:
                            with app:
                                app.send_photo(in_put, mes_s)
                                rest()
                else:
                    if user_text == "4" or user_text == "04":
                        in_put = input("User: ")
                        print(app.get_users(in_put))
                        input("ENTER to continue")
                        rest()
                    else:
                        rest()
rest()

app.run()

