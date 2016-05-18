# -*- coding:UTF-8 -*-
# 
#  Created by WzxJinag
# 
#  https://github.com/Wzxhaha/wzx_Image_crawler
# 

import requests
import re
import time
import os

word = raw_input('Input keyword:')

url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word='+word+'&ct=201326592&v=flip'

html = requests.get(url).text

pic_url = re.findall('"objURL":"(.*?)",',html,re.S)

pic_folder = 'pictures'

if (os.path.exists(pic_folder)):
	pass
else:
	os.mkdir(pic_folder)

if (os.path.exists(pic_folder+'/'+'['+word+']')): 
	pass
else: 
	os.mkdir(pic_folder+'/'+'['+word+']')

i = 0
for each in pic_url:
	print each 					# web's path
	try:
		pic = requests.get(each, timeout=100)
	except requests.exceptions.ConnectionError:
		print '[Error] Current image can‘t download'
		continue
	
	index = each.rfind('.')
	img_type = str(each[index:])

	if (len(img_type) > 5):
		img_type = '.jpg'

	string = pic_folder+'/'+'['+word+']/'+str(time.time())+img_type
	print string     			# image's path
	fp = open(string,'wb')
	fp.write(pic.content)
	fp.close()
	i += 1
    