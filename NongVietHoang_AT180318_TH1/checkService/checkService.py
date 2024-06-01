# import thư viện socket
import socket

#gán biến ip có địa chỉ như dưới
ip = '142.250.207.78' #facebook.com

# tạo 1 list những port mà mình muốn kiểm tra
portlist = [21,22,23,80,443]

#vòng lặp for với biến port chạy trong portlist

for port in portlist:
    #dòng này tạo 1 socket với addressFamily là ipv4 và socketType là giao thức TCP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #kết nối thử địa chỉ và cổng đc cho trước rồi lưu vào biến result
    result = sock.connect_ex((ip,port))
    #in ra màn hình trạng thái kết nối: 0 là cổng đang sử dụng, khác 0 là cổng không có  kết nối(errno)
    print(port, ':', result)
    #đóng socket
    sock.close()