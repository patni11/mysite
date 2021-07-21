from datetime import date
import datetime
import os
import pandas as pd
from main.models import Articles


def add_article_to_database(article):
    title = article["Name"]
    date_created = convert_date(article["date pub"])
    medium_link = article["Link"]
    image = article["image_path"]
    tags = change_tag(article["Topic"])

    if Articles.objects.filter(title=title).exists():
        return
    else:
        Articles.objects.create(title=title, date_created=date_created,
                                medium_link=medium_link, image=image, tags=tags)
        print("added an article")


def change_tag(tags):
    replace_tags = {'blockchain': "Crypto", 'productivity': "Productivity", 'money': "Tech", 'AR': "Tech", 'gadgets': "Tech", 'programming': "Programming",
                    'cryptocurrency': "Crypto", 'tech': "Tech", 'defi': "Crypto", 'electronics': "Programming", 'life': 'Productivity', 'crypto': 'Crypto', 'future': "Tech"}

    all_tags = []
    final_tag = ""
    for i in tags.split(','):
        new_tag = i.replace(" ", "")
        if new_tag in replace_tags.keys():
            new_tag = replace_tags[new_tag]
            all_tags.append(new_tag)

    for tag in all_tags:
        if tag == "Productivity":
            final_tag = "Productivity"

        elif tag == "Programming":
            final_tag = "Programming"

        elif tag == "Crypto":
            final_tag = "Crypto"

        elif tag == "Tech":
            final_tag = "Tech"

    return final_tag


def add_all_articles():
    path = os.getcwd()
    df = pd.read_csv('main/static/data/my_articles.csv')

    for index, row in df.iterrows():
        article = {"Name": row['Name'], "Link": row['Link'],
                   "Topic": row['Topic'], "date pub": row['date pub'], "image_path": f"/article_images/{row['Name']}.png"}

        add_article_to_database(article)


def get_all_tags():
    tag_list = []
    for each in Articles.objects.all():
        for i in each.tags.split(','):
            tag_list.append(i.replace(" ", ""))

    tag_list = set(tag_list)
    return tag_list


def change_all_tags():
    replace_tags = {'blockchain': "Crypto", 'productivity': "Productivity", 'money': "Tech", 'AR': "Tech", 'gadgets': "Tech", 'programming': "Programming",
                    'cryptocurrency': "Crypto", 'tech': "Tech", 'defi': "Crypto", 'electronics': "Programming", 'life': 'Productivity', 'crypto': 'Crypto', 'future': "Tech"}

    for each in Articles.objects.all():
        final_tag = ""
        all_tags = []
        for i in each.tags.split(','):
            new_tag = i.replace(" ", "")
            if new_tag in replace_tags.keys():
                new_tag = replace_tags[new_tag]
                all_tags.append(new_tag)

        for tag in all_tags:
            if tag == "Productivity":
                final_tag = "Productivity"

            elif tag == "Programming":
                final_tag = "Programming"

            elif tag == "Crypto":
                final_tag = "Crypto"

            elif tag == "Tech":
                final_tag = "Tech"

        each.tags = final_tag
        print(final_tag)
        print("tag changed")


def convert_date(date):
    if '-' not in date:
        date_components = date.split()
        datetime_object = datetime.datetime.strptime(date_components[0], "%B")
        day = date_components[1].split(',')
        return f"{date_components[2]}-{datetime_object.month}-{day[0]}"
    else:
        return date
# def check_new_article():
