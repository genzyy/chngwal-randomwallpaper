#! /usr/bin/env python3

import os
import random

saveddir = "/home/rishit/Desktop/wallpapers"

allwalls = []

for root, dirs, files in os.walk(saveddir):
    for filename in files:
        allwalls.append(filename)

index = random.randrange(0, len(allwalls))
print('Setting up ' + allwalls[index] + ' as the wallpaper...')

bashCommand = 'feh --bg-scale ' + saveddir + '/' + allwalls[index]
os.system(bashCommand)