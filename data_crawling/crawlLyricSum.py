# coding = "utf-8"

# 爬取所有歌曲的链接信息，写文件代码在获得数据后注销，防止误操作

from selenium import webdriver
import time

songFilePath = "F://RescueMrZhou/Corpus/songSum.txt"

if __name__=="__main__":
    # 启动浏览器
    browser = webdriver.Chrome()
    # 打开要抓取的歌手页面
    browser.get('http://www.kuwo.cn/artist/content?name=周杰伦')
    # 点击歌曲按钮，获取歌曲列表
    songButton = browser.find_element_by_xpath('//div[@class="tab"]//li[@id="tab_music"]//span')
    songButton.click()
    time.sleep(3)
    print("songButton",songButton)
    # songFile = open(songFilePath,"w",encoding="utf-8")
    pageNum=1
    while(pageNum<65):
        songList = browser.find_elements_by_xpath('//div[@id="song"]//ul[@class="listMusic"]//li//div[@class="name"]/a')
        for i in songList:
            print(i.text,i.get_attribute("href"))
            # songFile.write(i.text)
            # songFile.write(":")
            # songFile.write(i.get_attribute("href"))
            # songFile.write("\n")
        # 找到下页链接
        next = browser.find_element_by_xpath('//div[@class="page"]//a[@class="next"]')
        browser.execute_script("arguments[0].scrollIntoView()", next)
        next.click()
        time.sleep(10)

    # songFile.close()
    browser.close()

