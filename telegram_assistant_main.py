"""
We're going to search for the music(done)
Download track as mp3-file(done)
And upload it to Telegram channel(done)
Let's Go! :)
12.08.2018 @ 4:03
All done!
09.09.2018 @ 18:09
"""

import re
import requests
import telebot
import wget
from bs4 import BeautifulSoup
from pyshorteners import Shortener
from requests.packages.urllib3 import HTTPConnectionPool


banner = '''
--------------------------------------------------------------------------------------------------
  __  __                 _                                   _         _                     _    
 |  \/  |               (_)              /\                 (_)       | |                   | |   
 | \  / |  _   _   ___   _    ___       /  \     ___   ___   _   ___  | |_    __ _   _ __   | |_  
 | |\/| | | | | | / __| | |  / __|     / /\ \   / __| / __| | | / __| | __|  / _` | | '_ \  | __| 
 | |  | | | |_| | \__ \ | | | (__     / ____ \  \__ \ \__ \ | | \__ \ | |_  | (_| | | | | | | |_  
 |_|  |_|  \__,_| |___/ |_|  \___|   /_/    \_\ |___/ |___/ |_| |___/  \__|  \__,_| |_| |_|  \__| 
         FOR TELEGRAM           v.1.01b         by Viacheslav Vorotilin aka "music meister"      
--------------------------------------------------------------------------------------------------
'''
print(banner + '\n')

artistName = input('Artist: ')  # Variable for Artist Name
songName = input('Name: ')      # Variable for Song Name
mixName = input('Mix Name: ')   # Variable for Remix Name
blankInput = str()              # String Variable for Blank Input

'''
plusInput = '+'                 # Variable for a Plus [+]
underInput = '_'                # Variable for an Underscore [_]
'''

spaceInput = ' '                # Variable for a Space [ ]
hyphenInput = '-'               # Variable for a Hyphen [-]
codeOpen = '<code>'             # Variable for Text-Formatting
codeClose = '</code>'           # Variable for Text-Formatting
boldOpen = '<b>'                # Variable for Text-Formatting
boldClose = '</b>'              # Variable for Text-Formatting

if mixName == blankInput:
    query = (artistName + spaceInput + songName)
elif songName == blankInput:
    query = (artistName + spaceInput + mixName)
elif artistName == blankInput:
    query = (songName + spaceInput + mixName)
else:
    query = (artistName + spaceInput + songName + spaceInput + mixName)

if mixName == blankInput:
    text = (codeOpen + artistName + spaceInput + hyphenInput + spaceInput + songName + codeClose)
else:
    text = (codeOpen + artistName + spaceInput + hyphenInput + spaceInput + songName
            + spaceInput + '(' + mixName + ')' + codeClose)

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) \
    Gecko/20100101 Firefox/45.0'
}

url = 'https://mp3cc.biz/search/f/' + query + '/'

with open('parse.txt', 'wb') as lf:
    response = requests.get(url, headers=headers, stream=True)
    lf.write(response.content)
    lf.close()

with open('parse.txt', 'r', encoding='UTF-8') as p:
    s = BeautifulSoup(p, 'html.parser')
    link = s.find(href=re.compile('download'))
    print(type(link))
    get_link = link.get('href')
try:
    shorten = Shortener('Tinyurl')
except HTTPConnectionPool(host='tinyurl.com', port=80) as e:
  raise requests.exceptions.ReadTimeout
  pass
    shrink_url = shorten.short(get_link)
    print('Downloading: ' + '(' + artistName + spaceInput + hyphenInput + spaceInput + songName + ')' +
          ' via Short URL => ' + shrink_url + '\n')
try:
    mp3 = wget.download(shrink_url, out='/tmp/')
    print(mp3 + ' Downloaded!' + '\n')
    chat_id = '@testing_now'
    token = '658217975:AAEmtIoL3SX-Cf8budKCQHpd99BDNlEMnRg'
    tb = telebot.TeleBot(token)
    user = tb.get_me()
    print(user)
    audio = open(mp3, 'rb')
    print('Uploading File to Telegram Channel...\n')
    tb.send_audio(chat_id, audio)
except:
  pass
    print('File Uploaded!\n')
    tb.send_message(chat_id, text)
    print("Found: " + artistName + hyphenInput + songName)
    print("Downloaded: " + artistName + hyphenInput + songName)
    print("Uploaded to: " + chat_id)

import delete_mp3
