import requests
from bs4 import BeautifulSoup
from model import Card
import csv


def parser():
    cookies = {
        '__vt': 'xbKeiVvyVa3IupvqABQCCQPEFUluRFmojcP0P3EgGijZPlIz7soonA5aTOP1msD1nAeidleNo7zQ6gpB7xmBzB-Qwmu4EfTppPwa4K6BuZPsxYzNL-oa_4irIx7wNyae8pOI-reC7jz45cRpipaBFjBYJg',
        'OptanonConsent': 'isGpcEnabled=0&datestamp=Thu+Oct+19+2023+19%3A55%3A13+GMT%2B0300+(%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%2C+%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%BE%D0%B5+%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)&version=202209.1.0&isIABGlobal=false&hosts=&consentId=cd2be580-ffcd-446c-a0cf-c6caf6565b7d&interactionCount=1&landingPath=https%3A%2F%2Fwww.tripadvisor.ru%2FAttractions-g298484-Activities-a_allAttractions.true-Moscow_Central_Russia.html&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1',
        'TASession': 'V2ID.045962714FC1487083E53937C8585642*SQ.4*LS.Attractions*HS.recommended*ES.popularity*DS.5*SAS.popularity*FPS.oldFirst*FA.1*DF.0*TRA.true*LD.298484*EAU._',
        'TATrkConsent': 'eyJvdXQiOiIiLCJpbiI6IkFMTCJ9',
        'datadome': 'RUK2YTzJlJLqYQC08Xv6JbHd~dO3K6jNUPBMttaiJuu4CNluARNfBUDlBkAmev0HTAZ3gkjA7igDMa0rpg_YEsuFGBLzjXOFa~kznEEzCM8ooIQoP0gMklfyjZ9s3lhz',
        'TAUD': 'LA-1697734454014-1*RDD-1-2023_10_20*ARC-3*LG-56503-2.1.F.*LD-56504-.....',
        'PAC': 'ALhynkBP-cEA7UFssFWsk00eEbQ6Vt7UJkqqE7VjHlcjm_vbQlNsznomrXgDwx6EbRazmklqb_H2Hq-lBdCwcpezAabcr1ovoG3AU3Zb-uG5-npB8kms9JUkiaVnvh1mMtehLYUkk0UsHFxu5sBiGdeiydkcd2YL2yA-LKNZP9Sli3s79nMZFoRitsuJSrnEzGSk4L3wsvyO3h9r0U-ifNA5gd9mgIVrx8a3aNHCPfaV',
        'ServerPool': 'A',
        'TATravelInfo': 'V2*A.2*MG.-1*HP.2*FL.3*RS.1',
        'TAUnique': '%1%enc%3AJ3nSFJI1onSXS47kGeRaLXfrq6ZJXv8WSJ4TfOmTEoI2jHwltRJPGQ%3D%3D',
        'PMC': 'V2*MS.64*MD.20231019*LD.20231019',
        'TADCID': '-1vII8FcIpWNcMbQABQCCKy0j55CTpGVsECjuwJMq3j7YxVLu1MTCNZEIrp22V-ROqCuiEK66lXUaKHZjql1uP89Ipm1w5DIojY',
        'TART': '%1%enc%3Al0uO5BnkWi2ysHBCn%2Bjf0ELP3fLOfOXy7yZfJcdGH%2BIYYg8AqLinCrYQG0rMel3O4ieoPdYMDDY%3D',
        'TASSK': 'enc%3AAPnyI91wCJpZddkm%2F8Iw2NfAAOJzdWmhI28MJTVmlzxyKTg1Qyx7ZiUWuhOtRA9eqFYIoOg2WwVLUdeCaC45BACc51JsVJcsn%2B5nq9mQ%2B%2BteS3FGvXXJbPCe1lJaMzeXeQ%3D%3D',
        'TASameSite': '1',
    }

    headers = {
        # Requests sorts cookies= alphabetically
        # 'Cookie': '__vt=xbKeiVvyVa3IupvqABQCCQPEFUluRFmojcP0P3EgGijZPlIz7soonA5aTOP1msD1nAeidleNo7zQ6gpB7xmBzB-Qwmu4EfTppPwa4K6BuZPsxYzNL-oa_4irIx7wNyae8pOI-reC7jz45cRpipaBFjBYJg; OptanonConsent=isGpcEnabled=0&datestamp=Thu+Oct+19+2023+19%3A55%3A13+GMT%2B0300+(%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%2C+%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%BE%D0%B5+%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)&version=202209.1.0&isIABGlobal=false&hosts=&consentId=cd2be580-ffcd-446c-a0cf-c6caf6565b7d&interactionCount=1&landingPath=https%3A%2F%2Fwww.tripadvisor.ru%2FAttractions-g298484-Activities-a_allAttractions.true-Moscow_Central_Russia.html&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1; TASession=V2ID.045962714FC1487083E53937C8585642*SQ.4*LS.Attractions*HS.recommended*ES.popularity*DS.5*SAS.popularity*FPS.oldFirst*FA.1*DF.0*TRA.true*LD.298484*EAU._; TATrkConsent=eyJvdXQiOiIiLCJpbiI6IkFMTCJ9; datadome=RUK2YTzJlJLqYQC08Xv6JbHd~dO3K6jNUPBMttaiJuu4CNluARNfBUDlBkAmev0HTAZ3gkjA7igDMa0rpg_YEsuFGBLzjXOFa~kznEEzCM8ooIQoP0gMklfyjZ9s3lhz; TAUD=LA-1697734454014-1*RDD-1-2023_10_20*ARC-3*LG-56503-2.1.F.*LD-56504-.....; PAC=ALhynkBP-cEA7UFssFWsk00eEbQ6Vt7UJkqqE7VjHlcjm_vbQlNsznomrXgDwx6EbRazmklqb_H2Hq-lBdCwcpezAabcr1ovoG3AU3Zb-uG5-npB8kms9JUkiaVnvh1mMtehLYUkk0UsHFxu5sBiGdeiydkcd2YL2yA-LKNZP9Sli3s79nMZFoRitsuJSrnEzGSk4L3wsvyO3h9r0U-ifNA5gd9mgIVrx8a3aNHCPfaV; ServerPool=A; TATravelInfo=V2*A.2*MG.-1*HP.2*FL.3*RS.1; TAUnique=%1%enc%3AJ3nSFJI1onSXS47kGeRaLXfrq6ZJXv8WSJ4TfOmTEoI2jHwltRJPGQ%3D%3D; PMC=V2*MS.64*MD.20231019*LD.20231019; TADCID=-1vII8FcIpWNcMbQABQCCKy0j55CTpGVsECjuwJMq3j7YxVLu1MTCNZEIrp22V-ROqCuiEK66lXUaKHZjql1uP89Ipm1w5DIojY; TART=%1%enc%3Al0uO5BnkWi2ysHBCn%2Bjf0ELP3fLOfOXy7yZfJcdGH%2BIYYg8AqLinCrYQG0rMel3O4ieoPdYMDDY%3D; TASSK=enc%3AAPnyI91wCJpZddkm%2F8Iw2NfAAOJzdWmhI28MJTVmlzxyKTg1Qyx7ZiUWuhOtRA9eqFYIoOg2WwVLUdeCaC45BACc51JsVJcsn%2B5nq9mQ%2B%2BteS3FGvXXJbPCe1lJaMzeXeQ%3D%3D; TASameSite=1',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Host': 'www.tripadvisor.ru',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
        'Accept-Language': 'ru',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
    }

    create_csv()

    res = requests.get('https://www.tripadvisor.ru/Attractions-g298484-Activities-a_allAttractions.true-Moscow_Central_Russia.html', cookies=cookies, headers=headers)
    soup = BeautifulSoup(res.text, "html5lib")
    products = soup.find_all("a", class_="BUupS _R w _Z y M0 B0 Gm wSSLS")

    listCards = []
    id = 0

    for product in products:

        link = product.get("href")
        response = requests.get("https://www.tripadvisor.ru" + link, cookies=cookies, headers=headers)
        soup = BeautifulSoup(response.text, "html5lib")

        id += 1
        if soup.find("h1") is None:
            title = ""
        else:
            title = soup.find("h1").text

        if soup.find("span", class_="JguWG") is None:
            discription = ""
        else:
            discription = soup.find("span", class_="JguWG").text
        if soup.find("span", class_="eojVo") is None:
            category = ""
        else:
            category = soup.find("span", class_="eojVo").text

        if soup.find("div", class_="biGQs _P fiohW fOtGX") is None:
            location = ""
        else:
            location = soup.find("div", class_="biGQs _P fiohW fOtGX").text

        if soup.find("div", class_="biGQs _P pZUbB mtnKn KxBGd") is None:
            toGo = ""
        else:
            toGo = soup.find("div", class_="biGQs _P pZUbB mtnKn KxBGd").text


        if soup.find("span", class_="EFKKt") is None:
            timeToWork = ""
        else:
            timeToWork = soup.find("span", class_="EFKKt").text

        listCards.append(Card(id = id,
                              title = title,
                              link = link,
                              category = category,
                              discription = discription,
                              location = location,
                              toGo = toGo,
                              timeToWork = timeToWork))
        write_csv(listCards)
        listCards = []

        # print("Номер карточки: " + str(id))
        # print("Название:" + title)
        # print("Ссылка: https://www.tripadvisor.ru" + link)
        # print("Категория: " + category)
        # print("Описание: " + discription)
        # print(location)
        # print("Откуда можно добраться: "+ toGo)
        # print("Время работы: " + timeToWork)
        # print('')


    pageNum = 0

    while 1 > 0:

        count = 30
        pageNum += 30

        while count != 0:


            res = requests.get('https://www.tripadvisor.ru/Attractions-g298484-Activities-oa'+ str(pageNum) + '-Moscow_Central_Russia.html', cookies=cookies, headers=headers)
            soup = BeautifulSoup(res.text, "html5lib")
            products = soup.find_all("a", class_="BUupS _R w _Z y M0 B0 Gm wSSLS")

            for product in products:
                link = product.get("href")
                response = requests.get("https://www.tripadvisor.ru"+link, cookies=cookies, headers=headers)
                soup = BeautifulSoup(response.text, "html5lib")

                id += 1

                if soup.find("h1") is None:
                    title = ""
                else:
                    title = soup.find("h1").text

                if soup.find("span", class_="JguWG") is None:
                    discription = ""
                else:
                    discription = soup.find("span", class_="JguWG").text
                if soup.find("span", class_="eojVo") is None:
                    category = ""
                else:
                    category = soup.find("span", class_="eojVo").text

                if soup.find("div", class_="biGQs _P fiohW fOtGX") is None:
                    location = ""
                else:
                    location = soup.find("div", class_="biGQs _P fiohW fOtGX").text

                if soup.find("div", class_="biGQs _P pZUbB mtnKn KxBGd") is None:
                    toGo = ""
                else:
                    toGo = soup.find("div", class_="biGQs _P pZUbB mtnKn KxBGd").text

                if soup.find("span", class_="EFKKt") is None:
                    timeToWork = ""
                else:
                    timeToWork = soup.find("span", class_="EFKKt").text

                listCards.append(Card(id=id,
                                      title=title,
                                      link=link,
                                      category=category,
                                      discription=discription,
                                      location=location,
                                      toGo=toGo,
                                      timeToWork=timeToWork))

                write_csv(listCards)
                listCards = []
                count -= 1

                print("Номер карточки: " + str(id))
                print("Название:" + title)
                # print("Ссылка: https://www.tripadvisor.ru" + link)
                # print("Описание: " + discription)
                # print(location)
                # print("Откуда можно добраться: " + toGo)
                # print("Время работы: " + timeToWork)
                print(count, pageNum)
                print('')






def create_csv():
    with open(f"cards.csv", mode= "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            "ID карточки",
            "Название",
            "Ссылка на источник",
            "Категория",
            "Описание",
            "Район/Квартал",
            "Откуда можно добраться",
            "Время работы"
        ])

def write_csv(cards: list):
    with open(f"cards.csv", mode= "a", newline="") as file:
        writer = csv.writer(file)
        for card in cards:
            writer.writerow([
                card.id,
                card.title,
                card.link,
                card.category,
                card.discription,
                card.location,
                card.toGo,
                card.timeToWork
            ])


if __name__ == "__main__":
    parser()


