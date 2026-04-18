import customtkinter as ctk
import subprocess, sys
from database import get_logs, init_db
from analytics import show_chart

init_db()

ctk.set_appearance_mode("dark")

app = ctk.CTk()
app.geometry("1000x600")
app.title("ASIS AI")

tabs = ctk.CTkTabview(app)
tabs.pack(fill="both", expand=True)

dash = tabs.add("Dashboard")
logs_tab = tabs.add("Logs")

# -------- DASHBOARD --------
def start():
    subprocess.Popen([sys.executable,"main.py"])

ctk.CTkButton(dash, text="Start System",
              command=start).pack(pady=20)

ctk.CTkButton(dash, text="Show Analytics",
              command=show_chart).pack(pady=10)

# -------- LOGS --------
box = ctk.CTkTextbox(logs_tab)
box.pack(fill="both", expand=True)

def update_logs():
    box.delete("1.0","end")
    for t,g in get_logs():
        box.insert("end",f"{t} - {g}\n")
    app.after(2000, update_logs)

update_logs()

app.mainloop()