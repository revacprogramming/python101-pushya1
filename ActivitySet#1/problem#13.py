# Network Programming
# https://www.py4e.com/lessons/network

'''
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()
------------------------------------------------------------------------------------------------
Last-Modified:
 Sat, 13 May 2017 11:22:22 GMT
 
ETag:
"1d3-54f6609240717"
 
Content-Length:
467
 
Cache-Control:
max-age=0, no-cache, no-store, must-revalidate
 
Content-Type:
text/plain
 



#http://py4e-data.dr-chuck.net/comments_1546808.html    
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

nums_li = list()
# Retrieve all of the spam tags
spams = soup('span')
for spam in spams:
    st = str(spam)
    num = re.findall('[0-9]+',st)
    int_num=int(num[0])
    nums_li.append(int_num)
sum_n = 0
count =0
for n in nums_li:
    sum_n+=n
    count+=1

print("count",count)
print('sum',sum_n)

'''



#importing library(regx)
import re
#using urllib 
from urllib.request import urlopen
#import BeautifulSoup from bs4 file
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
#function to get link in 18th position

def get_link(url):
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    count=0
    tags = soup('a')
    for tag in tags:
        count+=1
        if count!=18: continue
        link=tag.get('href',None)
    return link
# function to loop  7 times
def find_link():
    links_list = list()
    times=6
    while True:
            url = input('Enter_')
            l=get_link(url)
            break
    while times>0:
        times-=1
        l=get_link(l)
        links_list.append(l)
    return links_list
    
    
l_l=find_link()
new_string=str(l_l[-1])
result_ = re.findall('by_([^.]+)',new_string)
string_result = str(result_[0])
print(string_result)

#Enter_http://py4e-data.dr-chuck.net/known_by_Katherine.html
#Tammie

