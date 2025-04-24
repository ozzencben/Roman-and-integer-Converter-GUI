import tkinter
from tkinter import messagebox
from romanToIntFunc import valueControl

def convert():
    value = value_entry.get()
    result = ""
    if value.isdigit():
        result = valueControl(int(value))
    else:
        result = valueControl(value.upper())
    result_label.config(text=result)

window = tkinter.Tk()
window.title("Roman and Integer Conversion App")
window.config(bg="slategrey")

sh = window.winfo_screenheight()
sw = window.winfo_screenwidth()

height =260
width = 400

x = (sw - width) // 2
y = (sh - height) // 2

window.geometry(f"{width}x{height}+{x}+{y}")

title_label = tkinter.Label(text="Please enter your values", font=("montserrat", 15, "normal"), bg="slategrey")
title_label.pack(pady=15)

value_entry = tkinter.Entry(width=30, font=("montserrat", 12, "normal"), relief="flat")
value_entry.pack(pady=20)

convert_button = tkinter.Button(text="Convert", font=("montserrat", 12, "normal"), relief="flat", cursor="hand2")
convert_button.config(command=convert)
convert_button.pack(pady=20)

result_label = tkinter.Label(text="Ready", font=("montserrat", 12, "normal"), bg="slategrey")
result_label.pack(side="bottom", pady=20)

window.mainloop()
# def convert():
#     value = entry.get()
#
#     try:
#         # Integer mi diye kontrol et
#         if value.isdigit():
#             result = valueControl(int(value))
#         else:
#             result = valueControl(value.upper())
#         result_label.config(text=f"Sonuç: {result}")
#     except Exception as e:
#         messagebox.showerror("Hata", str(e))
#
# # Pencere oluştur
# window = tk.Tk()
# window.title("Roma Rakamı Dönüştürücü")
# window.config(bg="gainsboro")
#
# # Ortala
# w, h = 400, 300
# sw = window.winfo_screenwidth()
# sh = window.winfo_screenheight()
# x = (sw - w) // 2
# y = (sh - h) // 2
# window.geometry(f"{w}x{h}+{x}+{y}")
#
# # Başlık
# title_label = tk.Label(window, text="Sayı veya Roma Rakamı girin:", font=("montserrat", 14), bg="gainsboro")
# title_label.pack(pady=10)
#
# # Giriş
# entry = tk.Entry(window, font=("montserrat", 14), width=25)
# entry.pack(pady=10)
#
# # Dönüştür Butonu
# button = tk.Button(window, text="Dönüştür", font=("montserrat", 14), command=convert, cursor="hand2")
# button.pack(pady=10)
#
# # Sonuç etiketi
# result_label = tk.Label(window, text="Sonuç:", font=("montserrat", 14), bg="gainsboro")
# result_label.pack(pady=20)
#
# window.mainloop()
