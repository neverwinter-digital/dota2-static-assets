import urllib
import yaml
import os
import shutil
import json


def download(url, filepath):
    u = urllib.urlopen(url)
    data = u.read()
    f = open(filepath, 'wb')
    f.write(data)
    f.close()


def readYamlFile(path):
    with open(path, "r") as stream:
        items = yaml.load(stream)
    return items


def getConfig():
    return readYamlFile("./config.yaml")


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


def removeDir(path):
    shutil.rmtree(path, ignore_errors=True)
