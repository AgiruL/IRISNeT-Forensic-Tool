import random
import datetime
import tkinter as tk
from tkinter import messagebox
import sys

# --- CONFIGURATION ---
FILENAME = "evidence.log"
LINES_TO_GENERATE = 100

# --- DATA POOLS ---
users = ["admin", "root", "guest", "jdoe", "manager", "support"]
ips_internal = ["192.168.1.10", "192.168.1.12", "10.0.0.5", "172.16.0.22"]
ips_attacker = ["45.33.22.11", "103.20.15.1", "221.14.55.3", "89.40.2.14"]

messages_normal = [
    "System boot initiated successfully",
    "User {user} logged in from {ip}",
    "User {user} logged out",
    "Scheduled maintenance task started",
    "File accessed by {user}",
    "Network connection established"
]
messages_suspicious = [
    "Failed login attempt for user {user} from {ip}",
    "Invalid user access attempt from {ip}",
    "Root access requested by {ip}",
    "SSH protocol mismatch from {ip}",
    "Multiple authentication failures for {user}"
]

def generate_log():
    # Hide the main Tkinter window (we only want the popup)
    root = tk.Tk()
    root.withdraw()

    start_time = datetime.datetime.now() - datetime.timedelta(days=1)
    
    try:
        with open(FILENAME, "w") as f:
            current_time = start_time
            
            for _ in range(LINES_TO_GENERATE):
                # Advance time randomly (1s to 10mins)
                current_time += datetime.timedelta(seconds=random.randint(1, 600))
                timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")

                # 80% chance normal, 20% chance attack
                if random.random() < 0.8:
                    template = random.choice(messages_normal)
                    ip = random.choice(ips_internal)
                else:
                    template = random.choice(messages_suspicious)
                    ip = random.choice(ips_attacker)

                user = random.choice(users)
                message = template.format(user=user, ip=ip)
                f.write(f"{timestamp} {message}\n")
        
        # SUCCESS POPUP
        messagebox.showinfo("Attack Simulator", f"ATTACK SIMULATED!\n\nGenerated {LINES_TO_GENERATE} lines of forensic data.\nFile saved: {FILENAME}")
    
    except Exception as e:
        messagebox.showerror("Error", f"Could not generate logs:\n{e}")

if __name__ == "__main__":
    generate_log()