# coding:utf8
from baike_spider import url_management, html_download, html_parser, html_output


class SpiderMain(object):
    def __init__(self):
        self.urls = url_management.UrlManager()
        self.downloader = html_download.HomeDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_output.HtmlOutputer()

    
    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            new_url = self.urls.get_new_url()
            print 'craw %d : %s' % (count, new_url)
            html_cont = self.downloader.download(new_url)
            new_urls, new_data = self.parser.parse(new_url, html_cont)
            self.urls.add_new_urls(new_urls)
            self.outputer.collect_data(new_data)
            
            if count ==1000:
                break
            count = count + 1
            
        self.outputer.output_html()

if  __name__ == "__main__":
    root_url = "http://baike.baidu.com/view/21087.htm"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)