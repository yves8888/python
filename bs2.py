#coding=utf-8

from bs4 import BeautifulSoup
import urllib.request
urls = []
for i in range(1,54):
    url = "http://www.cnblogs.com/php-linux/?page="+str(i)
    res = urllib.request.urlopen(url)

    soup = BeautifulSoup(res,'lxml')
    book_div = soup.find(attrs={'id':"mainContent"})
    book_a = book_div.findAll(attrs={"class":'postTitle2'})
    f = open('a.txt',"a",encoding='utf8')
    for book in book_a :
        urls.append(book.get('href'))
        #f.write(book.string+str("链接:")+ str(book.get('href')) + "\n")
    f.close()
    print("保存成功"+ book.string+str("链接:")+ str(book.get('href')))

print(urls)