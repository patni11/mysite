import urllib.request
import json
import requests
import shutil
import os
import pandas as pd
import calendar
from django.conf import settings
from .articles import add_article_to_database


def download_image(image_url, filename):

    r = requests.get(image_url, stream=True)

    if r.status_code == 200:
        r.raw.decode_content = True
        file = f"{os.getcwd()}/media/article_images/{filename}.png"
        with open(file, 'wb') as f:
            shutil.copyfileobj(r.raw, f)

        print('Image sucessfully Downloaded: ', filename)
    else:
        print('Image Couldn\'t be retreived')


def change_date_format(date):
    date_components = date.split("-")
    month_name = calendar.month_name[int(date_components[1])]
    return f"{month_name} {date_components[2]}, {date_components[0]}"


def add_new_article():
    url = f"https://api.rss2json.com/v1/api.json?rss_url=https%3A%2F%2Fshubhpatni.medium.com%2Ffeed&api_key={settings.RSS_2_JSON_KEY}&count=2"
    response = urllib.request.urlopen(url)
    path = os.getcwd()
    data = json.loads(response.read())
    data_frame = pd.read_csv(
        f"{path}/main/static/data/my_articles.csv")

    article_title = [each for each in data_frame["Name"]]

    new_articles = {}
    try:
        for item in data['items']:

            topic = ""
            for each in item['categories']:
                topic += f"{each}, "
            topic = topic[:len(topic)-2]

            new_articles[item['title']] = {"date pub": item['pubDate'], "Link": item['link'],
                                           "thumbnail": item['thumbnail'], "Topic": topic}

    except IndexError:
        print("Empty")

    for each in new_articles.keys():
        if each in article_title:
            continue
        else:

            date_pub = change_date_format(
                new_articles[each]['date pub'].split()[0])

            new_article_data = {"Name": each, "Link": new_articles[each]['Link'],
                                "Topic": new_articles[each]['Topic'], "date pub": date_pub}

            data_frame = data_frame.append(new_article_data, ignore_index=True)
            data_frame = data_frame.filter(
                ['Name', 'Link', 'Topic', 'date pub'], axis=1)

            data_frame.to_csv(
                f"{os.getcwd()}/main/static/data/my_articles.csv", encoding='utf-8', index=False)
            print("New Article Added:  ", each)

            download_image(new_articles[each]['thumbnail'], each)
            image_name = image_name(each)
            new_article_data[
                "image_path"] = f"/article_images/{image_name}.png"

            add_article_to_database(new_article_data)


'''
def move_images(csv_location):
    article_file = pd.read_csv(f"{csv_location}/my_articles.csv")
    articles = []
    for num, each in enumerate(article_file["Name"]):
        try:
            print(num, each.split('|')[0])
        except:
            print("INT")

    for each in article_file["Name"]:
        for dirpath, dirname, files in os.walk(f"{csv_location}/my_articles"):

            each = each.split('|')[0]
            if each[0:3] == dirname[0:3]:
                for f in files:
                    if f[-3:].lower() == 'jpg' or files[-4:].lower() == "jpeg" or f[-3:].lower() == 'png':
                        os.rename(f"{csv_location}/my_articles/{dirname}/{f}",
                                  f"{csv_location}/my_articles/{dirname}/{each}.png")
                        shutil.move(f"{csv_location}/my_articles/{dirname}/{each}.png",
                                    'mysite/main/static/images/articles/article_images/')
move_images('mysite/main/static/data/')
'''

# print(get_data())
# print(download_image(
#   "https://cdn-images-1.medium.com/max/2600/0*t141bucVcHQacCvy", "6 Ways To Generate Passive Income With Crypto.png"))
