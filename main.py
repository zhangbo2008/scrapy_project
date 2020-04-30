'''
zhuyanshu

'''
import shutil ,os

# 每一次爬虫先闪了旧的文件夹output,省的每次都手动删,麻烦.
if os.path.exists('output'):
    shutil.rmtree('output')


import os,sys
# os.system("scrapy crawl dmoz")  # 爬取https://blog.scrapinghub.com/
# os.system("scrapy crawl dmoz2")  # 爬取https://www.51voa.com/Bilingual_News_1.html
# os.system("scrapy crawl dmoz3")  # 爬取 https://www.51test.net/yyzy/syxw/
# os.system("scrapy crawl dmoz4")  # 爬取 http://www.kekenet.com/read/news/
os.system("scrapy crawl dmoz5")  # 爬取 http://www.171english.cn/news/


'''
这个框架比较坑的一点就是,预处理需要都跑.
所以多个爬虫机器人放在同一个项目中,初始化会都初始化,可能会影响速度.
'''




