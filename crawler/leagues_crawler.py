import json
import urllib
from utils import download, readJson, mkdir, getConfig
from progress.bar import Bar


def fetchIconFromCdn(leagueId, resourceUrl, savePath, type):
    cdnUrl = "http://cdn.dota2.com/apps/570/" + resourceUrl
    types = {
        0: "ticket",
        1: "ticket_large",
        2: "ingame",
    }
    download(cdnUrl, savePath + leagueId + "_" + types[type] + ".png")


def buildSteamApiUrl(interface, method, apiKey):
    return "https://api.steampowered.com/{0}/{1}/v1/?key={2}&format=json".format(interface, method, apiKey)


def crawl(items, savePath, apiKey):
    steamUrl = buildSteamApiUrl("IEconDOTA2_570", "GetItemIconPath", apiKey)
    bar = Bar('Processing', max=len(items))
    for key, value in items.iteritems():
        image = value['ticket'].split("/")[-1]
        for type in range(0, 3):
            response = urllib.urlopen(steamUrl + "&iconname={0}&icontype={1}".format(image, type))
            data = json.loads(response.read())
            if not 'error' in data['result']:
                imagePath = data['result']['path']
                fetchIconFromCdn(key, imagePath, savePath, type)
                bar.next()
    bar.finish()


if __name__ == '__main__':
    config = getConfig()
    apiKey =  config["api"]["key"]
    jsonSrouce = "https://raw.githubusercontent.com/dotabuff/d2vpkr/master/dota/scripts/items/leagues.json"
    jsonPath = "model/leagues.json"
    savePath = "{0}/leagues/".format(config["output"]["path"])
    download(jsonSrouce, jsonPath)
    mkdir(savePath)
    crawl(readJson(jsonPath), savePath, apiKey)
