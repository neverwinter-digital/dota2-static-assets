from utils import download, readYamlFile, mkdir, getConfig
from progress.bar import Bar


class AbilitiesCrawler(object):
    def __init__(self):
        self.config = getConfig()
        self.savePath = config['savepath'] + '/abilities/'
        self.constantPath = "dota2-constant/yml_min/abilities.yml"

    def crawl(self):
        endpoint = "http://cdn.dota2.com/apps/dota2/images/abilities/"
        items = readYamlFile(self.constantPath)
        bar = Bar('Crawling abilities', max=len(items))
        for key, value in items.items():
            smname = "{0}_sm.png".format(value)
            mdname = "{0}_md.png".format(value)
            lgname = "{0}_lg.png".format(value)
            download(endpoint + lgname, self.savePath + lgname)
            download(endpoint + smname, self.savePath + smname)
            download(endpoint + mdname, self.savePath + mdname)
            bar.next()
        bar.finish()


if __name__ == '__main__':
    config = getConfig()
    savePath = "{0}/abilities/".format(config["savepath"])
    mkdir(savePath)
    crawler = AbilitiesCrawler()
    crawler.crawl()
