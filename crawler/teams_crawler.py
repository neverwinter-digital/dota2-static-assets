from utils import buildSteamApiUrl, getConfig, mkdir
from progress.bar import Bar
import psycopg2
import urllib
import json


class TeamsCrawler(object):
    def __init__(self):
        self.config = getConfig()
        self.savePath = config['savepath'] + '/teams/'
        self.ugcApiUrl = buildSteamApiUrl('ISteamRemoteStorage', 'GetUGCFileDetails', config['apikey'])
        self.teamsApiUrl = buildSteamApiUrl('IDOTA2Match_570', 'GetTeamInfoByTeamID', config['apikey'])

    def crawl(self):
        teams = self.getTeamFromDb()
        bar = Bar('Crawling', max=len(teams))
        for team in teams:
            teamId = team[0]
            logoId = team[1]
            try:
                self.loadAndSaveImageToPath(self.getImageUrlByUgcId(logoId),
                                            self.savePath + '{0}_logo.png'.format(teamId))
                if team[2] != 0:
                    sponsorLogoId = team[2]
                    self.loadAndSaveImageToPath(self.getImageUrlByUgcId(sponsorLogoId),
                                                self.savePath + '{0}_sponsor.png'.format(teamId))
            except(RuntimeError, TypeError, NameError, ValueError):
                print "Failed to process team {0}\n".format(teamId)
            bar.next()
        bar.finish()

    def crawlByTeamId(self, teamId):
        res = self.getTeamInfoById(teamId)
        if res['result']['status'] != 1 or len(res['result']['teams']) == 0:
            return
        team = res['result']['teams'][0]
        logoId = team['logo']
        sponsorId = team['logo_sponsor']
        self.loadAndSaveImageToPath(self.getImageUrlByUgcId(logoId), self.savePath + '{0}_logo.png'.format(teamId))
        if sponsorId != "":
            self.loadAndSaveImageToPath(self.getImageUrlByUgcId(sponsorId),
                                        self.savePath + '{0}_sponsor.png'.format(teamId))

    def getTeamInfoById(self, teamId):
        url = self.teamsApiUrl + '&start_at_team_id={0}&teams_requested=1'.format(teamId)
        response = urllib.urlopen(url)
        res = json.loads(response.read())
        return res

    def getTeamFromDb(self):
        conn = psycopg2.connect("dbname={0} user={1} password={2} host={3} port={4}".format(config['db']['name'], config['db']['user'],
                                                                          config['db']['password'], config['db']['host'], config['db']['port']))
        cur = conn.cursor()
        cur.execute("SELECT id, logo_id, logo_sponsor_id FROM dota2_teams WHERE logo_id <> 0")
        data = cur.fetchall()
        cur.close()
        conn.close()
        return data

    def getImageUrlByUgcId(self, id):
        url = self.ugcApiUrl + '&ugcid={0}&appid=570'.format(id)
        response = urllib.urlopen(url)
        res = json.loads(response.read())
        if not 'data' in res:
            return
        imageUrl = res['data']['url']
        return imageUrl

    def loadAndSaveImageToPath(self, imageUrl, filepath):
        if not imageUrl is None:
            urllib.urlretrieve(imageUrl, filepath)


if __name__ == '__main__':
    config = getConfig()
    mkdir(config['savepath'] + '/teams') # create the output folder if not exists
    crawler = TeamsCrawler()
    crawler.crawl()
    # crawler.crawlByTeamId(15)
