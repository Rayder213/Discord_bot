import requests
from bs4 import BeautifulSoup
from requests_html import AsyncHTMLSession


async def get_data(name_picture):
    asession = AsyncHTMLSession()
    r = await asession.get(f"https://yandex.ru/images/search?from=tabbar&text={name_picture}")
    await r.html.arender()
    return r


async def get_picture(name_picture):
    try:

        results = await get_data(name_picture)

        soup = BeautifulSoup(results.html.html, 'html.parser')

        img_data = requests.get(
            "http:" + soup.find_all('img', class_="serp-item__thumb justifier__thumb")[0]['src']).content
        with open('image_name.jpg', 'wb') as handler:
            handler.write(img_data)
        return "image_name.jpg"
    except BaseException as e:
        print(e)
        return False
