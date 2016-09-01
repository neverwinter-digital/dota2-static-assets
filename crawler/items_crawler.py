from utils import download, readYamlFile, mkdir, getConfig
from progress.bar import Bar


class ItemCrawler(object):
    def __init__(self):
        self.config = getConfig()
        self.savePath = config['savepath'] + '/items/'
        self.constantPath = "dota2-constant/yml/items.yml"

    def crawl(self):
        endpoint = "http://cdn.dota2.com/apps/dota2/images/items/"
        items = readYamlFile(self.constantPath)
        bar = Bar('Crawling items', max=len(items))
        for key, value in items.iteritems():
            lgname = "{0}_lg.png".format(value)
            egname = "{0}_eg.png".format(value)
            download(endpoint + lgname, self.savePath + lgname)
            download(endpoint + egname, self.savePath + egname)
            bar.next()
        bar.finish()

if __name__ == '__main__':
    config = getConfig()
    savePath = "{0}/items/".format(config["savepath"])
    mkdir(savePath)
    crawler = ItemCrawler()
    crawler.crawl()
