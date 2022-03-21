# import HTMLSession from requests_html
from requests_html import AsyncHTMLSession
from bs4 import BeautifulSoup
import asyncio


async def get_data(name_video):
    asession = AsyncHTMLSession()
    r = await asession.get(f"https://www.youtube.com/results?search_query={name_video}")
    await r.html.arender()
    return r


async def get_url(name_video):
    # create an HTML Session object

    # Use the object above to connect to needed webpage
    results = await get_data(name_video)

    # Run JavaScript code on webpage
    soup = BeautifulSoup(results.html.html, 'html.parser')
    return "https://www.youtube.com" + \
           soup.find_all('a', class_="yt-simple-endpoint style-scope ytd-video-renderer")[0]['href']