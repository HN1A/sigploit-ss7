#!/usr/bin/env python3
# encoding: utf-8
'''
SS7 main 

@author:    ꧁༒☬Al-Muheb☬༒꧂

@copyright:  2025 All rights reserved.

@license:    MIT license
'''

import os
import time
import ss7.tracking
import ss7.fraud
import ss7.interception
import ss7.dos
import ss7.real_attacks
import sigploit
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

def LocationTracking():
    os.system('clear')

    console.print(Panel.fit("[bold red]Location Tracking[/bold red]", border_style="red"))
    console.print(Panel.fit("[bold blue]Select a Message from the below[/bold blue]", border_style="blue"))
    
    # Create a table for tracking options
    table = Table()
    table.add_column("Message", justify="right", style="cyan")
    table.add_column("Category", style="green")
    
    table.add_row("0) SendRoutingInfo", "CAT1")
    table.add_row("1) ProvideSubsriberInfo", "CAT2")
    table.add_row("2) SendRoutingInfoForSM", "CAT3")
    table.add_row("3) AnyTimeInterrogation", "CAT1")
    table.add_row("4) SendRoutingInfoForGPRS", "CAT1")
    
    console.print(table)
    console.print("")
    console.print("or type back to go back to Attacks Menu".rjust(42))

    choice = input("\033[37m(\033[0m\033[2;31mLocationTracking\033[0m\033[37m)>\033[0m ")

    if choice == "0":
        ss7.tracking.sri()
    elif choice == "1":
        ss7.tracking.psi()
    elif choice == "2":
        ss7.tracking.srism()
    elif choice == "3":
        ss7.tracking.ati()
    elif choice == "4":
        ss7.tracking.srigprs()
    elif choice == "back":
        attacksMenu()
    else:
        console.print('\n[red][-]Error:[/red] Please Enter a Valid Choice (0 - 4)')
        time.sleep(1.5)
        LocationTracking()


def Interception():
    os.system('clear')

    console.print(Panel.fit("[bold red]Interception[/bold red]", border_style="red"))
    console.print(Panel.fit("[bold blue]Select a Message from the below[/bold blue]", border_style="blue"))
    
    # Create a table for interception options
    table = Table()
    table.add_column("Message", justify="right", style="cyan")
    table.add_column("Category", style="green")
    
    table.add_row("0) UpdateLocation-SMS Interception", "CAT3")
    table.add_row("1) Call Interception", "CAT3")
    table.add_row("2) SMS Interception", "CAT3")
    
    console.print(table)
    console.print("")
    console.print("or type back to go back to Attacks Menu".rjust(42))

    choice = input("\033[37m(\033[0m\033[2;31mInterception\033[0m\033[37m)>\033[0m ")

    if choice == "0":
        ss7.interception.ul()
    elif choice == "1":
        ss7.interception.call_interception()
    elif choice == "2":
        ss7.interception.sms_interception()
    elif choice == "back":
        attacksMenu()
    else:
        console.print('\n[red][-]Error:[/red] Please Enter a Valid Choice (0-2)')
        time.sleep(1.5)
        Interception()


def Fraud():
    os.system('clear')

    console.print(Panel.fit("[bold red]Fraud[/bold red]", border_style="red"))
    console.print(Panel.fit("[bold blue]Select a Message from the below[/bold blue]", border_style="blue"))
    
    # Create a table for fraud options
    table = Table()
    table.add_column("Message", justify="right", style="cyan")
    table.add_column("Category", style="green")
    
    table.add_row("0) SendIMSI", "CAT3")
    table.add_row("1) MTForwardSMS SMS Spoofing", "CAT3")
    table.add_row("2) Fake Roaming", "CAT3")
    
    console.print(table)
    console.print("")
    console.print("or type back to go back to Attacks Menu".rjust(42))

    choice = input("\033[37m(\033[0m\033[2;31mFraud\033[0m\033[37m)>\033[0m ")

    if choice == "0":
        ss7.fraud.simsi()
    elif choice == "1":
        ss7.fraud.mtsms()
    elif choice == "2":
        ss7.fraud.fake_roaming()
    elif choice == "back":
        attacksMenu()
    else:
        console.print('\n[red][-]Error:[/red] Please Enter a Valid Choice (0-2)')
        time.sleep(1.5)
        Fraud()


