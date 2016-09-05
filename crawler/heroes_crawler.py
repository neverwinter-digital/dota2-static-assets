from utils import download, readYamlFile, mkdir, getConfig
from progress.bar import Bar

class HeroCrawler(object):
    def __init__(self):
        self.config = getConfig()
        self.savePath = config['savepath'] + '/heroes/'
        self.constantPath = "dota2-constant/yml/heroes.yml"

    def crawl(self):
        endpoint = "http://cdn.dota2.com/apps/dota2/images/heroes/"
        heros = readYamlFile(self.constantPath)
        bar = Bar('Crawling heroes', max=len(heros))
        for key, value in heros.iteritems():
            full = value + "_full.png"
            lg = value + "_lg.png"
            sb = value + "_sb.png"
            vert = value + "_vert.jpg"
            download(endpoint + full, savePath + full)
            download(endpoint + lg, savePath + lg)
            download(endpoint + sb, savePath + sb)
            download(endpoint + vert, savePath + vert)
            bar.next()
        bar.finish()

if __name__ == '__main__':
    config = getConfig()
    savePath = "{0}/heroes/".format(config["savepath"])
    mkdir(savePath)
    crawler = HeroCrawler()
    crawler.crawl()
