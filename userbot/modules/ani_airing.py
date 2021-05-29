import requests
from userbot import CMD_HELP
from userbot.events import register
import requests

# time formatter from uniborg
# Port By @xflicks Linux-Userbot
# yang hapus stress ajg


def time_(milliseconds: int) -> str:
    """Inputs time in milliseconds, to get beautified time,
    as string"""
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = ((str(days) + " Days, ") if days else "") + \
        ((str(hours) + " Hours, ") if hours else "") + \
        ((str(minutes) + " Minutes, ") if minutes else "") + \
        ((str(seconds) + " Seconds, ") if seconds else "") + \
        ((str(milliseconds) + " ms, ") if milliseconds else "")
    return tmp[:-2]
# Don't do anything
# f"FKTnK3aKtFvMSUiWLZrTuAp4g93VSjbXcR5zGmqWAijuAuYgR2ACP8WNot2ZyTRVECks1uV5WWW7muWz5SZkY2P8YbWW6AYLUFTsmFU1oW9Y2GP4"


def _api(str_):
    query = '''
    query ($id: Int,$search: String) {
      Media (id: $id, type: ANIME,search: $search) {
        id
        title {
          romaji
          native
        }
        nextAiringEpisode {
           airingAt
           timeUntilAiring
           episode
        }
        coverImage {
           extraLarge
        }
        startDate{
            year
        }
          episodes
          bannerImage
      }
    }
    '''
    variables = {
        'search': str_,
        "asHtml": True
    }
    url = 'https://graphql.anilist.co'
    response = requests.post(
        url,
        json={
            'query': query,
            'variables': variables})
    jsonD = response.json()
    return jsonD


"""Jadwal rilis anime"""


@register(outgoing=True, pattern=r"^.airing ?(.*)")
async def _(event):
    query = event.pattern_match.group(1)
    if not query:
        await event.edit("Usage: .airing <Anime Name>")
        return
    result = _api(query)
    error = result.get('errors')
    if error:
        err = f"**Anime** : `{error[0].get('message')}`"
        await event.edit(err)
        return
    caption = ""
    data = result['data']['Media']
    mid = data.get('id')
    romaji = data['title']['romaji']
    native = data['title']['native']
    episodes = data.get('episodes')
    coverImg = data.get('coverImage')['extraLarge']
    caption += f"**Name**: **{romaji}**(`{native}`)"
    caption += f"\n**ID**: `{mid}`"
    if data['nextAiringEpisode']:
        time = data['nextAiringEpisode']['timeUntilAiring'] * 1000
        time = time_(time)
        caption += f"\n**Episode**: `{data['nextAiringEpisode']['episode']}`"
        caption += f"\n**Airing in**: `{time}`"
        await event.delete()
        await event.client.send_file(
            event.chat_id,
            file=coverImg,
            caption=caption,
            reply_to=event,
        )
    else:
        caption += f"\n**Episode**: `{episodes}`"
        caption += f"\n**Status**: `N/A`"
        await event.delete()
        await event.client.send_file(
            event.chat_id,
            file=coverImg,
            caption=caption,
            reply_to=event,
        )


@register(outgoing=True, pattern=r"^\.jadwalrilis ?(.*)")
async def _(event):
    post = event.pattern_match.group(1).lower()
    if not post:
        await event.edit("**Usage**: `.jadwalrilis` <Senin/Selasa>")
    else:
        await event.edit("`Loading..`")
        url = "https://anime.kaedenoki.net/api/schedule"
        jsn = requests.get(url).json()
        m_query = 0
        tbl_hari = [
            "senin",
            "selasa",
            "rabu",
            "kamis",
            "jumat",
            "sabtu",
            "minggu"]
        msg = "Jadwal Rilis Hari: "
        if post == tbl_hari[0]:
            m_query = 0
        if post == tbl_hari[1]:
            m_query = 1
        if post == tbl_hari[2]:
            m_query = 2
        if post == tbl_hari[3]:
            m_query = 3
        if post == tbl_hari[4]:
            m_query = 4
        if post == tbl_hari[5]:
            m_query = 5
        if post == tbl_hari[6]:
            m_query = 6
        json_day = jsn["scheduleList"]
        json_days = json_day[m_query]["day"]
        json_titl = json_day[m_query]["animeList"]
        msg += f"**{json_days}**\n"
        for json_tt in json_titl:
            json_title = json_tt["anime_name"]
            msg += f" ~ `{json_title}`\n"
        msg += f"\n**Note**: `Jadwal bisa berubah sewaktu-waktu`"
        await event.edit(msg)


# f"FKTnK3aKtFvMSUiWLZrTuAp4g93VSjbXcR5zGmqWAijuAuYgR2ACP8WNot2ZyTRVECks1uV5WWW7muWz5SZkY2P8YbWW6AYLUFTsmFU1oW9Y2GP4"
CMD_HELP.update({
    "ani_airing":
    "ani_airing"
    "\n > `.airing` <`anime name`>"
    "\n  **Usage**: `liat anime waktu rilis`"
    "\n > `.jadwalrilis` <`senin/selasa`>"
    "\n  **Usage**: `liat jadwal rilis anime`"
})
