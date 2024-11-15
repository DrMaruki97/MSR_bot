import webbrowser as wb
import pyautogui as msk
import requests as req
import random as rn 
import string as str
import time as t

word_list = req.get('https://www.mit.edu/~ecprice/wordlist.10000').text.split('\n')

edge = wb.get('windows-default')
edge.open('https://www.bing.com',1)
x,y = msk.size()
msk.moveTo(x/(1920/663),y/(1080/339),1.5)
msk.click()
msk.write(rn.choice(word_list),interval=0.15)
msk.press('enter')
nth_search = (x/(1920/660),y/(1080/186))
t.sleep(5)
msk.moveTo(nth_search[0],nth_search[1],1.5)
for i in range(29):
    if i > 1:
        msk.press('backspace')
    msk.write(rn.choice(word_list),interval=0.15)
    msk.press('enter')
    t.sleep(5)
