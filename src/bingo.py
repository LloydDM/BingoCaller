#! /usr/bin/python

import time, random, os
from espeak import espeak
from pyfiglet import Figlet
from prettytable import PrettyTable

BINGO_NUMBERS = dict(zip([x+1 for x in range(75)], [x for x in "BINGO" for i in range(15)]))
B_COLUMN = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
I_COLUMN = [16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
N_COLUMN = [31,32,33,34,35,36,37,38,39,40,41,42,43,44,45]
G_COLUMN = [46,47,48,49,50,51,52,53,54,55,56,57,58,59,60]
O_COLUMN = [61,62,63,64,65,66,67,68,69,70,71,72,73,74,75]

FigNums = Figlet(font="doh")

espeak.synth("Bingo begins in 5 seconds")
time.sleep(6)

def draw():
    os.system('clear')
    popper = random.choice(BINGO_NUMBERS.keys())
    saythis = BINGO_NUMBERS.pop(popper)
    print FigNums.renderText(saythis + "  " + str(popper))
    
    if 1 <= popper <= 15:
        B_COLUMN[B_COLUMN.index(popper)] = '\x1b[7m'+str(popper)+'\x1b[27m'
    elif 16 <= popper <= 30:
        I_COLUMN[I_COLUMN.index(popper)] = '\x1b[7m'+str(popper)+'\x1b[27m'
    elif 31 <= popper <= 45:
        N_COLUMN[N_COLUMN.index(popper)] = '\x1b[7m'+str(popper)+'\x1b[27m'
    elif 46 <= popper <= 60:
        G_COLUMN[G_COLUMN.index(popper)] = '\x1b[7m'+str(popper)+'\x1b[27m'
    elif 61 <= popper <= 75:
        O_COLUMN[O_COLUMN.index(popper)] = '\x1b[7m'+str(popper)+'\x1b[27m'
    
    table = PrettyTable()
#   table.border=False
    table.add_column("B", B_COLUMN)
    table.add_column("I", I_COLUMN)
    table.add_column("N", N_COLUMN)
    table.add_column("G", G_COLUMN)
    table.add_column("O", O_COLUMN)
    print table
    
    espeak.synth(saythis + str(popper))
    time.sleep(3)
        
while BINGO_NUMBERS:
    try:
        draw()
    except KeyboardInterrupt:
        print '\nPausing...  (Hit ENTER to continue, type quit to exit.)'
        try:
            response = raw_input()
            if response == 'quit':
                break
            print 'Resuming...'
        except KeyboardInterrupt:
            print 'Resuming...'
            continue

espeak.synth("Game Over")
time.sleep(1)