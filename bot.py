import discord
import os
import numpy as np
import re
def get_auth_keys(dir_loc):
    file_lines = []
    with open(dir_loc,'r') as f:
        for line in f:
            file_lines.append(line)
    keys = []
    for item in file_lines:
        pattern = re.compile(r'\n')
        key = item.split(' : ')[1]
        res = re.sub(pattern,'',key)
        keys.append(res)
    return keys

discord_keys = get_auth_keys('key.txt')
token = discord_keys[2]

client = discord.Client()
client.run(token)