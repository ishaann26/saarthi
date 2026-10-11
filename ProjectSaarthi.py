import tkinter as tk
from tkinter import messagebox
import json
import os
import time
import threading

# ---------------- GLOBAL DATA ----------------
DATA_FILE = "saarthi_data.json"
current_user = None

FONT_TITLE = ("Segoe UI", 18, "bold")
FONT_HEAD = ("Segoe UI", 15, "bold")
FONT_TEXT = ("Segoe UI", 13)
FONT_BTN = ("Segoe UI", 13, "bold")

root = tk.Tk()
root.title("SAARTHI")
root.geometry("650x700")
root.resizable(False, False)

# ---------------- DATA FUNCTIONS ----------------
def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

data = load_data()

# ---------------- COMMON ----------------
def clear():
    for w in root.winfo_children():
        w.destroy()

def back_to_dashboard():
    dashboard()

# ---------------- HOME ----------------
def home():
    clear()
    tk.Label(root, text="Welcome to SAARTHI", font=FONT_TITLE).pack(pady=40)
    tk.Button(root, text="Login", font=FONT_BTN, width=30, command=login).pack(pady=10)
    tk.Button(root, text="New User", font=FONT_BTN, width=30, command=register).pack(pady=10)

# ---------------- REGISTER ----------------
def register():
    clear()
    tk.Label(root, text="Create Account", font=FONT_HEAD).pack(pady=20)

    phone = tk.Entry(root, font=FONT_TEXT)
    pwd = tk.Entry(root, font=FONT_TEXT, show="*")

    for lbl, ent in [("Phone Number", phone), ("Password", pwd)]:
        tk.Label(root, text=lbl, font=FONT_TEXT).pack()
        ent.pack(pady=5)

    def save():
        global current_user
        if phone.get() in data:
            messagebox.showerror("Error", "User already exists")
            return

        data[phone.get()] = {
            "password": pwd.get(),
            "profile": {},
            "attendance": {},
            "study_plans": [],
            "completed": [],
            "marks": {}
        }
        save_data(data)
        current_user = phone.get()
        profile()

    tk.Button(root, text="Register", font=FONT_BTN, command=save).pack(pady=15)
    tk.Button(root, text="Back", font=FONT_BTN, command=home).pack()

# ---------------- LOGIN ----------------
def login():
    clear()
    tk.Label(root, text="Login", font=FONT_HEAD).pack(pady=20)

    phone = tk.Entry(root, font=FONT_TEXT)
    pwd = tk.Entry(root, font=FONT_TEXT, show="*")

    for lbl, ent in [("Phone Number", phone), ("Password", pwd)]:
        tk.Label(root, text=lbl, font=FONT_TEXT).pack()
        ent.pack(pady=5)

    def check():
        global current_user
        if phone.get() in data and data[phone.get()]["password"] == pwd.get():
            current_user = phone.get()
            dashboard()
        else:
            messagebox.showerror("Error", "Invalid login")

    tk.Button(root, text="Login", font=FONT_BTN, command=check).pack(pady=15)
    tk.Button(root, text="Back", font=FONT_BTN, command=home).pack()

# ---------------- PROFILE ----------------
def profile():
    clear()
    tk.Label(root, text="Profile Details", font=FONT_HEAD).pack(pady=20)

    name = tk.Entry(root, font=FONT_TEXT)
    clas = tk.Entry(root, font=FONT_TEXT)
    stream = tk.Entry(root, font=FONT_TEXT)

    for lbl, ent in [("Name", name), ("Class", clas), ("Stream", stream)]:
        tk.Label(root, text=lbl, font=FONT_TEXT).pack()
        ent.pack(pady=5)

    def save():
        data[current_user]["profile"] = {
            "name": name.get(),
            "class": clas.get(),
            "stream": stream.get()
        }
        save_data(data)
        dashboard()

    tk.Button(root, text="Save Profile", font=FONT_BTN, command=save).pack(pady=20)

# ---------------- DASHBOARD ----------------
def dashboard():
    clear()
    tk.Label(root, text="Dashboard", font=FONT_HEAD).pack(pady=25)

    buttons = [
        ("Create Self Study Plan", study_plan),
        ("Completed Chapters", completed_chapters),
        ("Attendance %", attendance),
        ("Semester Marks Entry", marks_entry),
        ("Progress Comparison", progress),
        ("Pomodoro Mode", pomodoro)
    ]

    for txt, cmd in buttons:
        tk.Button(root, text=txt, font=FONT_BTN, width=38, command=cmd).pack(pady=7)

