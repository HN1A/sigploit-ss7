#!/usr/bin/env python3
'''
Created on 1 Feb 2025

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

sri_path = os.path.join(os.getcwd(),'ss7/attacks/tracking/sri')
srism_path = os.path.join(os.getcwd(),'ss7/attacks/tracking/srism')
psi_path = os.path.join(os.getcwd(),'ss7/attacks/tracking/psi')
ati_path = os.path.join(os.getcwd(),'ss7/attacks/tracking/ati')
srigprs_path = os.path.join(os.getcwd(),'ss7/attacks/tracking/srigprs')



def sri():
	
	jar_file = 'SendRoutingInfo.jar'

	try:
		sendRoutingInfo = check_call(['java','-jar', os.path.join(sri_path,jar_file)])
		if sendRoutingInfo == 0:
			lt = input('\nWould you like to go back to LocationTracking Menu? (y/n): ')
			if lt == 'y' or lt == 'yes':
				ss7main.LocationTracking()
			elif lt == 'n' or lt == 'no':
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
		console.print(f"[red][-]Error:[/red] SendRoutingInfo Failed to Launch, {str(e)}")
		time.sleep(2)
		ss7main.LocationTracking()
	

def psi():
	
	jar_file = 'ProvideSubscriberInfo.jar'
	
	try:
		psi = check_call(['java','-jar', os.path.join(psi_path,jar_file)])
		if psi == 0:
			lt = input('\nWould you like to go back to LocationTracking Menu? (y/n): ')
			if lt == 'y' or lt == 'yes':
				ss7main.LocationTracking()
			elif lt == 'n' or lt == 'no':
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
		console.print(f"[red][-]Error:[/red] {jar_file} Failed to Launch, {str(e)}")
		time.sleep(2)
		ss7main.LocationTracking()

def srism():
	jar_file = 'SendRoutingInfoForSM.jar'

	try:
		srism = check_call(['java','-jar', os.path.join(srism_path,jar_file)])
		if srism == 0:
			lt = input('\nWould you like to go back to LocationTracking Menu? (y/n): ')
			if lt == 'y' or lt == 'yes':
				ss7main.LocationTracking()
			elif lt == 'n' or lt == 'no':
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
		console.print(f"[red][-]Error:[/red] {jar_file} Failed to Launch, {str(e)}")
		time.sleep(2)
		ss7main.LocationTracking()

def ati():
	jar_file = 'AnyTimeInterrogation.jar'

	try:
		ati = check_call(['java','-jar', os.path.join(ati_path,jar_file)])
		if ati == 0:
			lt = input('\nWould you like to go back to LocationTracking Menu? (y/n): ')
			if lt == 'y' or lt == 'yes':
				ss7main.LocationTracking()
			elif lt == 'n' or lt == 'no':
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
		console.print(f"[red][-]Error:[/red] {jar_file} Failed to Launch, {str(e)}")
		time.sleep(2)
		ss7main.LocationTracking()

def srigprs():
	jar_file = 'SendRoutingInfoForGPRS.jar'
	
	try:
		srigprs = check_call(['java','-jar', os.path.join(srigprs_path,jar_file)])
		if srigprs == 0:
			lt = input('\nWould you like to go back to LocationTracking Menu? (y/n): ')
			if lt == 'y' or lt == 'yes':
				ss7main.LocationTracking()
			elif lt == 'n' or lt == 'no':
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
		console.print(f"[red][-]Error:[/red] {jar_file} Failed to Launch, {str(e)}")
		time.sleep(2)
		ss7main.LocationTracking()
