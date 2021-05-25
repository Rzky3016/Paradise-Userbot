import json
import urllib.request


from userbot.events import register
from userbot import CMD_HELP


# Port By @VckyouuBitch From GeezProject
# Buat Kamu Yang Hapus Credits. Intinya Kamu Anjing:)
@register(outgoing=True, pattern="^.ip(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)

    adress = input_str

    token = "19e7f2b6fe27deb566140aae134dec6b"

    api = "http://api.ipstack.com/" + adress + "?access_key=" + token + "&format=1"

    result = urllib.request.urlopen(api).read()
    result = result.decode()

    result = json.loads(result)
    linux1 = result["type"]
    linux2 = result["country_code"]
    linux3 = result["region_name"]
    linux4 = result["city"]
    linux5 = result["zip"]
    linux6 = result["latitude"]
    linux7 = result["longitude"]
        f"<b><u>INFORMASI BERHASIL DIKUMPULKAN</b></u>\n\n<b>Ip type :-</b><code>{linux1}</code>\n<b>Country code:- </b> <code>{linux2}</code>\n<b>State name :-</b><code>{linux3}</code>\n<b>City name :- </b><code>{linux4}</code>\n<b>zip :-</b><code>{linux5}</code>\n<b>Latitude:- </b> <code>{linux6}</code>\n<b>Longitude :- </b><code>{linux7}</code>\n",
        parse_mode = "HTML",
    )


CMD_HELP.update({
    "alamatpalsu":
    "•CMD: `.ip`\
    \n•Penjelasan: Memberikan detail tentang alamat ip."


})
