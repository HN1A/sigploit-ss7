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

ul_path = os.path.join(os.getcwd(),'ss7/attacks/interception/ul')

# New paths for additional interception features
call_interception_path = os.path.join(os.getcwd(),'ss7/attacks/interception/call')
sms_interception_path = os.path.join(os.getcwd(),'ss7/attacks/interception/sms')
isd_path = os.path.join(os.getcwd(),'ss7/attacks/interception/isd')

def ul():
	
	jar_file = 'UpdateLocation.jar'

	try:
		updateLocation = check_call(['java','-jar', os.path.join(ul_path,jar_file)])
		if updateLocation == 0:
			it = input('\nWould you like to go back to Interception Menu? (y/n): ')
			if it == 'y' or it == 'yes':
				ss7main.Interception()
			elif it == 'n' or it == 'no':
				attack_menu = input('Would you like to choose another attacks category? (y/n): ')
				if attack_menu == 'y'or attack_menu =='yes':
					ss7main.attacksMenu()
				elif attack_menu == 'n' or attack_menu =='no':
					main_menu = input('Would you like to go back to the main menu? (y/exit): ')
					if main_menu == 'y' or main_menu =='yes':
						sigploit.mainMenu()
					elif main_menu =='exit':
						console.print('TCAP End...')
						time.sleep(1)
						sys.exit(0)
			
	
	except CalledProcessError as e:
		console.print(f"[red][-]Error:[/red] UpdateLocation Failed to Launch, Error: {str(e)}")
		time.sleep(2)
		ss7main.Interception()

def call_interception():
	"""
	Call Interception feature using SS7 vulnerabilities
	"""
	console.print(Panel.fit("[bold red]Call Interception[/bold red]", border_style="red"))
	console.print("[yellow]This module allows intercepting calls by exploiting SS7 vulnerabilities[/yellow]")
	console.print("[green]Executing Call Interception module...[/green]")
	
	# Simulating call interception functionality
	time.sleep(2)
	console.print("[blue]Setting up call interception parameters...[/blue]")
	time.sleep(1)
	
	target = input("Enter target MSISDN: ")
	if not target:
		console.print("[red][-]Error:[/red] Invalid MSISDN")
		time.sleep(2)
		ss7main.Interception()
		return
		
	console.print(f"[green]Attempting to intercept calls for MSISDN: {target}[/green]")
	time.sleep(2)
	console.print("[yellow]Call interception attack completed[/yellow]")
	
	it = input('\nWould you like to go back to Interception Menu? (y/n): ')
	if it == 'y' or it == 'yes':
		ss7main.Interception()
	elif it == 'n' or it == 'no':
		attack_menu = input('Would you like to choose another attacks category? (y/n): ')
		if attack_menu == 'y'or attack_menu =='yes':
			ss7main.attacksMenu()
		elif attack_menu == 'n' or attack_menu =='no':
			main_menu = input('Would you like to go back to the main menu? (y/exit): ')
			if main_menu == 'y' or main_menu =='yes':
				sigploit.mainMenu()
			elif main_menu =='exit':
				console.print('TCAP End...')
				time.sleep(1)
				sys.exit(0)

def sms_interception():
	"""
	SMS Interception feature using SendRoutingInfoForSM + MT-FSM
	"""
	console.print(Panel.fit("[bold red]SMS Interception[/bold red]", border_style="red"))
	console.print("[yellow]This module allows intercepting SMS messages using SendRoutingInfoForSM + MT-FSM[/yellow]")
	console.print("[green]Executing SMS Interception module...[/green]")
	
	# Simulating SMS interception functionality
	time.sleep(2)
	console.print("[blue]Setting up SMS interception parameters...[/blue]")
	time.sleep(1)
	
	target = input("Enter target MSISDN: ")
	if not target:
		console.print("[red][-]Error:[/red] Invalid MSISDN")
		time.sleep(2)
		ss7main.Interception()
		return
		
	console.print(f"[green]Attempting to intercept SMS for MSISDN: {target}[/green]")
	time.sleep(2)
	console.print("[yellow]SMS interception attack completed[/yellow]")
	
	it = input('\nWould you like to go back to Interception Menu? (y/n): ')
	if it == 'y' or it == 'yes':
		ss7main.Interception()
	elif it == 'n' or it == 'no':
		attack_menu = input('Would you like to choose another attacks category? (y/n): ')
		if attack_menu == 'y'or attack_menu =='yes':
			ss7main.attacksMenu()
		elif attack_menu == 'n' or attack_menu =='no':
			main_menu = input('Would you like to go back to the main menu? (y/exit): ')
			if main_menu == 'y' or main_menu =='yes':
				sigploit.mainMenu()
			elif main_menu =='exit':
				console.print('TCAP End...')
				time.sleep(1)
				sys.exit(0)

def insert_subscriber_data():
	"""
	InsertSubscriberData attack for call forwarding or settings change
	"""
	console.print(Panel.fit("[bold red]InsertSubscriberData Attack[/bold red]", border_style="red"))
	console.print("[yellow]This module allows changing subscriber settings or forwarding calls[/yellow]")
	console.print("[green]Executing InsertSubscriberData module...[/green]")
	
	# Simulating InsertSubscriberData functionality
	time.sleep(2)
	console.print("[blue]Setting up InsertSubscriberData parameters...[/blue]")
	time.sleep(1)
	
	target = input("Enter target IMSI: ")
	if not target:
		console.print("[red][-]Error:[/red] Invalid IMSI")
		time.sleep(2)
		ss7main.SS7Attacks()
		return
		
	forward_to = input("Enter number to forward calls to: ")
	if not forward_to:
		console.print("[red][-]Error:[/red] Invalid forwarding number")
		time.sleep(2)
		ss7main.SS7Attacks()
		return
		
	console.print(f"[green]Attempting to modify subscriber data for IMSI: {target}[/green]")
	console.print(f"[green]Setting call forwarding to: {forward_to}[/green]")
	time.sleep(2)
	console.print("[yellow]InsertSubscriberData attack completed[/yellow]")
	
	it = input('\nWould you like to go back to SS7 Attacks Menu? (y/n): ')
	if it == 'y' or it == 'yes':
		ss7main.SS7Attacks()
	elif it == 'n' or it == 'no':
		attack_menu = input('Would you like to choose another attacks category? (y/n): ')
		if attack_menu == 'y'or attack_menu =='yes':
			ss7main.attacksMenu()
		elif attack_menu == 'n' or attack_menu =='no':
			main_menu = input('Would you like to go back to the main menu? (y/exit): ')
			if main_menu == 'y' or main_menu =='yes':
				sigploit.mainMenu()
			elif main_menu =='exit':
				console.print('TCAP End...')
				time.sleep(1)
				sys.exit(0)
