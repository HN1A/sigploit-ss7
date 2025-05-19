#!/usr/bin/env python3
'''
Created on 1 Feb 2025

@author: ꧁༒☬Al-Muheb☬༒꧂
'''

import sys
import os
import signal
import time
from ss7.tracking import *
from ss7.interception import *
from ss7.fraud import *
from ss7.dos import *
from ss7main import *
from rich.console import Console
from rich.text import Text
from rich import print as rprint
from rich.panel import Panel
from rich.table import Table

console = Console()

def banner(word):
    letterforms = '''\
       |       |       |       |       |       |       | |
  XXX  |  XXX  |  XXX  |   X   |       |  XXX  |  XXX  |!|
  X  X |  X  X |  X  X |       |       |       |       |"|
  X X  |  X X  |XXXXXXX|  X X  |XXXXXXX|  X X  |  X X  |#|
 XXXXX |X  X  X|X  X   | XXXXX |   X  X|X  X  X| XXXXX |$|
XXX   X|X X  X |XXX X  |   X   |  X XXX| X  X X|X   XXX|%|
  XX   | X  X  |  XX   | XXX   |X   X X|X    X | XXX  X|&|
  XXX  |  XXX  |   X   |  X    |       |       |       |'|
   XX  |  X    | X     | X     | X     |  X    |   XX  |(|
  XX   |    X  |     X |     X |     X |    X  |  XX   |)|
       | X   X |  X X  |XXXXXXX|  X X  | X   X |       |*|
       |   X   |   X   | XXXXX |   X   |   X   |       |+|
       |       |       |  XXX  |  XXX  |   X   |  X    |,|
       |       |       | XXXXX |       |       |       |-|
       |       |       |       |  XXX  |  XXX  |  XXX  |.|
      X|     X |    X  |   X   |  X    | X     |X      |/|
  XXX  | X   X |X     X|X     X|X     X| X   X |  XXX  |0|
   X   |  XX   | X X   |   X   |   X   |   X   | XXXXX |1|
 XXXXX |X     X|      X| XXXXX |X      |X      |XXXXXXX|2|
 XXXXX |X     X|      X| XXXXX |      X|X     X| XXXXX |3|
X      |X    X |X    X |X    X |XXXXXXX|     X |     X |4|
XXXXXXX|X      |X      |XXXXXX |      X|X     X| XXXXX |5|
 XXXXX |X     X|X      |XXXXXX |X     X|X     X| XXXXX |6|
XXXXXX |X    X |    X  |   X   |  X    |  X    |  X    |7|
 XXXXX |X     X|X     X| XXXXX |X     X|X     X| XXXXX |8|
 XXXXX |X     X|X     X| XXXXXX|      X|X     X| XXXXX |9|
   X   |  XXX  |   X   |       |   X   |  XXX  |   X   |:|
  XXX  |  XXX  |       |  XXX  |  XXX  |   X   |  X    |;|
    X  |   X   |  X    | X     |  X    |   X   |    X  |<|
       |       |XXXXXXX|       |XXXXXXX|       |       |=|
  X    |   X   |    X  |     X |    X  |   X   |  X    |>|
 XXXXX |X     X|      X|   XXX |   X   |       |   X   |?|
 XXXXX |X     X|X XXX X|X XXX X|X XXXX |X      | XXXXX |@|
   X   |  X X  | X   X |X     X|XXXXXXX|X     X|X     X|A|
XXXXXX |X     X|X     X|XXXXXX |X     X|X     X|XXXXXX |B|
 XXXXX |X     X|X      |X      |X      |X     X| XXXXX |C|
XXXXXX |X     X|X     X|X     X|X     X|X     X|XXXXXX |D|
XXXXXXX|X      |X      |XXXXX  |X      |X      |XXXXXXX|E|
XXXXXXX|X      |X      |XXXXX  |X      |X      |X      |F|
 21.45 |6     8|7      |2   lat|x1    x5|9     4| 31.74 |G|
X     X|X     X|X     X|XXXXXXX|X     X|X     X|X     X|H|
  XXX  |   X   |   X   |   X   |   X   |   X   |  XXX  |I|
      X|      X|      X|      X|X     X|X     X| XXXXX |J|
X    X |X   X  |X  X   |XXX    |X  X   |X   X  |X    X |K|
X      |X      |X      |X      |X      |X      |XXXXXXX|L|
X     X|XX   XX|X X X X|X  X  X|X     X|X     X|X     X|M|
X     X|XX    X|X X   X|X  X  X|X   X X|X    XX|X     X|N|
XXXXXXX|X     X|X     X|X     X|X     X|X     X|XXXXXXX|O|
XXXXXX |X     X|X     X|XXXXXX |X      |X      |X      |P|
 XXXXX |X     X|X     X|X     X|X   X X|X    X | XXXX X|Q|
XXXXXX |X     X|X     X|XXXXXX |X   X  |X    X |X     X|R|
 _IMSI |0x1  GT|PC     | _IMEI |     CI|Kc  421| _HLR_ |S|
XXXXXXX|   X   |   X   |   X   |   X   |   X   |   X   |T|
X     X|X     X|X     X|X     X|X     X|X     X| XXXXX |U|
X     X|X     X|X     X|X     X| X   X |  X X  |   X   |V|
X     X|X  X  X|X  X  X|X  X  X|X  X  X|X  X  X| XX XX |W|
X     X| X   X |  X X  |   X   |  X X  | X   X |X     X|X|
X     X| X   X |  X X  |   X   |   X   |   X   |   X   |Y|
XXXXXXX|     X |    X  |   X   |  X    | X     |XXXXXXX|Z|
 XXXXX | X     | X     | X     | X     | X     | XXXXX |[|
X      | X     |  X    |   X   |    X  |     X |      X|\|
 XXXXX |     X |     X |     X |     X |     X | XXXXX |]|
   X   |  X X  | X   X |       |       |       |       |^|
       |       |       |       |       |       |XXXXXXX|_|
       |  XXX  |  XXX  |   X   |    X  |       |       |`|
       |   XX  |  X  X | X    X| XXXXXX| X    X| X    X|a|
       | XXXXX | X    X| XXXXX | X    X| X    X| XXXXX |b|
       |  XXXX | X    X| X     | X     | X    X|  XXXX |c|
       | XXXXX | X    X| X    X| X    X| X    X| XXXXX |d|
       | XXXXXX| X     | XXXXX | X     | X     | XXXXXX|e|
       | XXXXXX| X     | XXXXX | X     | X     | X     |f|
       |  XXXX | X    X| X     | X  XXX| X    X|  XXXX |g|
       | X    X| X    X| XXXXXX| X    X| X    X| X    X|h|
       |  E    |  n    |  C    |  r    |  P    |  T    |i|
       |      X|      X|      X|      X| X    X|  XXXX |j|
       | X    X| X   X | XXXX  | X  X  | X   X | X    X|k|
       | GT    | PC    | x7    |x6    | x8    | Fraud |l|
       | X    X| XX  XX| X XX X| X    X| X    X| X    X|m|
       | X    X| XX   X| X X  X| X  X X| X   XX| X    X|n|
       |  SGSN | X    X| X    X| X    X| X    X|  gGsN |o|
       | Track | 6    8| s    i|credit | Kc    | G     |p|
       |  XXXX | X    X| X    X| X  X X| X   X |  XXX X|q|
       | XXXXX | X    X| X    X| XXXXX | X   X | X    X|r|
       |  XXXX | X     |  XXXX |      X| X    X|  XXXX |s|
       |--USIM-- |   x0  |   x2  |   x3  |   x8  |   x6  |t|
       | X    X| X    X| X    X| X    X| X    X|  XXXX |u|
       | X    X| X    X| X    X| X    X|  X  X |   XX  |v|
       | X    X| X    X| X    X| X XX X| XX  XX| X    X|w|
       | X    X|  X  X |   XX  |   XX  |  X  X | X    X|x|
       |  X   X|   X X |    X  |    X  |    X  |    X  |y|
       | XXXXXX|     X |    X  |   X   |  X    | XXXXXX|z|
  XXX  | X     | X     |XX     | X     | X     |  XXX  |{|
   X   |   X   |   X   |       |   X   |   X   |   X   |||
  XXX  |     X |     X |     XX|     X |     X |  XXX  |}|
 XX    |X  X  X|    XX |       |       |       |       |~|
'''.splitlines()

    table = {}
    for form in letterforms:
        if '|' in form:
            table[form[-2]] = form[:-3].split('|')

    ROWS = len(list(table.values())[0])

    for row in range(ROWS):
        for c in word:
            print(table[c][row], end=' ')
        print()
    print()


