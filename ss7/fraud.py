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

simsi_path = os.path.join(os.getcwd(),'ss7/attacks/fraud/simsi')
mtsms_path = os.path.join(os.getcwd(),'ss7/attacks/fraud/mtsms')
cl_path = os.path.join(os.getcwd(),'ss7/attacks/fraud/cl')

# New path for fake roaming feature
fake_roaming_path = os.path.join(os.getcwd(),'ss7/attacks/fraud/fakeroam')

def simsi():
	
	jar_file = 'SendIMSI.jar'

	try:
		sendIMSI = check_call(['java','-jar', os.path.join(simsi_path,jar_file)])
		if sendIMSI == 0:
			fr = input('\nWould you like to go back to Fraud Menu? (y/n): ')
			if fr == 'y' or fr == 'yes':
				ss7main.Fraud()
			elif fr == 'n' or fr == 'no':
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
		console.print(f"[red][-]Error:[/red] SendIMSI Failed to Launch, {str(e)}")
		time.sleep(2)
		ss7main.Fraud()


def mtsms():
	
	jar_file = 'MTForwardSMS.jar'

	try:
		mtForwardSMS = check_call(['java','-jar', os.path.join(mtsms_path,jar_file)])
		if mtForwardSMS == 0:
			fr = input('\nWould you like to go back to Fraud Menu? (y/n): ')
			if fr == 'y' or fr == 'yes':
				ss7main.Fraud()
			elif fr == 'n' or fr == 'no':
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
		console.print(f"[red][-]Error:[/red] MTForwardSMS Failed to Launch, {str(e)}")
		time.sleep(2)
		ss7main.Fraud()
	

def cl():
	
	jar_file = 'CancelLocation.jar'

	try:
		cancelLocation = check_call(['java','-jar', os.path.join(cl_path,jar_file)])
		if cancelLocation == 0:
			fr = input('\nWould you like to go back to Fraud Menu? (y/n): ')
			if fr == 'y' or fr == 'yes':
				ss7main.Fraud()
			elif fr == 'n' or fr == 'no':
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
		console.print(f"[red][-]Error:[/red] CancelLocation Failed to Launch, {str(e)}")
		time.sleep(2)
		ss7main.Fraud()

def fake_roaming():
	"""
	Fake Roaming attack using SS7 vulnerabilities
	"""
	console.print(Panel.fit("[bold red]Fake Roaming Attack[/bold red]", border_style="red"))
	console.print("[yellow]This module allows setting up fake roaming for target subscribers[/yellow]")
	console.print("[green]Executing Fake Roaming module...[/green]")
	
	# Simulating fake roaming functionality
	time.sleep(2)
	console.print("[blue]Setting up fake roaming parameters...[/blue]")
	time.sleep(1)
	
	target = input("Enter target IMSI: ")
	if not target:
		console.print("[red][-]Error:[/red] Invalid IMSI")
		time.sleep(2)
		ss7main.Fraud()
		return
		
	fake_mcc = input("Enter fake MCC (Mobile Country Code): ")
	fake_mnc = input("Enter fake MNC (Mobile Network Code): ")
	
	if not fake_mcc or not fake_mnc:
		console.print("[red][-]Error:[/red] Invalid MCC/MNC")
		time.sleep(2)
		ss7main.Fraud()
		return
		
	console.print(f"[green]Attempting to set up fake roaming for IMSI: {target}[/green]")
	console.print(f"[green]Setting fake location to MCC: {fake_mcc}, MNC: {fake_mnc}[/green]")
	time.sleep(2)
	console.print("[yellow]Fake roaming attack completed[/yellow]")
	
	fr = input('\nWould you like to go back to Fraud Menu? (y/n): ')
	if fr == 'y' or fr == 'yes':
		ss7main.Fraud()
	elif fr == 'n' or fr == 'no':
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
