import tkinter as tk
from tkinter import ttk

# --- Conversion Logic ---
def perform_conversion(val, mode):
    if mode == "Celsius to Fahrenheit":
        return (val * 9/5) + 32
    elif mode == "Fahrenheit to Celsius":
        return (val - 32) * 5/9
    elif mode == "Kilometers to Miles":
        return val * 0.621371
    elif mode == "Miles to Kilometers":
        return val * 1.60934
    return 0.0

# --- Event Handlers ---
def calculate():
    try:
        # Prevent crash if input is invalid or empty
        input_value = float(entry_input.get())
        selected_mode = combo_mode.get()
        
        raw_result = perform_conversion(input_value, selected_mode)
        
        # Format to 2 decimal places, removing trailing zeros
        formatted_result = f"{raw_result:.2f}".rstrip('0').rstrip('.')
        label_result.config(text=formatted_result, fg="black")
    except ValueError:
        label_result.config(text="Invalid Input", fg="red")

def update_labels(event):
    # Dynamically update the UI labels based on dropdown selection
    mode = combo_mode.get()
    if mode == "Celsius to Fahrenheit":
        label_unit_in.config(text="Celsius")
        label_unit_out.config(text="Fahrenheit")
        window.title("Celsius to Fahrenheit")
    elif mode == "Fahrenheit to Celsius":
        label_unit_in.config(text="Fahrenheit")
        label_unit_out.config(text="Celsius")
        window.title("Fahrenheit to Celsius")
    elif mode == "Kilometers to Miles":
        label_unit_in.config(text="Kilometers")
        label_unit_out.config(text="Miles")
        window.title("KM to Miles")
    elif mode == "Miles to Kilometers":
        label_unit_in.config(text="Miles")
        label_unit_out.config(text="Km")
        window.title("Miles to KM")
    
    # Clear the previous result when changing modes
    label_result.config(text="0", fg="black")

# --- UI Setup ---
window = tk.Tk()
window.title("Multi-Converter")
window.config(padx=20, pady=20) # Add padding for a cleaner look

# Dropdown for selecting conversion type
modes = [
    "Celsius to Fahrenheit", 
    "Fahrenheit to Celsius", 
    "Kilometers to Miles", 
    "Miles to Kilometers"
]
combo_mode = ttk.Combobox(window, values=modes, state="readonly", width=22)
combo_mode.current(0)
combo_mode.grid(row=0, column=0, columnspan=3, pady=(0, 15))
combo_mode.bind("<<ComboboxSelected>>", update_labels)

# Input Row
entry_input = tk.Entry(width=10)
entry_input.grid(row=1, column=1)

label_unit_in = tk.Label(text="Celsius")
label_unit_in.grid(row=1, column=2, sticky="w", padx=5)

# Output Row
label_equal = tk.Label(text="is equal to")
label_equal.grid(row=2, column=0, sticky="e", padx=5)

label_result = tk.Label(text="0", font=("Arial", 10, "bold"))
label_result.grid(row=2, column=1)

label_unit_out = tk.Label(text="Fahrenheit")
label_unit_out.grid(row=2, column=2, sticky="w", padx=5)

# Action Row
button_calculate = tk.Button(text="Calculate", command=calculate, width=10)
button_calculate.grid(row=3, column=1, pady=(15, 0))

window.mainloop()
