import json
import urllib
from utils import listAlFiles, mkdir, getConfig, buildSteamApiUrl
from progress.bar import Bar
import vdf


class LeagueCrawler(object):
    def __init__(self, config):
        self.config = config
        self.savePath = config['savepath'] + '/leagues/'
        self.imageUrl = buildSteamApiUrl('IEconDOTA2_570', 'GetItemIconPath', config['apikey'])
        self.schemaUrl = buildSteamApiUrl('IEconItems_570', 'GetSchemaURL', config['apikey'])
        self.cdnUrl = "http://cdn.dota2.com/apps/570/"

    def crawl(self):
        self.downloadSchema()
        items = self.loadAndParseVdf()
        leagues = self.getAllLeagueResource(items)

        existingFiles = listAlFiles(self.config['volumnPath'] + '/leagues/')
        leagueIdSet = set()
        for filename in existingFiles:
            leagueIdSet.add(filename.split('_')[0])

        # Any league id in the leagueIdSet means we can ignore these leagues
        bar = Bar('Crawling Leagues', max=len(leagues))

        for key, value in leagues.iteritems():
            # skip already downloaded leagues
            if key in leagueIdSet:
                bar.next()
                continue

            # First find out the valid url to use
            resourceId = value[0]
            if len(value) > 1:
                resourceId = self.getValidResourceId(value)

            if resourceId is None:
                bar.next()
                continue

            for type in range(0, 3):
                response = urllib.urlopen("{0}&iconname={1}&icontype={2}".format(self.imageUrl, resourceId, type))
                data = json.loads(response.read())
                if not 'error' in data['result']:
                    imagePath = data['result']['path']
                    self.fetchIconFromCdn(key, imagePath, type)
            bar.next()
        bar.finish()

    def getValidResourceId(self, list):
        for id in list:
            response = urllib.urlopen("{0}&iconname={1}".format(self.imageUrl, id))
            data = json.loads(response.read())
            if 'error' in data['result']:
                continue
            if 'path' in data['result']:
                return id
        return None

    def getAllLeagueResource(self, items):
        # leagues : {
        #   league_id : [possible_resource_id]
        # }
        leagues = {}
        for key, value in items.iteritems():
            if 'prefab' in value and value['prefab'] == 'league':
                resourcePath = value['image_inventory']
                if 'tool' in value and 'usage' in value['tool'] and 'league_id' in value['tool']['usage']:
                    leagueId = value['tool']['usage']['league_id']
                    resourceId = resourcePath.split("/")[-1]
                    if leagueId not in leagues:
                        leagues[leagueId] = [resourceId]
                    else:
                        leagues[leagueId].append(resourceId)
        return leagues

    def loadAndParseVdf(self):
        d = vdf.load(open('resources/items_game.txt'))
        items = d['items_game']['items']
        return items

    def downloadSchema(self):
        response = urllib.urlopen(self.schemaUrl)
        res = json.loads(response.read())
        imageUrl = res['result']['items_game_url']
        urllib.urlretrieve(imageUrl, 'resources/items_game.txt')

    def fetchIconFromCdn(self, leagueId, resourceUrl, type):
        cdnUrl = self.cdnUrl + resourceUrl
        types = {
            0: "ticket",
            1: "ticket_large",
            2: "ingame",
        }
        urllib.urlretrieve(cdnUrl, "{0}{1}_{2}.png".format(self.savePath, leagueId, types[type]))


if __name__ == '__main__':
    config = getConfig()
    mkdir(config['savepath'] + '/leagues')
    crawler = LeagueCrawler(config)
    crawler.crawl()
