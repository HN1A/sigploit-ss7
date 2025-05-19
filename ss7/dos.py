#!/usr/bin/env python3

'''
Created on 8 Feb 2025

@author: ꧁༒☬Al-Muheb☬༒꧂
'''

import sys
import os
import time
import sigploit
import ss7main
from subprocess import *
from rich.console import Console
from rich.panel import Panel

console = Console()

purge_path = os.path.join(os.getcwd(),'ss7/attacks/dos/prgms')

def purge():
	
	jar_file = 'PurgeMS.jar'

	try:
		purgeMS = check_call(['java','-jar', os.path.join(purge_path,jar_file)])
		if purgeMS == 0:
			ds = input('\nWould you like to go back to DoS Menu? (y/n): ')
			if ds == 'y' or ds == 'yes':
				ss7main.DoS()
			elif ds == 'n' or ds == 'no':
				attack_menu = input('Would you like to choose another attacks category? (y/n): ')
				if attack_menu == 'y'or attack_menu =='yes':
					ss7main.attacksMenu()
				elif attack_menu == 'n' or attack_menu =='no':
					main_menu = input('Would you like to go back to the main menu? (y/exit): ')
					if main_menu == 'y' or main_menu =='yes':
						sigploit.mainMenu()
					elif main_menu =='exit':
						console.print('TCAP End...')
						sys.exit(0)
			
	
	except CalledProcessError as e:
		console.print(f"[red][-][/red]Error: PurgeMS Failed to Launch, {str(e)}")
		time.sleep(2)
		ss7main.DoS()
