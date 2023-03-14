from http.server import BaseHTTPRequestHandler, HTTPServer

class Vidu(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        html = "<div><a href='#'>Trang chủ</a><a href='#'>Tin tức</a><a href='#'>Liên hệ</a></div>"
        self.wfile.write(html.encode("utf8"))
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        processed_data = process_post_data(post_data)
        self.send_response(200)
        self.send_header('Content-type', 'text/ex')
        self.end_headers()
        self.wfile.write(processed_data.encode('utf-8'))
    def process_post_data(data):
    # Xử lý dữ liệu ở đây
        post_data = request.get_json()

    # Trả về kết quả xử lý
        processed_data = "Processed data: " + str(post_data)
    
    # Trả về kết quả xử lý
    return processed_data
if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, Vidu)
    print('Đang khởi động server...')
    httpd.serve_forever()
