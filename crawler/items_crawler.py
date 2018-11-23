from utils import download, readYamlFile, mkdir, get_config
from progress.bar import Bar


class ItemCrawler(object):
    def __init__(self):
        self.config = get_config()
        self.savePath = config['savepath'] + '/items/'
        self.constantPath = "dota2-constant/active_yml/items.yml"

    def crawl(self):
        endpoint = "http://cdn.dota2.com/apps/dota2/images/items/"
        items = readYamlFile(self.constantPath)
        bar = Bar('Crawling items', max=len(items))
        for key, value in items.items():
            lgname = "{0}_lg.png".format(value)
            egname = "{0}_eg.png".format(value)
            download(endpoint + lgname, self.savePath + lgname)
            download(endpoint + egname, self.savePath + egname)
            bar.next()
        bar.finish()


if __name__ == '__main__':
    config = get_config()
    savePath = "{0}/items/".format(config["savepath"])
    mkdir(savePath)
    crawler = ItemCrawler()
    crawler.crawl()
