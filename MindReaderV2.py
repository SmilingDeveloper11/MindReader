import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import time
import threading

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x_coordinate = (screen_width - width) // 2
    y_coordinate = (screen_height - height) // 2

    window.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")

def analyze():
    number = input_entry.get()
    if not number.isdigit():
        messagebox.showerror("Invalid Input", "Please enter only numbers.")
        return
    
    # Cerrar la ventana principal
    root.withdraw()
    
    # Mostrar ventana de carga
    loading_window = tk.Toplevel()
    loading_window.title("Loading")
    loading_window.geometry("300x100")  # Tamaño de la ventana de carga
    center_window(loading_window, 300, 100)
    
    loading_label = tk.Label(loading_window, text="Analyzing brainwaves...")
    loading_label.pack()
    
    progress_bar = ttk.Progressbar(loading_window, orient='horizontal', mode='determinate', length=200)
    progress_bar.pack(pady=5)
    
    # Simular proceso de carga
    for i in range(101):
        progress_bar['value'] = i
        loading_window.update_idletasks()  # Actualizar la ventana de carga
        time.sleep(0.1)  # Pequeño retraso para simular carga
        
        # Actualizar el texto de la carga en función del progreso
        if i == 25:
            loading_label.config(text="Scanning memories...")
        elif i == 50:
            loading_label.config(text="Calculating probabilities...")
        elif i == 75:
            loading_label.config(text="Decoding thoughts...")
    
    # Cerrar la ventana de carga al finalizar
    loading_window.destroy()
    
    # Mostrar el número pensado
    result_window = tk.Toplevel()
    result_window.title("Result")
    result_window.geometry("200x50")  # Tamaño de la ventana de resultado
    center_window(result_window, 200, 50)
    
    result_label = tk.Label(result_window, text=f"You're thinking of the number {number}.")
    result_label.pack(pady=10)

def read_mind():
    threading.Thread(target=analyze).start()

root = tk.Tk()
root.title("Mind Reader")
root.geometry("300x200")  # Tamaño de la ventana principal
center_window(root, 300, 200)

text_label = tk.Label(root, text="Think of a number between 1 and 10")
text_label.pack(pady=10)

validate_input = root.register(lambda x: x.isdigit())  # Validación para permitir solo números
input_entry = tk.Entry(root, width=10, validate="key", validatecommand=(validate_input, "%S"))
input_entry.pack(pady=5)

read_button = tk.Button(root, text="Read my mind", command=read_mind)
read_button.pack(pady=10)

root.mainloop()
