import os
from random import *
import random
import discord
from dotenv import load_dotenv
async def on_message(message):
    if message.content.startswith('$game'):
            Interger1 = randint(1,5000)
            Interger2 = randint(1,5000)
            Operations = ['Plus ', 'Minus ', 'Times ', 'Divided by ']
            Operation = random.choice(Operations) 
            StartGame = 'What is ' + str(Interger1) + ' ' + Operation + str(Interger2)
            match Operation:
                case 'Plus ':
                    result = Interger1 + Interger2
                case 'Minus ':
                    result = Interger1 - Interger2
                case 'Times ':
                    result = Interger1 * Interger2  
                case 'Divided by ':
                    result = Interger1 / Interger2
                case _: 
                    print("Error")
            await message.channel.send(StartGame)
            Answer = await client.wait_for('message')
            if Answer == result:
                await message.channel.send('Correct!') 
            else:
                await message.channel.send('Wrong! The Answer was ' + str(result))