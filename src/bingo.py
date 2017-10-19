#! /usr/bin/python

import time, random, os                 # Standard library modules
from espeak import espeak               # install espeak and espeak-devel, download module from launchpad.net/python-espeak
from pyfiglet import Figlet             # available on PyPI, install using pip
from prettytable import PrettyTable     # available on PyPI, install using pip

"""
The list comprehension here is creating a list consisting of 15 instances of the character 'B',
followed by 15 instances of the character 'I', and so on for the rest of the characters in "BINGO".

That list is zipped with a simple list of the integers 1-75.

The result of that zip is a list of tuples, with the first element of a tuple being an integer,
and the second element being a character from "BINGO".

That list of tuples is then converted into a dictionary of key: value pairs, with the integer
of each tuple as the key, and the character as the value.
"""
BINGO_NUMBERS = dict(zip(range(1,76), [c for c in "BINGO" for i in range(15)]))

# These set up the values to be shown in the table as lists of integers
B_COLUMN = range(1,16)
I_COLUMN = range(16,31)
N_COLUMN = range(31,46)
G_COLUMN = range(46,61)
O_COLUMN = range(61,76)

# Figlet displays large characters composed of single characters, think ASCII art.
# This initializes an instance of a Figlet class with its builtin font, 'doh'.
FigNums = Figlet(font="doh")

# espeak uses text-to-speech to tell players that Bingo will begin in 5 seconds.
# espeak.synth is asyncronous, so a timer is set to wait for six seconds once espeak starts speaking.
espeak.synth("Bingo begins in 5 seconds")
time.sleep(6)

# This is the main loop
def draw():
    os.system('clear')                                      # Clear the terminal screen
    popper = random.choice(BINGO_NUMBERS.keys())            # Choose a key at random from the above dictionary
    saythis = BINGO_NUMBERS.pop(popper)                     # Pop the key: value pair from the dict, then store the value in saythis
    print FigNums.renderText(saythis + "  " + str(popper))  # Print the chosen column letter and number in big characters
    
    # This if statement finds the chosen number in its column list and replaces the number with the same number, but with colors inverted.
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
    
    # Create and print the table of bingo numbers
    table = PrettyTable()
    table.add_column("B", B_COLUMN)
    table.add_column("I", I_COLUMN)
    table.add_column("N", N_COLUMN)
    table.add_column("G", G_COLUMN)
    table.add_column("O", O_COLUMN)
    print table
    
    # espeak calls out the letter and number, while waiting 3 seconds
    espeak.synth(saythis + str(popper))
    time.sleep(3)
        
# This while loop will run as long as there are key: value pairs in the dictionary
while BINGO_NUMBERS:
    try:
        draw()
    # This may be egregious use of Python's builtin keyboard interuption
    except KeyboardInterrupt:
        print '\nPausing...  (Hit ENTER to continue, type quit to exit.)'
        try:
            # If the user types quit, break out of the while loop
            response = raw_input()
            if response == 'quit':
                break
            print 'Resuming...'
        except KeyboardInterrupt:
            print 'Resuming...'
            continue

# After the while loop completes or is broken out of, say "Game Over" and execution finishes.
espeak.synth("Game Over")
time.sleep(1)