def mainMenu():
    os.system('clear')
    
    # Rich library enhanced banner
    console = Console()
    console.print(Panel.fit("[bold red]SiGploit SS7[/bold red]", border_style="red"))
    
    banner('SiGploit')
    
    console.print("[yellow][-][-][/yellow]\t\tSignaling Exploitation Framework\t[yellow][-][-][/yellow]")
    console.print("[yellow][-][-][/yellow]\t\t\tVersion:[red]BETA 0.4[/red]\t\t[yellow][-][-][/yellow]")
    console.print("[yellow][-][-][/yellow]\t\tAuthor:[green]꧁༒☬Al-Muheb☬༒꧂(@NH1A)[/green]\t[yellow][-][-][/yellow]\n")
    
    console.print("")
    console.print("Contributors:")
    console.print("\t[red]Rosalia D'Alessandro - TelecomItalia[/red]")
    console.print("")
    console.print("")
    console.print("")
    console.print("")
    console.print("")
    
    # Create a table for modules
    table = Table(title="Available Modules")
    table.add_column("Module", justify="right", style="cyan")
    table.add_column("Description", style="green")
    
    table.add_row("0) SS7", "2G/3G Voice and SMS attacks")
    table.add_row("1) Diameter", "4G Data attacks")
    table.add_row("2) GTP", "3G Data attacks")
    table.add_row("3) SIP", "4G VoLTE attacks")
    
    console.print(table)
    console.print("")
    console.print("or quit to exit SiGploit\n".rjust(28))

    choice = input("\033[34msig\033[0m\033[37m>\033[0m ")

    if choice == "0":
        os.system('clear')
        ss7main.attacksMenu()

    if choice == "1":
        console.print("\n[blue][*][/blue]Diameter will be updated in version 2 release..")
        console.print("[blue][*][/blue]Going back to Main Menu")
        time.sleep(2)
        mainMenu()
    elif choice == "2":
        console.print("\n[blue][*][/blue]GTP will be updated in version 3 release..")
        console.print("[blue][*][/blue]Going back to Main Menu")
        time.sleep(2)
        mainMenu()
    elif choice == "3":
        console.print("\n[blue][*][/blue]SIP will be updated in version 4 release..")
        console.print("[blue][*][/blue]Going back to Main Menu")
        time.sleep(2)
        mainMenu()
    elif choice == "quit" or choice == "exit":
        console.print('\nYou are now exiting SiGploit...')
        time.sleep(1)
        sys.exit(0)
    else:
        console.print('\n[red][-]Error:[/red] Please Enter a Valid Choice (0 - 3)')
        time.sleep(2)
        mainMenu()


def signal_handler(signal, frame):
    console.print('\nYou are now exiting SiGploit...')
    time.sleep(1)
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

if __name__ == '__main__':
    mainMenu()

if __name__ == '__sigploit__':
    LocationTracking()
    Interception()
    Fraud()
    DoS()
    attacksMenu()
    mainMenu()
