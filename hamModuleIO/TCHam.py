x = 10  # Biến toàn cục

def func():  
    global x
    x = 20
    print("Giá trị của x trong hàm func():", x)

func()
print("Giá trị của x sau khi gọi hàm func():", x)

#  toan cuc trong ham long nhau:


y = 10  # bien tc

def outer_func():
    "toan cuc trong ham long nhau:"
    y = 20  # bien cb
    print("Giá trị của y trước khi gọi hàm inner_func():", y)

    def inner_func():
        global y
        y = 30  # sua
        print("Giá trị của y trong hàm inner_func():", y)

    inner_func()

    print("Giá trị của y trong hàm outer_func() sau khi gọi hàm inner_func():", y)

outer_func()
print("Giá trị của y sau khi gọi hàm outer_func():", y)

#  tham so doi so
def name(ten, tuoi =18):

    " tham so"
    print( " ten cua ban la", ten)
    print( "tuoi: ", tuoi)

name( "duong")
 
# ham lambda

listA = [2,3,4,6,7,8]
print(list(filter(lambda x: x%2 == 0, listA)))