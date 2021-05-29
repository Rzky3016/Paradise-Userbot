from userbot import CMD_HELP
from userbot.events import register
import requests
from bs4 import BeautifulSoup as bs
import re

# Port By @xflicks Linux-Userbot
# Yang hapus cacat asu


@register(outgoing=True, pattern=r"^\.kucing ?(.*)")
async def _(event):
    query = event.pattern_match.group(1)
    if not query:
        await event.edit("Usage: <query>")
    else:
        await event.edit("Tungguuuu....")
        url = "https://nekosearch.frissst.repl.co/search/"
        req = requests.get(url + query)
        jsons = req.json()
        msg = f"<b>Hasil: {query}</b>\n\n"
        if not jsons["success"]:
            await event.edit("404 Not found")
        else:
            m_result = jsons["result"]
            for result in m_result:
                m_title = result["title"]
                m_video_url = result["url"]
                msg += f"~ <a href='{m_video_url}'>{m_title}</a>\n"
                await event.edit(msg, parse_mode="html")


def search(anime):
    result_anime = []
    str_url = "http://nekopoi-index.herokuapp.com/"
    search_url = requests.get(str_url + "?search=" + anime)
    soup_html = bs(search_url.text, "html5lib")
    soup_body = soup_html.find_all(
        "tr",
        class_="border-t border-b border-gray-300 my-2 p-4 rounded hover:bg-blue-100")
    if soup_body:
        for soup_result in soup_body:
            result_id = soup_result.find(
                "th", class_="my-2 p-2").get_text(strip=True)
            result_bool = True if soup_result.find(
                "th", string="True") else False
            if result_bool:
                result_title = soup_result.find("a").get_text()
                string_title = re.sub(r"[\W\^_-]", " ", result_title)
                my_title1 = re.sub(r"\s+", " ", string_title)
                my_title2 = my_title1.replace(r"480P", "")
                my_title3 = my_title2.replace(r"mp4", "")
                result_anime.append(
                    {"title": my_title3.replace(r"NekoPoi", ""), "id": result_id})
        return{
            "result": result_anime,
            "response": "200"
        }
    else:
        return{
            "result": "Not Found",
            "response": "404"
        }


def get_search_result(query):
    search_res = search(query)
    search_response = search_res["response"]
    search_body = search_res["result"]
    message = f"**Hasil Nekopoi**: `{query}`\n\n"
    if search_response == "404":
        return "`Nothing found`"
    else:
        for src in search_body:
            title = src["title"]
            ids = src["id"]
            message += f"•{title}(`{ids}`)\n"
        return message


@register(outgoing=True, pattern=r"^\.searchpoi ?(.*)")
async def nekopoi(bot):
    query = bot.pattern_match.group(1)
    if not query:
        await bot.edit("Usage: <query>")
    else:
        await bot.edit("Searching...")
        result = get_search_result(query)
        await bot.edit(result)


CMD_HELP.update({
    "nekocare":
        "Nekopoi search:\
          \n> Usage: .searchpoi <query>\
          \n Cari jav/hen di nekopoi"
})