def DoS():
    os.system('clear')

    console.print(Panel.fit("[bold red]Denial of Service[/bold red]", border_style="red"))
    console.print(Panel.fit("[bold blue]Select a Message from the below[/bold blue]", border_style="blue"))
    
    # Create a table for DoS options
    table = Table()
    table.add_column("Message", justify="right", style="cyan")
    table.add_column("Category", style="green")
    
    table.add_row("0) PurgeMS-Subscriber DoS", "CAT3")
    
    console.print(table)
    console.print("")
    console.print("or type back to go back to Attacks Menu".rjust(42))

    choice = input("\033[37m(\033[0m\033[2;31mDoS\033[0m\033[37m)>\033[0m ")

    if choice == "0":
        ss7.dos.purge()
    elif choice == "back":
        attacksMenu()
    else:
        console.print('\n[red][-]Error:[/red] Please Enter a Valid Choice (0)')
        time.sleep(1.5)
        DoS()


def SS7Attacks():
    os.system('clear')

    console.print(Panel.fit("[bold red]SS7 Attacks[/bold red]", border_style="red"))
    console.print(Panel.fit("[bold blue]Select an SS7 Attack from the below[/bold blue]", border_style="blue"))
    
    # Create a table for SS7 attack options
    table = Table()
    table.add_column("Attack", justify="right", style="cyan")
    table.add_column("Description", style="green")
    
    table.add_row("0) AnyTimeInterrogation", "Location Tracking")
    table.add_row("1) ProvideSubscriberInfo", "User Data Disclosure")
    table.add_row("2) InsertSubscriberData", "Call Forwarding/Settings Change")
    table.add_row("3) SendRoutingInfoForSM + MT-FSM", "SMS Interception")
    
    console.print(table)
    console.print("")
    console.print("or type back to go back to Attacks Menu".rjust(42))

    choice = input("\033[37m(\033[0m\033[2;31mSS7Attacks\033[0m\033[37m)>\033[0m ")

    if choice == "0":
        ss7.tracking.ati()
    elif choice == "1":
        ss7.tracking.psi()
    elif choice == "2":
        ss7.interception.insert_subscriber_data()
    elif choice == "3":
        ss7.interception.sms_interception()
    elif choice == "back":
        attacksMenu()
    else:
        console.print('\n[red][-]Error:[/red] Please Enter a Valid Choice (0-3)')
        time.sleep(1.5)
        SS7Attacks()


def NetworkSupport():
    os.system('clear')

    console.print(Panel.fit("[bold red]Network Support[/bold red]", border_style="red"))
    console.print(Panel.fit("[bold blue]Select Network Type[/bold blue]", border_style="blue"))
    
    # Create a table for network options
    table = Table()
    table.add_column("Network", justify="right", style="cyan")
    table.add_column("Description", style="green")
    
    table.add_row("0) 2G", "GSM/GPRS Networks")
    table.add_row("1) 3G", "UMTS Networks")
    table.add_row("2) 4G", "LTE Networks")
    
    console.print(table)
    console.print("")
    console.print("or type back to go back to Attacks Menu".rjust(42))

    choice = input("\033[37m(\033[0m\033[2;31mNetworkSupport\033[0m\033[37m)>\033[0m ")

    if choice == "0" or choice == "1" or choice == "2":
        console.print("[green]Network selected successfully![/green]")
        time.sleep(1.5)
        attacksMenu()
    elif choice == "back":
        attacksMenu()
    else:
        console.print('\n[red][-]Error:[/red] Please Enter a Valid Choice (0-2)')
        time.sleep(1.5)
        NetworkSupport()


def attacksMenu():
    os.system('clear')

    console.print(Panel.fit("[bold blue]Choose From the Below Attack Categories[/bold blue]", border_style="blue"))
    
    # Create a table for attack categories
    table = Table()
    table.add_column("Category", justify="right", style="cyan")
    table.add_column("Description", style="green")
    
    table.add_row("0) Location Tracking", "Track target location")
    table.add_row("1) Call and SMS Interception", "Intercept communications")
    table.add_row("2) Fraud", "Perform fraudulent operations")
    table.add_row("3) DoS", "Denial of Service attacks")
    table.add_row("4) SS7 Attacks", "Additional SS7 exploitation")
    table.add_row("5) Network Support", "2G/3G/4G network selection")
    table.add_row("6) Real SS7 Attacks", "Execute real SS7 attacks")
    
    console.print(table)
    console.print("")
    console.print("or type back to return to the main menu".rjust(42))
    console.print("")

    choice = input("\033[37m(\033[0m\033[2;31mAttacks\033[0m\033[37m)>\033[0m ")

    if choice == "0":
        LocationTracking()
    elif choice == "1":
        Interception()
    elif choice == "2":
        Fraud()
    elif choice == "3":
        DoS()
    elif choice == "4":
        SS7Attacks()
    elif choice == "5":
        NetworkSupport()
    elif choice == "6":
        ss7.real_attacks.real_attacks_menu()
    elif choice == "back":
        sigploit.mainMenu()
    else:
        console.print('\n[red][-]Error:[/red] Please Enter a Valid Choice (0 - 6)')
        time.sleep(1.5)
        attacksMenu()