# ---------------- SELF STUDY ----------------
def study_plan():
    clear()
    tk.Label(root, text="Self Study Plan", font=FONT_HEAD).pack(pady=20)

    chap = tk.Entry(root, font=FONT_TEXT)
    topic = tk.Entry(root, font=FONT_TEXT)
    hours = tk.Entry(root, font=FONT_TEXT)

    for lbl, ent in [("Chapter", chap), ("Topic", topic), ("Hours", hours)]:
        tk.Label(root, text=lbl, font=FONT_TEXT).pack()
        ent.pack(pady=5)

    def save():
        plan = f"{chap.get()} | {topic.get()} | {hours.get()} hrs"
        data[current_user]["study_plans"].append(plan)
        save_data(data)
        messagebox.showinfo("Saved", "Study plan added")

    tk.Button(root, text="Save Plan", font=FONT_BTN, command=save).pack(pady=15)
    tk.Button(root, text="Back", font=FONT_BTN, command=back_to_dashboard).pack()

# ---------------- COMPLETED ----------------
def completed_chapters():
    clear()
    tk.Label(root, text="Completed Chapters", font=FONT_HEAD).pack(pady=20)

    for plan in data[current_user]["study_plans"]:
        var = tk.BooleanVar()

        def toggle(p=plan, v=var):
            if v.get():
                if p not in data[current_user]["completed"]:
                    data[current_user]["completed"].append(p)
            else:
                if p in data[current_user]["completed"]:
                    data[current_user]["completed"].remove(p)
            save_data(data)

        cb = tk.Checkbutton(root, text=plan, font=FONT_TEXT, variable=var, command=toggle)
        if plan in data[current_user]["completed"]:
            var.set(True)
        cb.pack(anchor="w", padx=40)

    tk.Button(root, text="Back", font=FONT_BTN, command=back_to_dashboard).pack(pady=15)

# ---------------- ATTENDANCE ----------------
def attendance():
    clear()
    tk.Label(root, text="Attendance Calculator", font=FONT_HEAD).pack(pady=20)

    total = tk.Entry(root, font=FONT_TEXT)
    present = tk.Entry(root, font=FONT_TEXT)

    for lbl, ent in [("Total Working Days", total), ("Days Present", present)]:
        tk.Label(root, text=lbl, font=FONT_TEXT).pack()
        ent.pack(pady=5)

    def calc():
        try:
            t, p = int(total.get()), int(present.get())
            percent = (p / t) * 100
            messagebox.showinfo("Attendance", f"{percent:.2f}%")
        except:
            messagebox.showerror("Error", "Invalid input")

    tk.Button(root, text="Calculate", font=FONT_BTN, command=calc).pack(pady=15)
    tk.Button(root, text="Back", font=FONT_BTN, command=back_to_dashboard).pack()

# ---------------- MARKS ----------------
def marks_entry():
    clear()
    tk.Label(root, text="Semester Marks Entry", font=FONT_HEAD).pack(pady=20)

    sem = tk.Entry(root, font=FONT_TEXT)
    marks = tk.Entry(root, font=FONT_TEXT)

    for lbl, ent in [("Semester", sem), ("Average Marks", marks)]:
        tk.Label(root, text=lbl, font=FONT_TEXT).pack()
        ent.pack(pady=5)

    def save():
        data[current_user]["marks"][sem.get()] = float(marks.get())
        save_data(data)
        messagebox.showinfo("Saved", "Marks saved")

    tk.Button(root, text="Save Marks", font=FONT_BTN, command=save).pack(pady=15)
    tk.Button(root, text="Back", font=FONT_BTN, command=back_to_dashboard).pack()

# ---------------- PROGRESS ----------------
def progress():
    clear()
    tk.Label(root, text="Progress Comparison", font=FONT_HEAD).pack(pady=20)

    prev = None
    for sem, m in data[current_user]["marks"].items():
        text = f"{sem}: {m}"
        if prev is not None:
            text += " (Improved)" if m > prev else " (Declined)"
        tk.Label(root, text=text, font=FONT_TEXT).pack()
        prev = m

    tk.Button(root, text="Back", font=FONT_BTN, command=back_to_dashboard).pack(pady=15)

# ---------------- POMODORO ----------------
def pomodoro():
    clear()
    tk.Label(root, text="Pomodoro – 45 Minutes", font=FONT_HEAD).pack(pady=25)

    timer = tk.Label(root, text="45:00", font=("Segoe UI", 30, "bold"))
    timer.pack(pady=15)

    def start():
        def run():
            t = 45 * 60
            while t >= 0:
                m, s = divmod(t, 60)
                timer.config(text=f"{m:02d}:{s:02d}")
                time.sleep(1)
                t -= 1
            messagebox.showinfo("Done", "Session Complete!")

        threading.Thread(target=run, daemon=True).start()

    tk.Button(root, text="Start", font=FONT_BTN, command=start).pack(pady=10)
    tk.Button(root, text="Back", font=FONT_BTN, command=back_to_dashboard).pack()

# ---------------- START APP ----------------
home()
root.mainloop()
