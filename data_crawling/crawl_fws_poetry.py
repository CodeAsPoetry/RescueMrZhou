# coding = "utf-8"

import json
import time
import random
import requests
from bs4 import BeautifulSoup


if __name__ == "__main__":

    # f_o = open('../data/IP代理池.txt', 'r', encoding='utf-8')
    # proxies_list = f_o.readlines()
    # proxies_list = [json.loads(item.strip()) for item in proxies_list]
    # proxies = proxies_list[random.randint(0, len(proxies_list)-1)]

    proxies = {'HTTP': '61.216.156.222:60808', 'HTTPS': 'https://61.216.156.222:60808'}

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
         Chrome/80.0.3987.163 Safari/537.36"
    }

    url = 'https://www.gushimi.org/shiren/6284.html'
    res = requests.get(url=url, headers=headers, proxies=proxies)

    print(res.text)




    # poetry_urls = browser.find_elements(by=By.XPATH, value='//div[@class="relevant_news"]/ul/li/a')
    # print(poetry_urls, len(poetry_urls))
    #
    # f = open('../data/fangwenshan_poetry_name_link.json', 'w', encoding='utf-8')
    # for poetry_url in poetry_urls:
    #     f.write(json.dumps({poetry_url.text: poetry_url.get_attribute('href')}, ensure_ascii=False))
    #     f.write('\n')
    # f.close()
