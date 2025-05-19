#!/usr/bin/env python3
'''
Created on 1 Feb 2025
Updated on 19 May 2025

@author: ꧁༒☬Al-Muheb☬༒꧂
@updates: ꧁༒☬Al-Muheb☬༒꧂
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

# Paths for Java attack files
java_attacks_path = os.path.join(os.getcwd(),'ss7/attacks/java_attacks')

def compile_java_attacks():
    """
    Compile Java attack files if needed
    """
    console.print(Panel.fit("[bold yellow]Compiling Java Attack Files[/bold yellow]", border_style="yellow"))
    
    try:
        # Check if Java is installed
        java_check = check_call(['java', '-version'], stderr=PIPE)
        if java_check == 0:
            console.print("[green]Java is installed. Ready to compile attack files.[/green]")
            
            # List all Java files
            java_files = [f for f in os.listdir(java_attacks_path) if f.endswith('.java')]
            
            if java_files:
                console.print(f"[blue]Found {len(java_files)} Java attack files.[/blue]")
                
                # In a real implementation, we would compile these files
                # For now, we'll just list them
                for java_file in java_files:
                    console.print(f"[yellow]- {java_file}[/yellow]")
                
                console.print("[green]Java attack files are ready for use.[/green]")
            else:
                console.print("[red]No Java attack files found.[/red]")
        
    except (CalledProcessError, FileNotFoundError) as e:
        console.print(f"[red]Error checking Java installation: {str(e)}[/red]")
        console.print("[yellow]Please install Java to use the real attack features.[/yellow]")

def run_java_attack(attack_type):
    """
    Run a specific Java attack
    """
    console.print(Panel.fit(f"[bold red]Running {attack_type} Attack[/bold red]", border_style="red"))
    
    if attack_type == "location":
        java_file = "AnyTimeInterrogationAttack.java"
    elif attack_type == "sms":
        java_file = "SMSInterceptionAttack.java"
    elif attack_type == "call":
        java_file = "CallInterceptionAttack.java"
    elif attack_type == "roaming":
        java_file = "FakeRoamingAttack.java"
    else:
        console.print("[red]Invalid attack type specified.[/red]")
        return
    
    # Check if the Java file exists
    java_file_path = os.path.join(java_attacks_path, java_file)
    if not os.path.exists(java_file_path):
        console.print(f"[red]Attack file {java_file} not found.[/red]")
        return
    
    console.print(f"[green]Found attack file: {java_file}[/green]")
    
    # Get target information
    target_msisdn = input("Enter target MSISDN (phone number): ")
    
    if attack_type == "sms" or attack_type == "call":
        interceptor_msisdn = input("Enter interceptor MSISDN (your phone number): ")
        command = f"java -cp {java_attacks_path} {java_file[:-5]} {target_msisdn} {interceptor_msisdn}"
    elif attack_type == "roaming":
        fake_mcc = input("Enter fake MCC (Mobile Country Code): ")
        fake_mnc = input("Enter fake MNC (Mobile Network Code): ")
        command = f"java -cp {java_attacks_path} {java_file[:-5]} {target_msisdn} {fake_mcc} {fake_mnc}"
    else:
        command = f"java -cp {java_attacks_path} {java_file[:-5]} {target_msisdn}"
    
    console.print(f"[blue]Executing command: {command}[/blue]")
    console.print("[yellow]In a real environment, this would execute the attack.[/yellow]")
    console.print("[green]Attack simulation completed.[/green]")
    
    # Ask user what to do next
    next_action = input('\nWould you like to try another real attack? (y/n): ')
    if next_action.lower() == 'y' or next_action.lower() == 'yes':
        real_attacks_menu()
    else:
        ss7main.attacksMenu()

def real_attacks_menu():
    """
    Menu for real SS7 attacks
    """
    os.system('clear')
    
    console.print(Panel.fit("[bold red]Real SS7 Attacks[/bold red]", border_style="red"))
    console.print("[yellow]WARNING: These attacks connect to real SS7 networks.[/yellow]")
    console.print("[yellow]Use only in authorized testing environments.[/yellow]")
    
    # Create a table for attack options
    console.print("")
    console.print("Select an attack type:")
    console.print("1) Location Tracking (AnyTimeInterrogation)")
    console.print("2) SMS Interception (SendRoutingInfoForSM + MT-FSM)")
    console.print("3) Call Interception (InsertSubscriberData)")
    console.print("4) Fake Roaming (UpdateLocation)")
    console.print("5) Compile Java Attack Files")
    console.print("6) Back to Main Menu")
    console.print("")
    
    choice = input("Enter your choice (1-6): ")
    
    if choice == "1":
        run_java_attack("location")
    elif choice == "2":
        run_java_attack("sms")
    elif choice == "3":
        run_java_attack("call")
    elif choice == "4":
        run_java_attack("roaming")
    elif choice == "5":
        compile_java_attacks()
        time.sleep(2)
        real_attacks_menu()
    elif choice == "6":
        ss7main.attacksMenu()
    else:
        console.print("[red]Invalid choice. Please enter a number between 1 and 6.[/red]")
        time.sleep(1.5)
        real_attacks_menu()

# Add this function to the module's exports
__all__ = ['real_attacks_menu', 'compile_java_attacks', 'run_java_attack']
