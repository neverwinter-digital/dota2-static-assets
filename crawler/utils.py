import urllib.request
import yaml
import os
import shutil
import json
import os.path


def download(url, filepath):
    """"download image from url, save it to filepath"""
    if os.path.exists(filepath):
        return
    try:
        u = urllib.request.urlopen(url)
        data = u.read()
        f = open(filepath, 'wb')
        f.write(data)
        f.close()
    except urllib.error.HTTPError as e:
        pass


def readYamlFile(path):
    with open(path, "r") as stream:
        items = yaml.load(stream)
    return items


def get_config():
    config = {'db': {}}
    config['apikey'] = os.environ.get('STEAM_API_KEY', 'A72DE7D7BE9870C8DA671D67941CCAA7')
    config['savepath'] = os.environ.get('SAVE_PATH', '../images')
    config['volumnPath'] = os.environ.get('VOLUMN_PATH', '/var/www')
    config['db']['name'] = os.environ.get('DB_NAME', 'neverwinter_dota2_development')
    config['db']['port'] = os.environ.get('DB_PORT', '5432')
    config['db']['user'] = os.environ.get('DB_USER', 'Gison')
    config['db']['password'] = os.environ.get('DB_PASSWORD', '')
    config['db']['host'] = os.environ.get('DB_URL', 'localhost')
    return config


def readJson(path):
    with open(path) as data_file:
        data = json.load(data_file)
    return data


def mkdir(path):
    path = path.strip()
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        return True
    else:
        return False


def listAlFiles(path):
    return os.listdir(path)


def buildSteamApiUrl(interface, method, apiKey):
    return "https://api.steampowered.com/{0}/{1}/v1/?key={2}&format=json".format(interface, method, apiKey)


def removeDir(path):
    shutil.rmtree(path, ignore_errors=True)
