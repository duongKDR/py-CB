import requests, json

response = requests.get("http://localhost:8000")
print(response.text)



# Định nghĩa đường dẫn của API
url = 'http://localhost:8000'

# Định nghĩa dữ liệu cần gửi đến API
data = {'title': 'foo', 'body': 'bar', 'userId': 1}

# Gửi yêu cầu POST đến API và lưu phản hồi vào biến response
responsePost = requests.post(url= url, data=json.dumps(data))

# In ra mã trạng thái của phản hồi từ API
print('Status code:', responsePost.status_code)

# In ra nội dung của phản hồi từ API
print('Response:', responsePost)
