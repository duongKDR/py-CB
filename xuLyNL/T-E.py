# Sử dụng try-except để bắt và xử lý ngoại lệ:

try:
    x = int(input("Enter a number: "))
    y = 1 / x
except ValueError:
    print("NHAP VAO SAI ")
except ZeroDivisionError:
    print("KO THE CHIA CHO 0!")
else:
    print("kq 1/X :", y)
finally:
    print("XONG.")
