from urllib.request import urlopen
from bs4 import BeautifulSoup
html=urlopen("https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=blUw&qvt=0&query=04%EC%9B%9426%EC%9D%BC%EC%A3%BC%20%EB%93%9C%EB%9D%BC%EB%A7%88%20%EC%BC%80%EC%9D%B4%EB%B8%94%EC%8B%9C%EC%B2%AD%EB%A5%A0")
soup=BeautifulSoup(html,"lxml")
contents=soup.find_all('a',{'onclick':"return goOtherCR(this, 'a=nco_x0u*c.wdtitle&r=1&i=081024DF_000000000000&u=' + urlencode(this.href));"})
watch=soup.find_all('p',{'class':"rate"})
list=[]
list2=[]
for content in contents:
    list.append(content.get_text())
print(list)
for people in watch:
    list2.append(people.get_text())
list3 = []
for i in list2:
    j = len(i)
    list3.append(i[0:j-1])
print(list3)

import matplotlib.pyplot as plt
people=list3
x=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
plt.rc('font', family='Malgun Gothic')
title=list
plt.plot(x,people,label=title, c='r',lw=3)
plt.xticks(x,title,rotation='vertical')
plt.ylabel('시청률')
plt.xlabel('드라마 프로그램')
plt.suptitle('04월 26일주 평균 드라마 시청률')
plt.show()

list.pop(5)
list.pop(6)
list.pop(6)
list.pop(8)
list.pop(8)
list.pop(8)
list.pop(8)
list.pop(8)
list.pop(9)
list.pop(9)
list.pop(9)

list3.pop(5)
list3.pop(6)
list3.pop(6)
list3.pop(8)
list3.pop(8)
list3.pop(8)
list3.pop(8)
list3.pop(8)
list3.pop(9)
list3.pop(9)
list3.pop(9)


import matplotlib.pyplot as plt
people=list3
x=[1,2,3,4,5,6,7,8,9]
plt.rc('font', family='Malgun Gothic')
title=list
plt.plot(x,people,label=title, c='r',lw=3)
plt.xticks(x,title,rotation='vertical')
plt.ylabel('시청률')
plt.xlabel('드라마 프로그램')
plt.suptitle('04월 26일주 평균 드라마 시청률')
plt.show()