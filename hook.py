from dhooks import Webhook
import time
from time import sleep
from art import *
from colorama import *

tprint("Webhook   Spammer")
msg = input("Message : ")
hook = Webhook(input("Webhook : "))
sleeper = int(input("Delay : "))
while True:
    try:
        time.sleep(sleeper)
        hook.send(msg)
        print(f"{Fore.LIGHTGREEN_EX} [+] Sent{Fore.RESET}")
    except:
        print(f"{Fore.LIGHTRED_EX} [-] Failed{Fore.RESET}")
        sleep(1)
        print(f"{Fore.RED} [~] Invalid Webhook{Fore.RESET}")
        exit()