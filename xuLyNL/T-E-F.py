# Sử dụng try-except-finally để thực hiện các hành động dọn dẹp trong khối mã finally sau khi kết thúc khối mã try-except:  
try:
    f = open("example.txt", "r")
    data = f.read()
    print(data)
except FileNotFoundError:
    print("File not found!")
finally:
    f.close()
    print("Done.")
