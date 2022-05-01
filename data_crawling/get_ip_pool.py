# coding = "utf-8"


import time
import requests
from bs4 import BeautifulSoup


# 检查IP的可用性
def check_ip(list_ip):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 Edg/91.0.864.71',
        'Connection': 'close'}
    # url = 'https://www.baidu.com'  # 以百度为例，检测IP的可行性
    url = 'https://movie.douban.com/subject/1292052/'

    can_use = []
    for ip in list_ip:
        try:
            response = requests.get(url=url, headers=headers, proxies=ip, timeout=3)  # 在0.1秒之内请求百度的服务器
            if response.status_code == 200:
                can_use.append(ip)
        except Exception as e:
            print(e)

    return can_use


if __name__=="__main__":

    list_ip = []
    list_port = []
    list_headers_ip = []

    for start in range(1, 11):

        url = 'https://www.kuaidaili.com/free/inha/{}/'.format(start)  # 每页15个数据，共爬取10页
        print("正在处理url: ", url)

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)\
                           Chrome/91.0.4472.164 Safari/537.36 Edg/91.0.864.71'}
        response = requests.get(url=url, headers=headers)

        soup = BeautifulSoup(response.text, 'html.parser')

        ip = soup.select('#list > table > tbody > tr > td:nth-child(1)')
        port = soup.select('#list > table > tbody > tr > td:nth-child(2)')

        for i in ip:
            list_ip.append(i.get_text())

        for i in port:
            list_port.append(i.get_text())

        time.sleep(1)  # 防止爬取太快，数据爬取不全

    # 代理ip的形式:        'http':'http://119.14.253.128:8088'

    for i in range(150):
        IP_http = '{}:{}'.format(list_ip[i], list_port[i])
        IP_https = 'https://{}:{}'.format(list_ip[i], list_port[i])
        proxies = {
            'HTTP': IP_http,
            'HTTPS': IP_https
        }
        list_headers_ip.append(proxies)

    print(list_headers_ip)

    can_use = check_ip(list_headers_ip)
    print('能用的代理IP为：', can_use)
    for i in can_use:
        print(i)
    print('能用的代理IP数量为：', len(can_use))

    fo = open('../data/IP代理池.txt', 'w')
    for i in can_use:
        fo.write(str(i) + '\n')

    fo.close()

    """
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) \
    #                   Chrome/69.0.3497.100 Safari/537.36'}
    # get请求获取
    # response = requests.get(url='http://www.hxlib.cn/gushi/0/117/0/0/0/1/')
    # print(response.text)

    # 启动浏览器

    # chrome_options = Options()
    # chrome_options.add_argument('--headless')
    #
    # browser = webdriver.Chrome(options=chrome_options)  # 设置驱动参数
    # # browser = webdriver.Chrome()
    #
    






    # url = 'https://www.baidu.com'
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
    # # get请求获取
    # res = requests.get(url, headers=headers)
    #
    # print(res.status_code, "\t\t(响应状态码)")
    # print(res.encoding, "\t\t(获取编码格式)")
    # print(res.raw, "\t\t(原始响应体，使用r.raw.read()读取)")
    # print(res.content, "\t\t(字节方式的响应体，需要进行解码)")
    # print(res.headers, "\t\t(以字典对象储存服务器响应头，但是这个字典比较特殊，字典键不区分大小写，若键不存在，则返回None)")
    # print(res.raise_for_status(), "\t\t(请求失败(非200响应)，抛出异常)")
    # print(res.url, "\t\t(获取请求的url)")
    # print(res.cookies, "\t\t(获取请求后的cookies)")
    # print(res.json(), "\t\t(request中内置的json解码器)")
    # print(res.text, "\t\t(字符串方式的响应体，会自动更具响应头部的字符编码进行解码)")



    # for i in poetry_urls:
    #     print(i.text)
    #     print(i.get_attribute('href'))
    # for i in range(2):
    #     response_content = requests.get(url='https://www.baidu.com', headers=headers)
    #     print(response_content)
    #     print(response_content.text)


    # for poetry_url in poetry_urls:
    #     poetry_name = poetry_url.text
    #     print(poetry_url.text)
    #     print(poetry_url.get_attribute('herf'))
    #
    #     response_content = requests.get(poetry_url.get_attribute('herf'))
    #
    #     print(response_content)

    #     temp_f = open(poetryFilePath + poetry_name + '.txt', 'w', encoding='utf-8')
    #
    #     for item in poetry:
    #         temp_f.write(item.text)
    #
    #     temp_f.close()
    #     time.sleep(0.1)
    #
    # browser.close()
    """
