from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests
import threading
import os
import json


class Parcing:
    def __init__(self):
        self.lock = threading.Lock()


    def move_to_detailed_page(self,receipt_url):
        source = requests.get(f"https://kulinaria.ge{receipt_url}").text
        soup = BeautifulSoup(source, 'lxml')

        # რეცეპტის დასახელება
        receipt_name = soup.find('div',class_='post__title').h1.text


        # მთავარი სურათის მისამართი
        photo_url = soup.find("div", class_="post__img").img['src']

        # მოკლე აღწერა
        description = soup.find('div',class_='post__description').text.strip()
        description = description if description else None

        # ავტორის სახელი
        author = soup.find("span",class_='bold').a.text.lstrip()

         # მთავარი და ქვეკატეგორიების დასახელებები
        detailed_description = soup.find("div",class_="pagination-container")
        detailed_description = detailed_description.find_all('a')[2:]
        main_category_name, sub_category_name = detailed_description[0].text, detailed_description[1].text

        # მთავარი და ქვეკატეგორიების URL
        main_category_url, sub_category_url = detailed_description[0]['href'], detailed_description[1]['href']

        # ულუფების რაოდენობა
        portion = soup.find_all("div", class_='lineDesc__item')[1].text.split()[0]
        portion = int(portion) if portion.isdigit() else 0

        # რეცეპტის ინგრედიენტები
        ingredients = [" ".join(ingredient.text.split()) for ingredient in soup.find_all("div",class_='list__item')]

        # რეცეპტის მომზადების ეტაპები
        steps = [{step.div.text:step.p.text} for step in soup.find_all('div',class_='lineList__item')]



        data = {"receipt_name": receipt_name,
                "receipt_url":f"https://kulinaria.ge{receipt_url}",
                "photo_url":photo_url,
                "description":description,
                "author":author,
                "main_category_name":main_category_name,
                "sub_category_name":sub_category_name,
                "main_category_url":main_category_url,
                "sub_category_url":sub_category_url,
                "portion":portion,
                "ingredients":ingredients,
                "steps":steps
                }

        with self.lock:

            if os.path.exists("data.json"):
                with open("data.json", 'a',encoding="utf-8") as f:
                    f.write(",\n")
                    json.dump(data, f,ensure_ascii=False, indent=2)
            else:
                with open("data.json", 'w',encoding="utf-8") as f:
                    f.write("[\n")
                    json.dump(data, f,ensure_ascii=False, indent=2)


    def get_urls(self,i):
        source = requests.get(f"https://kulinaria.ge/receptebi/cat/sadResaswaulo/?page={i}").text
        soup = BeautifulSoup(source, 'lxml')
        receipts = soup.find_all("div", class_='box box--author kulinaria-col-3 box--massonry')
        receipt_urls = [receipt.find('div', class_='box-space').a['href'] for receipt in receipts]

        f = []
        with ThreadPoolExecutor() as exc:
            f = [exc.submit(self.move_to_detailed_page, url) for url in receipt_urls]

        for future in as_completed(f):
            future.result()
