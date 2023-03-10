# assert để kiểm tra các điều kiện và ném ra một ngoại lệ nếu điều kiện không được đáp ứng:
def divide(x, y):
    assert y != 0, "Y KO KHAC 0"
    return x / y

result = divide(10, 0)  # Raises an AssertionError
