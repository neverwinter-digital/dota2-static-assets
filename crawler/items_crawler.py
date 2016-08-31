from utils import download, readYamlFile, mkdir, getConfig
from progress.bar import Bar


def crawl(items, savePath):
    endpoint = "http://cdn.dota2.com/apps/dota2/images/items/"
    bar = Bar('Processing', max=len(items))
    for key, value in items.iteritems():
        lgname = value + "_lg.png"
        egname = value + "_eg.png"
        download(endpoint + lgname, savePath + lgname)
        download(endpoint + egname, savePath + egname)
        bar.next()
    bar.finish()


if __name__ == '__main__':
    config = getConfig()
    savePath = "{0}/items/".format(config["output"]["path"])
    mkdir(savePath)
    crawl(readYamlFile("model/items.yaml"), savePath)
