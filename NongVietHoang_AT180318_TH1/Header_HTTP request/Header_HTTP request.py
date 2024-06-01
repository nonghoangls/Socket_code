#khai báo thư viện
import urllib.request
from urllib.request import(Request)

#url chứa địa chỉ URL mà chúng ta muốn gửi yêu cầu HTTP đến, và USER_AGENT chứa chuỗi User-Agent của trình duyệt.
#User-Agent là một phần của header HTTP mà trình duyệt gửi đi khi yêu cầu một trang web. Trong trường hợp này,
#User-Agent được thiết lập để giống với trình duyệt Chrome trên Windows
url = 'http://python.org'
USER_AGENT = 'Mozilla/5.0 (Windows NT'

#Định nghĩa hàm chrome_user_agent(), chứa logic chính của chương trình:
def chrome_user_agent():
    #Mở một HTTP opener sử dụng build_opener().
    opener = urllib.request.build_opener()

    #Thêm header User-Agent vào opener với giá trị từ biến USER_AGENT
    opener.addheaders = [('User-Agent', USER_AGENT)]

    #Cài đặt opener vừa tạo bằng cách sử dụng install_opener(opener).
    urllib.request.install_opener(opener)

    #Gửi yêu cầu HTTP đến URL được chỉ định và lưu trữ phản hồi trong biến response.
    #response = urllib.request.urlopen(url)

    #In ra các header trong phản hồi HTTP sử dụng response.getheaders().
    # print('Response headers')
    # print('.......................')
    # #Vòng lặp này lặp qua tất cả các header có trong phản hồi HTTP. Hàm response.getheaders() trả về một danh sách
    # #các cặp (header, value), trong đó mỗi cặp đại diện cho một header và giá trị tương ứng của nó.
    # for header, value in response.getheaders():
    #     print(header + ':' + value)

    #Tạo một yêu cầu HTTP bằng cách sử dụng Request(url) và thêm header User-Agent vào yêu cầu này.
    request = Request(url)
    request.add_header('User-Agent', USER_AGENT)

    #In ra các header của yêu cầu HTTP sử dụng request.headers.items().
    print('\nRequest headers')
    print('..........................')
    for header,value in request.headers.items():
        print(header + ':' + value)

#Hàm chạy chính
#Kết thúc bằng cách gọi hàm chrome_user_agent().
if __name__ == '__main__':
    chrome_user_agent()
