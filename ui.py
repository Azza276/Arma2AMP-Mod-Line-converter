import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
from main import process_file

# Global variable to store the full file path
full_file_path = ""

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

def select_file():
    global full_file_path
    try:
        full_file_path = filedialog.askopenfilename(filetypes=[("HTML files", "*.html")])
        if full_file_path:
            file_name = os.path.basename(full_file_path)
            file_label.config(text=file_name)
            convert_button.config(state=tk.NORMAL)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while selecting the file: {e}")

def clear_file():
    global full_file_path
    try:
        full_file_path = ""
        file_label.config(text="")
        convert_button.config(state=tk.DISABLED)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while clearing the file: {e}")

def on_generate():
    global full_file_path
    try:
        workshop_mod_line = workshop_var.get()
        mod_id_line = mod_id_var.get()
        mod_name_line = mod_name_var.get()
        
        if not (workshop_mod_line or mod_id_line or mod_name_line):
            messagebox.showinfo("No Options Selected", "Please select at least one option.", icon='info')
            return
        
        process_file(full_file_path, workshop_mod_line, mod_id_line, mod_name_line)
        
        response = messagebox.askquestion("Success", "Mod line generation was successful. Do you want to do another?", icon='question')
        if response == 'yes':
            clear_file()
        else:
            exit_app()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred during mod line generation: {e}")

def exit_app():
    try:
        root.quit()
        os._exit(0)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while exiting the application: {e}")

# Create the main window
root = tk.Tk()
root.title("HTML to Mod Line Converter")
root.geometry("650x650")
root.resizable(True, True)

# Set the app icon
icon_path = os.path.join(script_dir, 'snake-a.ico')
root.iconbitmap(icon_path)

# Create a style
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12), padding=6)
style.configure("TLabel", font=("Helvetica", 12), padding=6)
style.configure("TCheckbutton", font=("Helvetica", 12), padding=6)

# Create a frame for the file selection
file_frame = ttk.Frame(root, padding="10 10 10 10")
file_frame.pack(pady=5, fill=tk.X)

# Add a label above the select button
select_label = ttk.Label(file_frame, text="1. Select the ArmA3 Launcher Mod Export HTML File you would like to convert.", anchor="w")
select_label.pack(side=tk.TOP, padx=5, anchor="w")

# Create a button to select the HTML file
select_button = ttk.Button(file_frame, text="Select HTML File", command=select_file)
select_button.pack(side=tk.LEFT, padx=5)

# Create a Label to show the selected file path
file_label_frame = ttk.Frame(root, padding="10 10 10 10")
file_label_frame.pack(pady=5, padx=10, fill=tk.X)

# Add a label above the file path label
ensure_label = ttk.Label(file_label_frame, text="2. Ensure correct file selected.", anchor="w")
ensure_label.pack(side=tk.TOP, padx=5, anchor="w")

file_label = ttk.Label(file_label_frame, text="", width=30, anchor="w")
file_label.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

# Create a clear button
clear_button = ttk.Button(file_label_frame, text="Clear", command=clear_file)
clear_button.pack(side=tk.LEFT, padx=5)

# Create a frame for the checkboxes
checkbox_frame = ttk.Frame(root, padding="10 10 10 10")
checkbox_frame.pack(pady=5, fill=tk.X)

# Add a label above the options
select2_label = ttk.Label(checkbox_frame, text="3. Select which Mod Line variants you need.", anchor="w")
select2_label.pack(side=tk.TOP, padx=5, anchor="w")

# Create checkboxes for the options
workshop_var = tk.BooleanVar(value=True)
mod_id_var = tk.BooleanVar(value=True)
mod_name_var = tk.BooleanVar(value=False)

workshop_check = ttk.Checkbutton(checkbox_frame, text="Workshop Mod Line - For Steam Workshop Mod Download.", variable=workshop_var)
mod_id_check = ttk.Checkbutton(checkbox_frame, text="Mod ID Line - For Mod Steam ID Server Mod Lines.", variable=mod_id_var)
mod_name_check = ttk.Checkbutton(checkbox_frame, text="Mod Name Line - For Mod @Name Server Mod Lines.", variable=mod_name_var)

workshop_check.pack(anchor=tk.W, pady=2)
mod_id_check.pack(anchor=tk.W, pady=2)
mod_name_check.pack(anchor=tk.W, pady=2)

# Create a frame for the action buttons
button_frame = ttk.Frame(root, padding="10 10 10 10")
button_frame.pack(pady=5, fill=tk.X)

# Add a label above the generate button
generate_label = ttk.Label(button_frame, text="4. Click Generate to create the text files in the same folder as the HTML.", anchor="w")
generate_label.pack(side=tk.TOP, padx=5, anchor="w")

# Create a button to execute the converter, initially disabled
convert_button = ttk.Button(button_frame, text="Generate", command=on_generate, state=tk.DISABLED)
convert_button.pack(side=tk.LEFT, padx=5)

# Create a frame below action buttons
bbutton_frame = ttk.Frame(root, padding="10 10 10 10")
bbutton_frame.pack(pady=5, fill=tk.X)

# Add a label below the generate button
generate2_label = ttk.Label(bbutton_frame, text="5. Copy text file content to AMP (or any other server that needs it).", anchor="w")
generate2_label.pack(side=tk.LEFT, padx=5, pady=10, anchor="w")

# Create a frame for the exit button
exit_button_frame = ttk.Frame(root, padding="10 10 10 10")
exit_button_frame.pack(side=tk.BOTTOM, anchor=tk.SE, pady=10, padx=10)

# Create an exit button
exit_button = ttk.Button(exit_button_frame, text="Exit", command=exit_app)
exit_button.pack(side=tk.RIGHT)

# Run the application
root.mainloop()