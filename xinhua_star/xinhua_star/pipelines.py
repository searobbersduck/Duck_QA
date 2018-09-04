# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import os
from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals
import time

class XinhuaStarPipeline(object):
    def process_item(self, item, spider):
        return item

class xinhuastarToJsonPipeline(object):
    def __init__(self):
        self.buffer_list = []
        self.buffer_size_max = 100
        self.outdir = './xinhua_data_json'
        os.makedirs(self.outdir, exist_ok=True)
        self.outfile_cnt = 0
        self.outfile_name = 'file'
        dispatcher.connect(self.spider_closed, signals.spider_closed)

    def _store_data(self):
        outfile = os.path.join(self.outdir, '{}_{}'.format(self.outfile_name, self.outfile_cnt))
        with open(outfile, 'w') as f:
            f.write(json.dumps(self.buffer_list))
        self.buffer_list.clear()
        print(u'输出文件: \t' + outfile)
        self.outfile_cnt += 1

    def _store_data1(self):
        outfile = os.path.join(self.outdir, '{}_{}'.format(self.outfile_name, self.outfile_cnt))
        with open(outfile, 'w') as f:
            for info in self.buffer_list:
                f.write(info['title'])
                f.write('\t')
                f.write(info['datetime'])
                f.write('\t')
                f.write(info['content'])
                f.write('\n\n\n')
        self.buffer_list.clear()
        print(u'输出文件: \t' + outfile)
        self.outfile_cnt += 1


    def process_item(self, item, spider):
        # time.sleep(1)
        # print(item['title'])
        line = dict(item)
        self.buffer_list.append(line)
        if len(self.buffer_list) == self.buffer_size_max:
            self._store_data()

    def spider_closed(self, spider):
        self._store_data()

