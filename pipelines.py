# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os
import json
class TutorialPipeline(object):
    def process_item(self, item, spider):
        content=json.dumps(item['neirong'],ensure_ascii=False)
        print("开始写")
        if not os.path.exists('output'):
            os.mkdir('output')
        name='output/'+item['title'].split(r'/')[-1]+'.json'
        print(name,9348938493849384)
        with open(name,'w') as f :
             f.write(content)
