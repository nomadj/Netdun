import os
import sys
import asyncio
from time import sleep
import objects as obj
from random import randint
from threading import Event

verbs = {"take": 100, "open": 200, "attack": 300, "eat": 400}
nouns = {"sword": 1, "lamp": 2, "apple": 3, "monster": 4}
messages = {101: "Your attack is increased by 10 ", 102: "The lamp is not lit "}

verb = ''
noun = ''
action = 0
default_message = "What should I do? "
current_message = default_message

warrior = obj.Hero("warrior")
wizard = obj.Hero("wizard")
mage = obj.Hero("mage")

async def pause(sec):
    await asyncio.sleep(sec)

while True:
    os.system('clear')
    us_in = input(current_message)
    us_in = us_in.split()
    try:
        verb = us_in[0]
        for word in us_in:
            if word in nouns:
                noun = word
                break
    except:
        if len(us_in) == 0:
            current_message = default_message
            continue
        else:
            current_message = "That doesn't seem to work "
            continue

    try:
        action = verbs[verb] + nouns[noun]
        current_message = messages[action]
        print(f"You {verb} the {noun}")
        asyncio.run(pause(2))
    except:
        if verb in verbs and len(us_in) == 1:
            us_in = input(f"What would you like to {verb}? ")
            us_in = us_in.split()
            for word in us_in:
                if word in nouns:
                    noun = word
                    break
            try:
                action = verbs[verb] + nouns[noun]
                current_message = messages[action]
            except:
                current_message = "That doesn't seem to work "

        else:
            current_message = "That doesn't seem to work "
