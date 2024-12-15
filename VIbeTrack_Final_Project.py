import os
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import json

DATA_FILE = 'users_data.json'  # Define the path to the data file

def load_users_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return {}

def save_users_data():
    with open(DATA_FILE, 'w') as file:
        json.dump(users_data, file, indent=4)

users_data = load_users_data()

def predict_mood(sleep_hours, exercise_minutes, meditation_minutes, exercise_intensity):
    if sleep_hours < 6 or exercise_minutes < 20:
        return "Stressed"
    elif sleep_hours >= 7 and exercise_minutes >= 30:
        return "Happy"
    elif meditation_minutes >= 10:
        return "Calm"
    elif exercise_intensity == "High" and exercise_minutes >= 45:
        return "Energized"
    else:
        return "Neutral"

def register_user():
    username = username_entry.get()
    password = password_entry.get()

    if not username or not password:
        messagebox.showerror("Error", "Username and password are required!")
        return
    
    if len(password) < 6:
        messagebox.showerror("Error", "Password must be at least 6 characters!")
        return
    
    if username in users_data:
        messagebox.showerror("Error", "Username already exists!")
        return

    users_data[username] = {"password": password, "data": {}}
    save_users_data()
    messagebox.showinfo("Success", "User registered successfully!")
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

def login_user():
    username = username_entry.get()
    password = password_entry.get()

    if not username or not password:
        messagebox.showerror("Error", "Please enter both username and password!")
        return

    if username not in users_data or users_data[username]["password"] != password:
        messagebox.showerror("Error", "Invalid username or password!")
        return

    messagebox.showinfo("Success", "Login successful!")
    open_data_input_window(username)

    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

def open_data_input_window(username):
    data_input_window = tk.Toplevel()
    data_input_window.title(f"{username} - Enter Your Daily Data")
    data_input_window.geometry("400x400")
    data_input_window.config(bg="#f4e1d2")

    sleep_label = tk.Label(data_input_window, text="Sleep hours (0-24):", bg="#f4e1d2", font=('Helvetica', 12))
    sleep_label.pack(pady=5)
    sleep_entry = tk.Entry(data_input_window)
    sleep_entry.pack(pady=5)

    exercise_type_label = tk.Label(data_input_window, text="Exercise Type:", bg="#f4e1d2", font=('Helvetica', 12))
    exercise_type_label.pack(pady=5)
    exercise_type_options = ["Aerobic", "Strength Training", "Mind-Body", "HIIT", "Stretching"]
    exercise_type_combobox = ttk.Combobox(data_input_window, values=exercise_type_options, state="readonly")
    exercise_type_combobox.pack(pady=5)
    
    exercise_minutes_label = tk.Label(data_input_window, text="Exercise minutes:", bg="#f4e1d2", font=('Helvetica', 12))
    exercise_minutes_label.pack(pady=5)
    exercise_minutes_entry = tk.Entry(data_input_window)
    exercise_minutes_entry.pack(pady=5)

    exercise_intensity_label = tk.Label(data_input_window, text="Exercise Intensity:", bg="#f4e1d2", font=('Helvetica', 12))
    exercise_intensity_label.pack(pady=5)
    exercise_intensity_options = ["Low", "Moderate", "High"]
    exercise_intensity_combobox = ttk.Combobox(data_input_window, values=exercise_intensity_options, state="readonly")
    exercise_intensity_combobox.pack(pady=5)

    meditation_label = tk.Label(data_input_window, text="Meditation minutes:", bg="#f4e1d2", font=('Helvetica', 12))
    meditation_label.pack(pady=5)
    meditation_entry = tk.Entry(data_input_window)
    meditation_entry.pack(pady=5)

    def submit_data():
        try:
            sleep_hours = int(sleep_entry.get())
            exercise_minutes = int(exercise_minutes_entry.get())
            meditation_minutes = int(meditation_entry.get())
            exercise_type = exercise_type_combobox.get()
            exercise_intensity = exercise_intensity_combobox.get()

            if sleep_hours < 0 or sleep_hours > 24 or exercise_minutes < 0 or meditation_minutes < 0:
                raise ValueError("Invalid data range.")
            
            if exercise_intensity not in ["Low", "Moderate", "High"]:
                raise ValueError("Exercise intensity must be Low, Moderate, or High.")

            if exercise_type not in ["Aerobic", "Strength Training", "Mind-Body", "HIIT", "Stretching"]:
                raise ValueError("Exercise type must be one of: Aerobic, Strength, Mind-Body, HIIT, Stretching.")

            users_data[username]["data"] = {
                "sleep_hours": sleep_hours,
                "exercise_minutes": exercise_minutes,
                "exercise_type": exercise_type,
                "exercise_intensity": exercise_intensity,
                "meditation_minutes": meditation_minutes
            }

            save_users_data()

            mood = predict_mood(sleep_hours, exercise_minutes, meditation_minutes, exercise_intensity)

            messagebox.showinfo("Mood Prediction", f"Your predicted mood: {mood}")
            data_input_window.destroy()

        except ValueError as e:
            messagebox.showerror("Error", f"Error: {str(e)}")

    submit_button = tk.Button(data_input_window, text="Submit", command=submit_data, bg="#FF69B4", fg="white", font=('Helvetica', 12, 'bold'))
    submit_button.pack(pady=20)

def open_welcome_window():
    welcome_window = tk.Tk()
    welcome_window.title("VibeTrack - Mood Classification")
    welcome_window.geometry("400x300")
    welcome_window.config(bg="#f4e1d2")

    welcome_label = tk.Label(welcome_window, text="Welcome to VibeTrack!", font=('Helvetica', 16), bg="#f4e1d2", fg="#FF69B4")
    welcome_label.pack(pady=20)

    start_button = tk.Button(welcome_window, text="Start", command=open_user_info_window, bg="#FF69B4", fg="white", font=('Helvetica', 12, 'bold'))
    start_button.pack(pady=20)

    welcome_window.mainloop()

def open_user_info_window():
    user_info_window = tk.Tk()
    user_info_window.title("VibeTrack - Login / Register")
    user_info_window.geometry("400x300")
    user_info_window.config(bg="#f4e1d2")

    username_label = tk.Label(user_info_window, text="Username:", bg="#f4e1d2", font=('Helvetica', 12))
    username_label.pack(pady=10)
    global username_entry
    username_entry = tk.Entry(user_info_window)
    username_entry.pack(pady=5)

    password_label = tk.Label(user_info_window, text="Password:", bg="#f4e1d2", font=('Helvetica', 12))
    password_label.pack(pady=10)
    global password_entry
    password_entry = tk.Entry(user_info_window, show="*")
    password_entry.pack(pady=5)

    register_button = tk.Button(user_info_window, text="Register", command=register_user, bg="#FF69B4", fg="white", font=('Helvetica', 12, 'bold'))
    register_button.pack(pady=5)

    login_button = tk.Button(user_info_window, text="Login", command=login_user, bg="#FF69B4", fg="white", font=('Helvetica', 12, 'bold'))
    login_button.pack(pady=5)

open_welcome_window()