import os
import time
import random

GREEN = "\033[32m"
RED = "\033[31m"
YELLOW = "\033[33m"
RESET = "\033[0m"

# ---------------- SAFE SLEEP ----------------
def safe_sleep(t):
    try:
        time.sleep(float(t))
    except:
        time.sleep(0.03)

# ---------------- CLEAR ----------------
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# ---------------- GLITCH EFFECT ----------------
def glitch_text(text, times=3):
    for _ in range(times):
        clear()
        distorted = "".join(
            random.choice([c, "█", "@", "#", "%", text.lower()[i % len(text)]])
            for i, c in enumerate(text)
        )
        print(GREEN + distorted + RESET)
        safe_sleep(0.08)

# ---------------- TYPE EFFECT ----------------
def type_text(text, delay=0.03, color=GREEN):
    try:
        delay = float(delay)
    except:
        delay = 0.03

    for c in text:
        print(color + c + RESET, end="", flush=True)
        safe_sleep(delay)
    print()

# ---------------- LOGO ----------------
def logo():
    print(GREEN + r"""
 ████████╗██████╗  ██████╗ ██████╗ 
 ╚══██╔══╝██╔══██╗██╔═══██╗██╔══██╗
    ██║   ██████╔╝██║   ██║██████╔╝
    ██║   ██╔══██╗██║   ██║██╔═══╝ 
    ██║   ██║  ██║╚██████╔╝██║     
    ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝     
""" + RESET)

# ---------------- LOGS ----------------
def logs():
    messages = [
        "[SYSTEM] boot sequence initiated...",
        "[OK] memory scan complete",
        "[WARNING] unknown process detected",
        "[ACCESS] terminal link unstable",
        "[ERROR] node corruption found",
        "[TRACE] user activity recorded..."
    ]

    for _ in range(6):
        print(GREEN + random.choice(messages) + RESET)
        safe_sleep(0.4)

# ---------------- MENU ----------------
def menu():
    print(GREEN + "\n[1] START SYSTEM" + RESET)
    print(GREEN + "[2] SHUTDOWN" + RESET)

# ---------------- SCENE ----------------
def connect_scene():
    clear()
    type_text("CONNECTING TO NODE...")
    safe_sleep(1)
    type_text("WARNING: UNKNOWN ENTITY DETECTED", RED)
    safe_sleep(2)

# ---------------- MAIN ----------------
def main():
    clear()

    glitch_text("INITIALIZING TERMINAL...")
    safe_sleep(1)

    clear()
    logo()
    safe_sleep(1)

    logs()
    safe_sleep(1)

    while True:
        clear()
        logo()
        menu()

        choice = input(GREEN + "\n> " + RESET).strip()

        if choice == "1":
            connect_scene()

        elif choice == "2":
            type_text("TERMINATING SESSION...", YELLOW)
            safe_sleep(1)
            break

        else:
            type_text("INVALID INPUT", RED)
            safe_sleep(1)

if __name__ == "__main__":
    main()