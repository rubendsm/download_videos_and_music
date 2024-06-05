import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import os
import asyncio
from download_videos import download_videos

BASE_OUTPUT_DIR = "./videos/"

def process_videos():
    links = links_text.get("1.0", "end").strip().split("\n")
    format_choice = format_combobox.get()

    try:
        progress_bar["value"] = 0  # Reinicia a barra de progresso
        progress_bar["maximum"] = len(links)  # Define o número máximo de progresso
        progress_bar.grid(row=4, column=0, columnspan=2, sticky="we", pady=(10, 0))  # Torna a barra de progresso visível

        output_dir = output_dir_var.get()
        if not output_dir:
            messagebox.showerror("Error", "Please choose a download directory.")
            return

        print("Processing videos...")
        asyncio.run(download_videos(links, output_dir, format_choice, update_progress))
        print("Completed processing videos.")
        messagebox.showinfo("Success", f"{len(links)} videos downloaded successfully.")
    except Exception as e:
        print(f"Error processing videos: {e}")
        messagebox.showerror("Error", f"An error occurred: {e}")

def update_progress(current_progress):
    progress_bar["value"] = current_progress
    root.update_idletasks()

def choose_directory():
    chosen_dir = filedialog.askdirectory(initialdir=os.path.expanduser("~/Downloads"))
    output_dir_var.set(chosen_dir)
    output_dir_label.config(text=chosen_dir)

def show_info():
    info_window = tk.Toplevel(root)
    info_window.title("Information")
    info_label = tk.Label(info_window, text="Made by rubendsm 2024")
    info_label.pack(padx=20, pady=10)

root = tk.Tk()
root.title("Video Download Tool")

# Frame to hold user input fields
input_frame = ttk.Frame(root, padding="20")
input_frame.grid(row=0, column=0, sticky="nsew")

# Dividindo o frame horizontalmente
input_frame.columnconfigure(0, weight=1)
input_frame.columnconfigure(1, weight=1)

# Links entry
ttk.Label(input_frame, text="Enter Video Links (one link per line):").grid(row=0, column=0, sticky="w", pady=(0, 5))
links_text = tk.Text(input_frame, height=5, width=50)
links_text.grid(row=1, column=0, sticky="we", pady=(0, 10), columnspan=2)

# Format selection
ttk.Label(input_frame, text="Select Output Format:").grid(row=2, column=0, sticky="w", pady=(0, 5))
format_combobox = ttk.Combobox(input_frame, values=[".mp3", ".mp4"], width=10)
format_combobox.grid(row=2, column=1, sticky="we", pady=(0, 10))
format_combobox.current(0)  # Default to .mp3

# Choose directory button
output_dir_var = tk.StringVar(value=os.path.expanduser("~/Downloads"))
output_dir_button = ttk.Button(input_frame, text="Choose Download Directory", command=choose_directory)
output_dir_button.grid(row=3, column=0, sticky="we", pady=(10, 0))
output_dir_label = ttk.Label(input_frame, text=output_dir_var.get(), wraplength=300)
output_dir_label.grid(row=3, column=1, sticky="w", pady=(10, 0))

# Barra de progresso (inicialmente invisível)
progress_bar = ttk.Progressbar(input_frame, orient="horizontal", length=200, mode="determinate")
progress_bar.grid(row=4, column=0, columnspan=2, sticky="we", pady=(10, 0))
progress_bar.grid_remove()  # Esconde a barra de progresso inicialmente

# Button to initiate processing
process_button = ttk.Button(input_frame, text="Download Videos", command=process_videos)
process_button.grid(row=5, column=0, columnspan=2, sticky="we", pady=(10, 0))

# Botão de informação
info_button = ttk.Button(input_frame, text="ℹ️", command=show_info)
info_button.grid(row=0, column=1, sticky="ne", padx=(0, 20), pady=(20, 0))

# Estilo
root.option_add("*TCombobox*Listbox*Background", "white")
root.option_add("*TCombobox*Listbox*Foreground", "black")
root.option_add("*TCombobox*Listbox*Font", "Arial")

root.mainloop()
