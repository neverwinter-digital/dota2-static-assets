from utils import download, readYamlFile, mkdir, getConfig
from progress.bar import Bar


def crawl(items, savePath):
    endpoint = "http://cdn.dota2.com/apps/dota2/images/heroes/"
    bar = Bar('Processing', max=len(items))
    for key, value in items.iteritems():
        # Type
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
    savePath = "{0}/heros/".format(config["output"]["path"])
    mkdir(savePath)
    crawl(readYamlFile("model/heros.yaml"), savePath)
