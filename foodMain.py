import requests
from bs4 import BeautifulSoup
from modelFood import Food
import csv


def parser():
    import requests

    cookies = {
        '__vt': 'hjnftwy7erx_l4jQABQCCQPEFUluRFmojcP0P3EgGijuTLa_megRh4c6s092BEVBzMQI1rwmZEaehv4IXSG9B62k7EyLqAF0hHFItvE65cBztXwpncg2OV6nhsB5hmlCV9XoYJkzlJb_JMBJ-1gYHGnS8A',
        'TASID': '64858CE342CD4361A9641C134C027D45',
        'TASession': 'V2ID.64858CE342CD4361A9641C134C027D45*SQ.151*LS.FindRestaurants*HS.recommended*ES.popularity*DS.5*SAS.popularity*FPS.oldFirst*LF.ru*FA.1*DF.0*TRA.true*LD.8429267*EAU._',
        'SRT': 'TART_SYNC',
        'TAUD': 'LA-1697734454014-1*RDD-1-2023_10_20*ARC-3*FO-275100465-MOW*FD-275100466-MOW*HDD-320504782-2023_11_05.2023_11_06*LD-325094214-2023.11.5.2023.11.6*LG-325094216-2.1.F.',
        'datadome': 'IcbmnnU2yepS0NmrmoWhLLxCRQq6PpbnEyWYMovARIiWIT_wPTlYgQICGQ7I7KAcnqsahOeU2zfu9CiHaqNCJUvvgIVtk5yvWrxpFKIAwaF5N6bu0FBI_~4WVopP1ulm',
        'OptanonConsent': 'isGpcEnabled=0&datestamp=Mon+Oct+23+2023+14%3A12%3A27+GMT%2B0300+(%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%2C+%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%BE%D0%B5+%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)&version=202209.1.0&isIABGlobal=false&hosts=&consentId=cd2be580-ffcd-446c-a0cf-c6caf6565b7d&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&AwaitingReconsent=false',
        'TATrkConsent': 'eyJvdXQiOiIiLCJpbiI6IkFMTCJ9',
        'roybatty': 'TNI1625!AC71uTh0MnKjHHbB0itSrmMfcUrq4bMHuCkY8BTWNw5u0WIbiC1qAwEYfxj%2F3FA7%2FGpBN1CCSTCGalYBf5X6PZ0G8soZI2UQRPCCOn0sJGYsphehaq%2BPbstUTmTJ2Wzm5XueOVImfoj1fuYAc%2Bp4sfGeQZiCmsqcz6VvFOLIEUFv%2C1',
        'TAReturnTo': '%1%%2FRestaurant_Review-g298484-d8429267-Reviews-Sabor_de_la_Vida_Restaurant-Moscow_Central_Russia.html',
        'PAC': 'AMvuqa4lbTDeG_GxdkCwJjAzBDMD8xk0aPG3uMZ96hs-0_M7L0zJV2q8IhHUn9BZ4jvoDPrEJ05w_cnR226vOxNMfthbPTEmXy_uAx2GhYGRwQbTSH3OseGt7WM_UjPrjPABdX7qsHLT9GLawWDX-6YCxP1UIUwZNNbCkBGp1Qgd',
        'TASameSite': '1',
        'VRMCID': '%1%V1*id.10568*llp.%2F*e.1698660179794',
        'TATravelInfo': 'V2*AY.2023*AM.11*AD.5*DY.2023*DM.11*DD.6*A.2*MG.-1*HP.2*FL.3*DSM.1698054958809*RS.1',
        'PMC': 'V2*MS.64*MD.20231019*LD.20231023',
        'TADCID': 'og2Q3k5lNc6nWm-6ABQCCKy0j55CTpGVsECjuwJMq3kLroX8yK-z8PRZXSc_pUwTlieZ9coxcJ5rorPah0ADHnfvqnnUOH0HUFI',
        'ServerPool': 'A',
        'TAUnique': '%1%enc%3AJ3nSFJI1onSXS47kGeRaLXfrq6ZJXv8WSJ4TfOmTEoI2jHwltRJPGQ%3D%3D',
        'TART': '%1%enc%3Al0uO5BnkWi2ysHBCn%2Bjf0ELP3fLOfOXy7yZfJcdGH%2BIYYg8AqLinCrYQG0rMel3O4ieoPdYMDDY%3D',
        'TASSK': 'enc%3AAPnyI91wCJpZddkm%2F8Iw2NfAAOJzdWmhI28MJTVmlzxyKTg1Qyx7ZiUWuhOtRA9eqFYIoOg2WwVLUdeCaC45BACc51JsVJcsn%2B5nq9mQ%2B%2BteS3FGvXXJbPCe1lJaMzeXeQ%3D%3D',
    }

    headers = {
        # Requests sorts cookies= alphabetically
        # 'Cookie': '__vt=hjnftwy7erx_l4jQABQCCQPEFUluRFmojcP0P3EgGijuTLa_megRh4c6s092BEVBzMQI1rwmZEaehv4IXSG9B62k7EyLqAF0hHFItvE65cBztXwpncg2OV6nhsB5hmlCV9XoYJkzlJb_JMBJ-1gYHGnS8A; TASID=64858CE342CD4361A9641C134C027D45; TASession=V2ID.64858CE342CD4361A9641C134C027D45*SQ.151*LS.FindRestaurants*HS.recommended*ES.popularity*DS.5*SAS.popularity*FPS.oldFirst*LF.ru*FA.1*DF.0*TRA.true*LD.8429267*EAU._; SRT=TART_SYNC; TAUD=LA-1697734454014-1*RDD-1-2023_10_20*ARC-3*FO-275100465-MOW*FD-275100466-MOW*HDD-320504782-2023_11_05.2023_11_06*LD-325094214-2023.11.5.2023.11.6*LG-325094216-2.1.F.; datadome=IcbmnnU2yepS0NmrmoWhLLxCRQq6PpbnEyWYMovARIiWIT_wPTlYgQICGQ7I7KAcnqsahOeU2zfu9CiHaqNCJUvvgIVtk5yvWrxpFKIAwaF5N6bu0FBI_~4WVopP1ulm; OptanonConsent=isGpcEnabled=0&datestamp=Mon+Oct+23+2023+14%3A12%3A27+GMT%2B0300+(%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%2C+%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%BE%D0%B5+%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)&version=202209.1.0&isIABGlobal=false&hosts=&consentId=cd2be580-ffcd-446c-a0cf-c6caf6565b7d&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&AwaitingReconsent=false; TATrkConsent=eyJvdXQiOiIiLCJpbiI6IkFMTCJ9; roybatty=TNI1625!AC71uTh0MnKjHHbB0itSrmMfcUrq4bMHuCkY8BTWNw5u0WIbiC1qAwEYfxj%2F3FA7%2FGpBN1CCSTCGalYBf5X6PZ0G8soZI2UQRPCCOn0sJGYsphehaq%2BPbstUTmTJ2Wzm5XueOVImfoj1fuYAc%2Bp4sfGeQZiCmsqcz6VvFOLIEUFv%2C1; TAReturnTo=%1%%2FRestaurant_Review-g298484-d8429267-Reviews-Sabor_de_la_Vida_Restaurant-Moscow_Central_Russia.html; PAC=AMvuqa4lbTDeG_GxdkCwJjAzBDMD8xk0aPG3uMZ96hs-0_M7L0zJV2q8IhHUn9BZ4jvoDPrEJ05w_cnR226vOxNMfthbPTEmXy_uAx2GhYGRwQbTSH3OseGt7WM_UjPrjPABdX7qsHLT9GLawWDX-6YCxP1UIUwZNNbCkBGp1Qgd; TASameSite=1; VRMCID=%1%V1*id.10568*llp.%2F*e.1698660179794; TATravelInfo=V2*AY.2023*AM.11*AD.5*DY.2023*DM.11*DD.6*A.2*MG.-1*HP.2*FL.3*DSM.1698054958809*RS.1; PMC=V2*MS.64*MD.20231019*LD.20231023; TADCID=og2Q3k5lNc6nWm-6ABQCCKy0j55CTpGVsECjuwJMq3kLroX8yK-z8PRZXSc_pUwTlieZ9coxcJ5rorPah0ADHnfvqnnUOH0HUFI; ServerPool=A; TAUnique=%1%enc%3AJ3nSFJI1onSXS47kGeRaLXfrq6ZJXv8WSJ4TfOmTEoI2jHwltRJPGQ%3D%3D; TART=%1%enc%3Al0uO5BnkWi2ysHBCn%2Bjf0ELP3fLOfOXy7yZfJcdGH%2BIYYg8AqLinCrYQG0rMel3O4ieoPdYMDDY%3D; TASSK=enc%3AAPnyI91wCJpZddkm%2F8Iw2NfAAOJzdWmhI28MJTVmlzxyKTg1Qyx7ZiUWuhOtRA9eqFYIoOg2WwVLUdeCaC45BACc51JsVJcsn%2B5nq9mQ%2B%2BteS3FGvXXJbPCe1lJaMzeXeQ%3D%3D',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Host': 'www.tripadvisor.ru',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
        'Accept-Language': 'ru',
        'Referer': 'https://www.tripadvisor.ru/',
        'Connection': 'keep-alive',
    }

    params = {
        'geo': '298484',
        'offset': '60',
        'establishmentTypes': '10591',
        'broadened': 'false',
    }

    create_csv()

    res = requests.get('https://www.tripadvisor.ru/Restaurants-g298484-Moscow_Central_Russia.html', cookies=cookies,
                            headers=headers)
    soup = BeautifulSoup(res.text, "html5lib")
    products = soup.find_all("a", class_="aWhIG _S _Z")

    listCards = []
    id = 600


    # for product in products:
    #
    #     link = product.get("href")
    #
    #     response = requests.get("https://www.tripadvisor.ru" + link, cookies=cookies, headers=headers)
    #     soup = BeautifulSoup(response.text, "html5lib")
    #
    #     id += 1
    #     if soup.find("h1") is None:
    #         title = ""
    #     else:
    #         title = soup.find("h1").text
    #
    #     if soup.find("a", href="#MAPVIEW") is None:
    #         address = ""
    #     else:
    #         address = soup.find("a", href="#MAPVIEW").text
    #
    #     if soup.find("span", class_="yEWoV OkcwQ") is None:
    #         location = ""
    #     else:
    #         location = soup.find("span", class_="yEWoV OkcwQ").text
    #
    #     if soup.find("div", class_="SrqKb") is None:
    #         priceRange = ""
    #     else:
    #         if "руб" in soup.find("div", class_="SrqKb").text:
    #             priceRange = soup.find("div", class_="SrqKb").text
    #         else:
    #             priceRange = ""
    #
    #
    #     if soup.find("span", class_="KscYp") is None:
    #         time = ""
    #     else:
    #         timeToWork = soup.find("span", class_="KscYp")
    #         time = timeToWork.findNext().text
    #
    #
    #     if soup.find("span", class_="yEWoV") is None:
    #         number = ""
    #     else:
    #         phoneNum = soup.find("span", class_="ui_icon phone XMrSj")
    #         number = phoneNum.findNext().text
    #
    #     # listCards.append(Food(id=id,
    #     #                       title=title,
    #     #                       link=link,
    #     #                       address=address,
    #     #                       location=location,
    #     #                       priceRange=priceRange,
    #     #                       time=time,
    #     #                       number=number))
    #
    #     listCards.append(Food(id=id,
    #                           title = title,
    #                           link = "https://www.tripadvisor.ru"+link,
    #                           address = address,
    #                           location = location,
    #                           priceRange = priceRange,
    #                           time = time,
    #                           number = number))
    #     write_csv(listCards)
    #     listCards = []
    #
    #     print("Номер карточки: " + str(id))
    #     print("Название:" + title)
    #     print("Ссылка: https://www.tripadvisor.ru" + link)
    #     print(address)
    #     print(location)
    #     print(priceRange)
    #     print(time)
    #     print(number)
    #     print('')
    #
    #
    pageNum = 570

    while 1 > 0:

        count = 30
        pageNum += 30

        while count != 0:

            res = requests.get('https://www.tripadvisor.ru/FindRestaurants?geo=298484&offset='+ str(pageNum) + '&establishmentTypes=10591&broadened=false', cookies=cookies,
                            headers=headers)

            soup = BeautifulSoup(res.text, "html5lib")
            products = soup.find_all("a", class_="aWhIG _S _Z")
            for product in products:
                link = product.get("href")
                response = requests.get("https://www.tripadvisor.ru"+link, cookies=cookies, headers=headers)
                soup = BeautifulSoup(response.text, "html5lib")

                id += 1

                if soup.find("h1") is None:
                    title = ""
                else:
                    title = soup.find("h1").text




                if soup.find("a", href="#MAPVIEW") is None:
                    address = ""
                else:
                    address = soup.find("a", href="#MAPVIEW").text




                if soup.find("span", class_="yEWoV OkcwQ") is None:
                    location = ""
                else:
                    location = soup.find("span", class_="yEWoV OkcwQ").text




                if soup.find("div", class_="SrqKb") is None:
                    priceRange = ""
                else:
                    if "руб" in soup.find("div", class_="SrqKb").text:
                        priceRange = soup.find("div", class_="SrqKb").text
                    else:
                        priceRange = ""




                if soup.find("span", class_="KscYp") is None:
                    time = ""
                else:
                    timeToWork = soup.find("span", class_="KscYp")
                    time = timeToWork.findNext().text




                if soup.find("span", class_="ui_icon phone XMrSj") is None:
                    number = ""
                else:
                    phoneNum = soup.find("span", class_="ui_icon phone XMrSj")
                    number = phoneNum.findNext().text




                listCards.append(Food(id=id,
                                      title=title,
                                      link="https://www.tripadvisor.ru"+link,
                                      address=address,
                                      location=location,
                                      priceRange=priceRange,
                                      time=time,
                                      number=number))


                write_csv(listCards)
                listCards = []
                count -= 1

                print("Номер карточки: " + str(id))
                print("Название:" + title)
                print("Ссылка: https://www.tripadvisor.ru" + link)
                print(address)
                print(location)
                print(priceRange)
                print(time)
                print(number)
                print('')






def create_csv():
    with open(f"food_2.csv", mode= "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            "ID карточки",
            "Название",
            "Ссылка на источник",
            "Адрес",
            "Месторасположение",
            "Цены",
            "Время работы",
            "Номер для связи"
        ])

def write_csv(foods: list):
    with open(f"food_2.csv", mode= "a", newline="") as file:
        writer = csv.writer(file)
        for food in foods:
            writer.writerow([
                food.id,
                food.title,
                food.link,
                food.address,
                food.location,
                food.priceRange,
                food.time,
                food.number
            ])


if __name__ == "__main__":
    parser()


