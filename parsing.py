from bs4 import BeautifulSoup
import requests


def writeToFile(filename, list):
    with open(filename, "w") as file:
        for i in list:
            if len(i) > 1:
                file.write(i.strip().replace("\n\n", "") + "\n")


def getText(list):
    arr = []
    for i in list:
        arr.append(i.text)
    return arr


def parsing(url, domTeg, fileName):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "lxml")
    list = soup.find("div", {"id": "pagecontent"}).findAll(domTeg)
    info = getText(list)
    writeToFile(fileName, info)
