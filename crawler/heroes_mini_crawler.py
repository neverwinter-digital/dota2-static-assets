from utils import download, readYamlFile, mkdir, get_config
from progress.bar import Bar


class HeroesMiniCrawler:
    """
    Download mini map hero images from Trackdota
    """
    def __init__(self):
        self.config = get_config()
        self.savePath = config['savepath'] + '/mini_heroes/'
        self.constantPath = "dota2-constant/yml_min/heroes.yml"

    def crawl(self):
        endpoint = "https://www.trackdota.com/static/heroes/png_o/32/"
        heroes = readYamlFile(self.constantPath)
        bar = Bar('Crawling heroes', max=len(heroes))
        for key, value in heroes.items():
            mini = "{0}.png".format(key)
            name = "{0}_mini.png".format(value)
            download(endpoint + mini, savePath + name)
            bar.next()
        bar.finish()


if __name__ == '__main__':
    config = get_config()
    savePath = "{0}/mini_heroes/".format(config["savepath"])
    mkdir(savePath)
    crawler = HeroesMiniCrawler()
    crawler.crawl()
