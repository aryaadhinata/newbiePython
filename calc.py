import tkinter as tk
from tkinter import messagebox
import math

# Fungsi untuk menghitung hasil
def calculate():
    try:
        x = float(entry_x.get())
        y = float(entry_y.get()) if entry_y.get() else None  # Nilai kedua opsional
        operation = operation_var.get()

        if operation == "tambah":
            result = x + y
        elif operation == "kurang":
            result = x - y
        elif operation == "bagi":
            if y is None or y == 0:
                messagebox.showerror("Kesalahan", "Pembagian dengan nol tidak diizinkan")
                return
            result = x / y
        elif operation == "kali":
            result = x * y
        elif operation == "sisa bagi":
            if y is None or y == 0:
                messagebox.showerror("Kesalahan", "Pembagian dengan nol tidak diizinkan untuk operasi sisa bagi")
                return
            result = x % y
        elif operation == "pangkat":
            result = x ** y
        elif operation == "akar":
            if y is None:
                y = 2  # Default ke akar kuadrat
            if x < 0:
                messagebox.showerror("Kesalahan", "Akar dari bilangan negatif tidak diizinkan")
                return
            result = round(x ** (1 / y), 6)  # Menghitung akar pangkat y
        else:
            messagebox.showerror("Kesalahan", f"Operasi '{operation}' tidak dikenal")
            return

        label_result.config(text=f"Hasil: {result}")
    except ValueError:
        messagebox.showerror("Kesalahan", "Masukkan nilai numerik yang valid")
    except Exception as e:
        messagebox.showerror("Kesalahan", f"Kesalahan tidak terduga: {e}")

# Membuat jendela utama
root = tk.Tk()
root.title("Kalkulator")
root.geometry("350x350")
root.configure(bg="#F4F4F4")

# Judul
title_label = tk.Label(root, text="Kalkulator", font=("Arial", 18, "bold"), bg="#F4F4F4", fg="#333333")
title_label.pack(pady=10)

# Pilihan operasi
operation_var = tk.StringVar()
operation_var.set("tambah")
operations = ["tambah", "kurang", "bagi", "kali", "sisa bagi", "pangkat", "akar"]
operation_menu = tk.OptionMenu(root, operation_var, *operations)
operation_menu.config(font=("Arial", 12), bg="#4CAF50", fg="white")
operation_menu.pack(pady=10)

# Input nilai pertama
label_x = tk.Label(root, text="Nilai pertama:", font=("Arial", 12), bg="#F4F4F4", fg="#333333")
label_x.pack()
entry_x = tk.Entry(root, font=("Arial", 12), justify="center")
entry_x.pack(pady=5)

# Input nilai kedua
label_y = tk.Label(root, text="Nilai kedua:", font=("Arial", 12), bg="#F4F4F4", fg="#333333")
label_y.pack()
entry_y = tk.Entry(root, font=("Arial", 12), justify="center")
entry_y.pack(pady=5)

# Tombol hitung
calculate_button = tk.Button(root, text="Hitung", font=("Arial", 14), bg="#FF5722", fg="white", command=calculate)
calculate_button.pack(pady=20)

# Label hasil
label_result = tk.Label(root, text="Hasil: ", font=("Arial", 14, "bold"), bg="#F4F4F4", fg="#333333")
label_result.pack(pady=10)

# Menjalankan aplikasi
root.mainloop()
