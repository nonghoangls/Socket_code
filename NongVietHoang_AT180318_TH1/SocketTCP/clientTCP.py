
#khai báo thư viện socket
import socket

#tao dia chi va cong ma server lang nghe toi
TCP_IP = "127.0.0.1"
TCP_PORT = 12000


while True:
    #tao client socket, tham so dau tien truyen vao la ipv4(AF_INET)va tham so thu 2 truyen vao su dung giao thuc TCP(SOCK_STREAM)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #client ket noi voi server theo dia chi va cong o tren
    client_socket.connect((TCP_IP, TCP_PORT))

    #bien message se duoc luu thong tin qua ham input o duoi; va voi vong lap cho den khi nguoi dung type'exit' thi
    #chuong trinh se ngung
    message = input("Input lowercase sentence:(type 'exit' to quit): ")
    if message.lower() == 'exit':
        break

    #client su dung send de gui tin nhan toi server va chuyen doi thong diep duoi dang byte bang encode()
    client_socket.send(message.encode())

    #sau khi gui thong diep cho server thi no se luu vao bien modifield_ms va duoc chuyen tu byte sang chuoi
    #voi ham decode(); 2048 la so byte toi da dc lưu trong bộ đệm của client
    modified_message = client_socket.recv(2048).decode()

    #in ra màn hinh thong diep server vua gui lai
    print("Modified message from server:", modified_message)

    #xong viec dong lai client socket
    client_socket.close()
