"""
	Scrape neonime.vip
	Feature
           Show new update anime
           Scrape link download
	By : @xflicks
"""

import requests
from bs4 import BeautifulSoup as bs
import re
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern=r"^\.neonime ?(.*)")
async def _neonime(event):
    await event.edit('tunggu bentar...')
    url = 'https://neonime.vip/episode/'
    ht_ = requests.get(url).text
    _bs = bs(ht_, "html.parser")
    bd_ = _bs.findAll('td', class_='bb')
    out = "<b>New Episode:</b>\n\n"
    for kntl_ in bd_:
        _lucu = kntl_.find('a')
        if not _lucu:
            _lucu = 'none'
        else:  # FKTnK3aKtFvMSUiWLZrTuAp4g93VSjbXcR5zGmqWAijuAuYgR2ACP8WNot2ZyTRVECks1uV5WWW7muWz5SZkY2P8YbWW6AYLUFTsmFU1oW9Y2GP4
            tt_ = _lucu.get_text()
            _tt = re.sub(r'\s+Subtitle\s+Indonesia\s+Season.\d+', '', tt_)
            link = _lucu['href']
            out += f"• <a href='{link}'>{_tt}</a>\n"
            if len(out) > 1000:
                break
            await event.edit(out, parse_mode="html")


def get_html(url):
    tag_li = []
    req = requests.get(url)
    res = bs(req.text, "html5lib")
    box = res.find("div", class_="sbox").parent.find_all("li")
    if len(box) != 0:
        for clear in box:
            if clear.get_text() == 'MP4':
                box.remove(clear)
            elif clear.get_text() == 'MKV':
                box.remove(clear)
            else:
                pass
    for box_ in box:
        tag_li.append(box_)
    return {
        "html": tag_li
    }


def link_download(query, url):
    tag_label = []
    tag_href = []
    r = get_html(url)["html"]
    for k, v in enumerate(r[query].find_all("a")):
        tag_href.append({"server": v.get_text(strip=True), "link": v["href"]})
    for p, o in enumerate(r[query].find_all("label")):
        tag_label.append(o.get_text())
    return {
        "label": tag_label,
        "url": tag_href
    }


@register(outgoing=True, pattern=r"^\.neolink ?(.*)")
async def _(event):
    url = event.pattern_match.group(1)
    if not url:
        await event.edit("Masukan url episode, liat .help neonime")
    elif 'https://' not in url:
        await event.edit('Masukan url')
        return
    else:
        await event.edit("Tunggu nyet..")
        msg = "`Link Download`\n\n"
        p = link_download(1, url)
        for label_name in p["label"]:
            msg += f"- **{label_name}**:\n"
        for server_link in p["url"]:
            server_name = server_link["server"]
            server_url = server_link["link"]
            msg += f"<a href='{server_url}'>{server_name}</a>｜"
        await event.edit(msg, parse_mode="html")


CMD_HELP.update({"neonime": "**Neonime**"
                 "\n >`.neonime`"
                 "\n  Usage: Liat anime baru rilis di neonime."
                 "\n >`.neolink` <`url episode`>"
                 "\n  Usage: Cari link download, Copy url episode dari `.neonime` "})
