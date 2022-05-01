# coding="utf-8"

# 根据所有歌曲的链接列表爬取歌词，每首歌建立歌词文件，以歌名为文件名
# 写文件代码在获得数据后注销，防止误操作

from selenium import webdriver
import time
import urllib.request
from bs4 import BeautifulSoup

songFilePath = "F://RescueMrZhou/Corpus/songSum.txt"

if __name__=="__main__":

    songFile = open(songFilePath,"r",encoding="utf-8")
    songNum = 960
    i = 1
    errorList=[]
    while(i<=songNum):
        nameLink = songFile.readline().strip("\n")
        name = nameLink.split(":")[0]
        link = nameLink.split(":")[1]+":"+nameLink.split(":")[2]

        try:
            # 获取链接响应，以UTF-8格式解析HTML文档
            respone = urllib.request.urlopen(link)
            time.sleep(5)
            html = respone.read()
            html = html.decode('utf-8')
            # 利用BeautifulSoup包装html文档
            soup = BeautifulSoup(html, 'html.parser')
            # 解析歌词
            lyricList = soup.select('.lrcItem')
            # tempFilePath = "F://RescueMrZhou/Corpus/"+name+".txt"
            # tempFile = open(tempFilePath,"w",encoding="utf-8")
            for row in lyricList:
                print(row.string)
                # tempFile.write(row.string)
                # tempFile.write("\n")
        except Exception as e:
            print(e)
            errorList.append(i)

        i+=1

    # tempFile.close()
    print("errorList",len(errorList),errorList)


