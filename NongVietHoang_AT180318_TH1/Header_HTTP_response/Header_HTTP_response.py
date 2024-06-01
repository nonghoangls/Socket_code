#import thư viện urllib.request để có thể gửi yêu cầu HTTP và nhận phản hồi từ server.
import urllib.request

#hàm get_response_headers nhận một tham số là url để chỉ định trang web cụ thể mà chúng ta muốn lấy header của HTTP response.
def get_response_headers(url):
    # urllib.request.urlopen(url) được sử dụng để gửi yêu cầu HTTP đến URL đã cho và nhận phản hồi từ server.
    # Phản hồi này sẽ chứa các thông tin như header, nội dung, mã trạng thái, v.v.
    response = urllib.request.urlopen(url)

    # sử dụng vòng lặp để lặp qua tất cả các cặp (header, value) trong danh sách các header của phản hồi sử dụng response.getheaders().
    # Đối với mỗi cặp (header, value), chúng ta in ra tên của header và giá trị tương ứng của nó.
    print('Response headers')
    print('.......................')
    for header, value in response.getheaders():
        print(header + ':' + value)


#hàm chinh de chay
if __name__ == '__main__':
    url = 'http://python.org'
    get_response_headers(url)
