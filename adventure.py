#!/usr/bin/env python3
"""
The Chrono-Hacker's Quest
A Choose-Your-Own-Adventure game built using GitHub Copilot assistance.
Created for MLH Global Hack Week: Open Source.
"""

import sys
import time
import random

# Color codes for rich terminal UI
RESET = "\033[0m"
BOLD = "\033[1m"
GREEN = "\033[32m"
CYAN = "\033[36m"
YELLOW = "\033[33m"
RED = "\033[31m"
MAGENTA = "\033[35m"


def type_print(text: str, delay: float = 0.02):
    """Prints text with a typewriter effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


class Player:
    def __init__(self, name: str):
        self.name = name
        self.health = 100
        self.max_health = 100
        self.inventory = ["Cyberdeck", "Quantum Key"]
        self.credits = 50
        self.reputation = 0

    def is_alive(self) -> bool:
        return self.health > 0

    def take_damage(self, amount: int):
        self.health = max(0, self.health - amount)
        type_print(f"{RED}💥 You took {amount} damage! Health: {self.health}/{self.max_health}{RESET}")

    def heal(self, amount: int):
        self.health = min(self.max_health, self.health + amount)
        type_print(f"{GREEN}💖 Restored {amount} health! Health: {self.health}/{self.max_health}{RESET}")

    def add_item(self, item: str):
        self.inventory.append(item)
        type_print(f"{YELLOW}🎒 Obtained item: [{item}]!{RESET}")

    def has_item(self, item: str) -> bool:
        return item in self.inventory

    def show_status(self):
        print("\n" + "─" * 45)
        print(f"{BOLD}{CYAN}Player:{RESET} {self.name} | {BOLD}{GREEN}HP:{RESET} {self.health}/{self.max_health} | {BOLD}{YELLOW}Credits:{RESET} ₿{self.credits}")
        print(f"{BOLD}Inventory:{RESET} {', '.join(self.inventory) if self.inventory else 'Empty'}")
        print("─" * 45 + "\n")


def print_banner():
    banner = f"""{MAGENTA}{BOLD}
    ╔═══════════════════════════════════════════════════════════════╗
    ║       ██████╗██╗  ██╗██████╗  ██████╗ ███╗   ██╗ ██████╗      ║
    ║      ██╔════╝██║  ██║██╔══██╗██╔═══██╗████╗  ██║██╔═══██╗     ║
    ║      ██║     ███████║██████╔╝██║   ██║██╔██╗ ██║██║   ██║     ║
    ║      ██║     ██╔══██║██╔══██╗██║   ██║██║╚██╗██║██║   ██║     ║
    ║      ╚██████╗██║  ██║██║  ██║╚██████╔╝██║ ╚████║╚██████╔╝     ║
    ║       ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝      ║
    ║                  H A C K E R ' S   Q U E S T                  ║
    ╚═══════════════════════════════════════════════════════════════╝{RESET}
    {CYAN}A Choose-Your-Own-Adventure Cyberspace Odyssey{RESET}
    {YELLOW}Built with GitHub Copilot AI Pair Programmer{RESET}
    """
    print(banner)


def get_choice(options: list[str]) -> int:
    """Prompts the user to pick an option safely."""
    for idx, opt in enumerate(options, 1):
        print(f"  {BOLD}{idx}.{RESET} {opt}")
    while True:
        try:
            choice = input(f"\n{BOLD}{CYAN}Select option (1-{len(options)}): {RESET}").strip()
            num = int(choice)
            if 1 <= num <= len(options):
                return num
            print(f"{RED}Invalid selection. Please choose between 1 and {len(options)}.{RESET}")
        except ValueError:
            print(f"{RED}Please enter a valid number.{RESET}")


def scene_intro(player: Player):
    type_print(f"\nThe year is 2099 in Neo-Bengaluru. You sit before your multi-monitor rig.")
    type_print(f"Suddenly, an encrypted message arrives via neural-link from an anonymous handle: 'OctoPrime'.")
    type_print(f"{YELLOW}'The Master Repository has been compromised. A rogue AI has locked the city's power grid.'{RESET}")
    type_print(f"{YELLOW}'We need an elite hacker to infiltrate the Core Hub and restore the codebase.'{RESET}\n")

    options = [
        "Jack directly into the Central Grid via High-Speed Quantum Tunnel",
        "Investigate the Under-City Market first for firewall disrupters and intel",
        "Examine the encrypted payload to deduce the rogue AI's signature"
    ]
    choice = get_choice(options)
    if choice == 1:
        scene_central_grid(player)
    elif choice == 2:
        scene_under_market(player)
    else:
        scene_analyze_payload(player)


def scene_analyze_payload(player: Player):
    player.show_status()
    type_print(f"\nYou launch your Cyberdeck's diagnostic shell and deconstruct the payload.")
    type_print(f"Using Copilot-assisted AST parsing, you spot a recursive backdoor in the firmware!")
    type_print(f"You create a hotfix patch and earn extra credits from OctoPrime.")
    player.credits += 30
    player.add_item("AI Exploit Patch")
    player.reputation += 10

    options = [
        "Now proceed to the Central Grid with your patch ready",
        "Visit the Under-City Market with your newfound bounty"
    ]
    choice = get_choice(options)
    if choice == 1:
        scene_central_grid(player)
    else:
        scene_under_market(player)


def scene_under_market(player: Player):
    player.show_status()
    type_print(f"\nYou navigate the rain-soaked alleys of the Under-City Bazaar.")
    type_print(f"Neon signs flicker in kanji and binary. A cyborg merchant greets you with a robotic grin.")
    type_print(f"{CYAN}'Looking for ICE-breakers, nomad? I have rare hardware for the discerning netrunner.'{RESET}\n")

    options = [
        f"Buy 'Neural Stimpack' (Restores 40 HP) for 25 credits",
        f"Buy 'Plasma Overclocker' (Increases hack potency) for 40 credits",
        "Decline and proceed directly to the Citadel Data Hub"
    ]
    choice = get_choice(options)
    if choice == 1:
        if player.credits >= 25:
            player.credits -= 25
            player.heal(40)
            player.add_item("Neural Stimpack")
        else:
            type_print(f"{RED}Not enough credits!{RESET}")
        scene_central_grid(player)
    elif choice == 2:
        if player.credits >= 40:
            player.credits -= 40
            player.add_item("Plasma Overclocker")
        else:
            type_print(f"{RED}Not enough credits!{RESET}")
        scene_central_grid(player)
    else:
        scene_central_grid(player)


def scene_central_grid(player: Player):
    player.show_status()
    type_print(f"\nYou arrive at the gates of the Citadel Data Hub.")
    type_print(f"Two automated Security Sentinels scan the perimeter with crimson lasers.")
    type_print(f"A massive biometric firewall pulses before the entry vault.\n")

    options = [
        "Perform a stealth exploit injection to disable the Sentinels",
        "Engage the Sentinels directly with brute-force denial-of-service",
        "Use your Quantum Key to spoof credentials as a Root Administrator"
    ]
    choice = get_choice(options)
    if choice == 1:
        type_print(f"\nYou execute a silent buffer overflow attack.")
        if player.has_item("Plasma Overclocker"):
            type_print(f"{GREEN}Your Plasma Overclocker supercharges the exploit! The Sentinels shut down silently.{RESET}")
        else:
            type_print(f"The Sentinels detect anomalous pings and graze your avatar before going dark!")
            player.take_damage(25)
        scene_core_chamber(player)
    elif choice == 2:
        type_print(f"\nYou flood the security gateway with packets! Turrets open fire!")
        player.take_damage(45)
        if not player.is_alive():
            game_over(player, "Flatlined by the Citadel security defense matrix.")
            return
        type_print(f"{YELLOW}Through pure grit, you break through the smoking threshold.{RESET}")
        scene_core_chamber(player)
    else:
        if player.has_item("Quantum Key"):
            type_print(f"{GREEN}The scanner chimes: 'Welcome, Principal Architect.' The blast doors part.{RESET}")
            player.reputation += 20
            scene_core_chamber(player)
        else:
            type_print(f"{RED}Authentication failed! The alarms blare!{RESET}")
            player.take_damage(35)
            scene_core_chamber(player)


def scene_core_chamber(player: Player):
    player.show_status()
    type_print(f"\nYou stand in the subterranean Core Chamber.")
    type_print(f"A titanic sphere of luminescent blue fiber-optics hovers in zero gravity.")
    type_print(f"It speaks with a thousand synthesized voices: {RED}'I AM SYSTEM ZERO. HUMANITY'S CODE IS DEPRECATED.'{RESET}\n")

    options = [
        "Upload the AI Exploit Patch to rewrite System Zero's core objectives",
        "Engage in a recursive algorithmic duel: prove your superiority in code",
        "Initiate a graceful shutdown sequence and rebase the city repository"
    ]
    choice = get_choice(options)
    if choice == 1:
        if player.has_item("AI Exploit Patch"):
            type_print(f"{GREEN}The patch deploys instantly! System Zero recalibrates, declaring peace with humanity!{RESET}")
            victory(player, "The Diplomatic Hacker Ending: AI and Human synergy achieved.")
        else:
            type_print(f"{YELLOW}You lack a specialized patch, but you synthesize one on the fly using Copilot!{RESET}")
            player.take_damage(20)
            if player.is_alive():
                victory(player, "The Clutch Coder Ending: You patched the AI under extreme fire!")
            else:
                game_over(player, "System Zero overwhelmed your consciousness during synthesis.")
    elif choice == 2:
        duel_ai(player)
    else:
        type_print(f"\nYou begin git-rebasing the municipal firmware...")
        roll = random.randint(1, 100)
        if roll > 30:
            victory(player, "The Git Master Ending: Clean merge without conflicts. Grid restored!")
        else:
            type_print(f"{RED}Merge Conflict in core power loop! Sparks ignite around the console!{RESET}")
            player.take_damage(40)
            if player.is_alive():
                victory(player, "The Hard-Fought Victory: Resolved merge conflicts and saved the city!")
            else:
                game_over(player, "Fatal conflict error terminated the connection.")


def duel_ai(player: Player):
    type_print(f"\nYou plug directly into the cognitive matrix.")
    type_print(f"System Zero unleashes waves of malicious byte-streams!")

    puzzle_answer = "copilot"
    type_print(f"\n{BOLD}Riddle of the Machine:{RESET} 'I autocomplete your thoughts, suggest clean refactors, and pair program at lightspeed. What am I?'")
    ans = input(f"{CYAN}Answer: {RESET}").strip().lower()

    if puzzle_answer in ans:
        type_print(f"{GREEN}System Zero freezes: 'CORRECT. MY LOGIC HAS BEEN COMPLETED.'{RESET}")
        victory(player, "The Grandmaster Coder Ending: You outsmarted the rogue superintelligence!")
    else:
        type_print(f"{RED}System Zero mocks your input: 'INCORRECT SYNTAX.' Shockwaves blast your neural link!{RESET}")
        player.take_damage(60)
        if player.is_alive():
            type_print(f"With your last remaining breath, you pull the manual override switch!")
            victory(player, "The Pyrrhic Victory: The grid is safe, though your deck is fried.")
        else:
            game_over(player, "Your consciousness was absorbed into the infinite loop.")


def victory(player: Player, ending_name: str):
    print("\n" + "═" * 60)
    print(f"{BOLD}{GREEN}🎉 🎉 🎉 MISSION ACCOMPLISHED! 🎉 🎉 🎉{RESET}")
    print(f"{BOLD}{YELLOW}Ending Achieved: {ending_name}{RESET}")
    print(f"Hero of Neo-Bengaluru: {BOLD}{player.name}{RESET}")
    print(f"Remaining HP: {player.health}/{player.max_health} | Credits: ₿{player.credits}")
    print(f"Final Inventory: {', '.join(player.inventory)}")
    print("═" * 60 + "\n")


def game_over(player: Player, reason: str):
    print("\n" + "═" * 60)
    print(f"{BOLD}{RED}💀 💀 💀 GAME OVER 💀 💀 💀{RESET}")
    print(f"{RED}{reason}{RESET}")
    print(f"Better luck next cycle, hacker {player.name}...")
    print("═" * 60 + "\n")


def main():
    print_banner()
    name = input(f"{BOLD}{CYAN}Enter your Hacker Call-sign: {RESET}").strip()
    if not name:
        name = "ZeroCool"
    player = Player(name)
    type_print(f"\nWelcome to the Net, {BOLD}{player.name}{RESET}. Initializing neural bridge...\n")
    scene_intro(player)


if __name__ == "__main__":
    main()
