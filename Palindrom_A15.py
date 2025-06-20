import re
import vs as ctk
from tkinter import messagebox

def is_palindrome(s: str) -> bool:
    normalized = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    return normalized == normalized[::-1]

def check_palindrome():
    user_input = entry.get()
    if not user_input.strip():
        messagebox.showwarning("Input Kosong", "Silakan masukkan string terlebih dahulu.")
        return
    if is_palindrome(user_input):
        result_label.configure(text=f'"{user_input}" adalah palindrom.', text_color="green")
    else:
        result_label.configure(text=f'"{user_input}" bukan palindrom.', text_color="red")

# Interface
ctk.set_appearance_mode("Light")         
ctk.set_default_color_theme("green")      

app = ctk.CTk()
app.title("Deteksi Palindrom")
app.geometry("500x370")

font_title = ("Poppins", 20, "bold")
font_desc = ("Poppins", 12, "italic")
font_body = ("Poppins", 14)

frame = ctk.CTkFrame(app, fg_color="transparent")
frame.pack(expand=True)

title_label = ctk.CTkLabel(frame, text="Palindrom Checker", font=font_title)
title_label.pack(pady=(10, 4))

desc_label = ctk.CTkLabel(
    frame,
    text="Input boleh huruf saja, angka saja,\natau kombinasi huruf dan angka.\nContoh: '12321', 'ABBA', atau 'A1B2B1A'.",
    font=font_desc,
    justify="center"
)
desc_label.pack(pady=(0, 20))

entry = ctk.CTkEntry(frame, width=300, font=font_body, placeholder_text="Masukkan huruf dan/atau angka...")
entry.pack(pady=10)

check_button = ctk.CTkButton(frame, text="Cek", font=font_body, command=check_palindrome)
check_button.pack(pady=10)

result_label = ctk.CTkLabel(frame, text="", font=font_body)
result_label.pack(pady=20)

app.mainloop()