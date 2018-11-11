#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
__time__ = 2018/11/11 13:45
__author__ = Kexin Xu
__desc__ = 输入title中的网址,对网址内容进行解析获取每一页上的图片下载地址
"""

import time
from bs4 import Tag

from get_title_urls import GetTitleUrls

class GetPicUrlInPages(GetTitleUrls):
    """输入title中的网址,对网址内容进行解析获取每一页上的图片下载地址
    
    """

    def __init__(self):
        """初始化父类__init__方法
        
        """
        super(GetPicUrlInPages, self).__init__()
        # self.get_pic_url_and_info(soup)

    def get_pic_url_and_info(self, soup):
        """获取图片,以及图片下方的说明作为图片名称
        
        Parameters
        ----------
        soup : bs4.BeautifulSoup
            BeautifulSoup对象
        
        Returns
        -------
        dict
            pic_explain -> title说明
            图片网址 -> 图片说明
        """

        mid_res_d = {}
        # 获取当前soup的页码
        page_num = soup.find(class_='active').text

        # 获取第一页的整体说明 -> 第一页的第一个P元素
        if page_num == '1':
            mid_res_d['pic_explain'] = ''.join(soup.find('p').text.split()) # 去除\r\n\t等占位符
        
        # 获取所有图片网址的元素
        # [<img alt="..." src="..."/>]
        all_img_eles = soup.find_all(self.img_has_alt)

        for n, img_ele in enumerate(all_img_eles):
            # 获取img的父元素的兄弟元素(叔叔吗?)
            # 判断其是否为Tag元素,并尝试获取其内容作为名称
            # 如无Tag元素,则将其视为无说明,将None+时间+顺序作为名称
            # 无Tag元素的例子https://www.3dmgame.com/bagua/525_48.html
            for mid_img_explain in img_ele.parent.next_siblings:
                if isinstance(mid_img_explain, Tag) and mid_img_explain.span:
                    img_explain = ''.join(mid_img_explain.text.split())
                    break
            else:
                img_explain = "None_" + time.strftime('%Y%m%d_%H%M%S') + '_' + str(n)
                print(img_explain)
            print(page_num)

            mid_res_d[img_ele['src']] = img_explain

        return mid_res_d

    def img_has_alt(self, tag):
        """查找带有alt属性的img
        
        Parameters
        ----------
        tag : soup.find_all 自动传入
            元素名称
        
        Returns
        -------
        bool
            返回bool作为判断依据
        """

        return tag.has_attr('alt')

    def start(self):
        """仅作测试使用
        
        Returns
        -------
        dict
            pic_explain -> title说明
            图片网址 -> 图片说明
        """
        url = r'https://www.3dmgame.com/bagua/525.html'
        res_d = {}

        while url:
            soup = self.get_soup(url)
            res_d.update(self.get_pic_url_and_info(soup))
            self.sleep_time.sleep(3)
            url = self.get_next_page(soup)
            

        return res_d


if __name__ == '__main__':
    tp = GetPicUrlInPages().start()
    # print(tp)