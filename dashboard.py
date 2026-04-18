import customtkinter as ctk
import subprocess, sys

ctk.set_appearance_mode("dark")

app = ctk.CTk()
app.geometry("900x600")
app.title("ASIS AI SYSTEM")

status = ctk.StringVar(value="STOPPED")

def start():
    status.set("RUNNING")
    subprocess.Popen([sys.executable,"main.py"])

def stop():
    status.set("STOPPED")

ctk.CTkLabel(app, text="ASIS AI SYSTEM",
             font=("Arial",28)).pack(pady=20)

ctk.CTkLabel(app, textvariable=status,
             font=("Arial",16)).pack(pady=10)

ctk.CTkButton(app, text="Start System",
              command=start).pack(pady=10)

ctk.CTkButton(app, text="Stop System",
              fg_color="orange",
              command=stop).pack(pady=10)

ctk.CTkLabel(app, text="Voice: Jarvis / Click / Open Chrome").pack(pady=20)

app.mainloop()