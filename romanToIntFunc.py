from tkinter import messagebox

# # roman_functions.py
#
# def valueControl(value):
#     val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
#     syms = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
#
#     if isinstance(value, int):
#         if 1 <= value <= 4999:
#             roman_num = ""
#             for i in range(len(val)):
#                 while value >= val[i]:
#                     roman_num += syms[i]
#                     value -= val[i]
#             return roman_num
#         else:
#             raise ValueError("Lütfen 1 ile 4999 arasında bir sayı girin.")
#
#     elif isinstance(value, str):
#
#         for char in value[::-1]:  # Tersten işlem
#             if char not in roman_map:
#                 raise ValueError(f"Geçersiz karakter: {char}")
#             current = roman_map[char]
#             if current < prev:
#                 total -= current
#             else:
#                 total += current
#             prev = current
#         return total


def valueControl(value):
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    syms = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

    if isinstance(value, int):
        if 1 <= value <= 9999:
            value_str = ""
            for i in range(len(val)):
                while value >= val[i]:
                    value_str += syms[i]
                    value -= val[i]
            return value_str
        else:
            messagebox.showwarning("Error", "Please enter only numerical values")

    elif isinstance(value, str):
        roman_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        total = 0
        prev = 0

        for letter in value[::-1]:
            if letter not in roman_map:
                messagebox.showwarning("Please enter only Roman numerical values")

            current = roman_map[letter]
            if current < prev:
                total -= current
            elif current > prev:
                total += current
                prev = current
        return total
