#khai bao thu vien socket
import socket

#cho dia chi va cong cua server
TCP_IP = "127.0.0.1"
TCP_PORT = 12000

#tao server socket voi tham so dau tien la ipv4 va tham so thu 2 la giao thuc TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#server socket lang nghe voi tham so duoc truyen vao TCP_IP va TCP_PORT
server_socket.bind((TCP_IP, TCP_PORT))

#server socket nghe de chap nhan ket noi tu client, o day cho phep 1 ket noi duoc truy cap cung 1 luc
server_socket.listen(1)

#in ra thong bao server da chay
print("TCP Server is running...")


while True:
    #server chap nhan ket noi voi client  Khi một kết nối được chấp nhận, nó trả về một đối tượng socket mới (connection_socket)
    #để truyền và nhận dữ liệu từ client và một tuple (addr) chứa địa chỉ IP và số cổng của client.
    connection_socket, addr = server_socket.accept()

    #Server nhận dữ liệu từ client thông qua kết nối socket (connection_socket) bằng cách sử dụng phương thức recv().
    #Dữ liệu được nhận có thể được giới hạn bởi kích thước buffer, trong trường hợp này là 2048 byte,
    #và sau đó được giải mã từ dạng byte sang chuỗi văn bản bằng phương thức decode()
    message = connection_socket.recv(2048).decode()

    #Sau khi nhận được dữ liệu từ client, server chuyển đổi dữ liệu thành chữ hoa bằng cách sử dụng phương thức upper().
    #Sau đó, dữ liệu đã sửa đổi này được gửi lại cho client thông qua kết nối socket bằng phương thức send().
    #Trước khi gửi, dữ liệu được mã hóa từ chuỗi văn bản sang dạng byte bằng phương thức encode()
    modified_message = message.upper()
    connection_socket.send(modified_message.encode())

    #dong server socket
    connection_socket.close()

