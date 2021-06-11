from time import sleep
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^.rizky(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Hai Perkenalkan Namaku Rizky`")
    sleep(3)
    await typew.edit("`16 Tahun`")
    sleep(1)
    await typew.edit("`Owner Dari Paradise Userbot, Salam Kenal:)`")
# Create by myself @localheart


@register(outgoing=True, pattern='^ilyu(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Cuma Mau Bilang`")
    sleep(3)
    await typew.edit("`Aku Sayang Kamu, Kamu Sangat Berharga Dan Berarti Di Hidupku`")
    sleep(1)
    await typew.edit("`I LOVE YOU 💞`")
# Create by myself @localheart


@register(outgoing=True. pattern='^.ganteng(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Lu Mau Tau Semua Fakta?`")
    sleep(3)
    await typew.edit("`Fakta Yang Belum Terbongkar Selama Ini`")
    sleep(3)
    await typew.edit("`GUA GANTENG FIX NO DEBAT😏`")


@register(outgoing=True, pattern='^.semangat(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Apapun Yang Terjadi`")
    sleep(3)
    await typew.edit("`Tetaplah Bernapas`")
    sleep(1)
    await typew.edit("`Dan Selalu Bersyukur`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.wibu(?: |$)(.*)')
async def typewriter(type):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("`Kata Emak`")
    sleep(2)
    await typew.edit("`Kalo Ketemu Wibuu`")
    sleep(2)
    await typew.edit("`Harus Lari Sekenceng Mungkin🏃🏻`")
    sleep(1)
    await typew.edit("`ㅤㅤㅤㅤㅤㅤㅤㅤㅤ🏃🏻`")
    sleep(1)
    await typew.edit("`ㅤㅤㅤㅤㅤㅤㅤㅤ🏃🏻💨`")
    sleep(1)
    await typew.edit("`ㅤㅤㅤㅤㅤㅤㅤ🏃🏻💨ㅤ`")
    sleep(1)
    await typew.edit("`ㅤㅤㅤㅤㅤㅤ🏃🏻💨ㅤㅤ`")
    sleep(1)
    await typew.edit("`ㅤㅤㅤㅤㅤ🏃🏻💨ㅤㅤㅤ`")
    sleep(1)
    await typew.edit("`ㅤㅤㅤㅤ🏃🏻💨ㅤㅤㅤㅤ`")
    sleep(1)
    await typew.edit("`ㅤㅤㅤ🏃🏻💨ㅤㅤㅤㅤㅤ`")
    sleep(1)
    await typew.edit("`ㅤㅤ🏃🏻💨ㅤㅤㅤㅤㅤㅤ`")
    sleep(1)
    await typew.edit("`ㅤ🏃🏻💨ㅤㅤㅤㅤㅤㅤㅤ`")
    sleep(1)
    await typew.edit("`🏃🏻💨ㅤㅤㅤㅤㅤㅤㅤㅤ`")


@register(outgoing=True, pattern='^.pe(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("`Bapaknya Udin Di Makan Udang`")
    sleep(2)
    await typew.edit("`Cuma Sendiri nih Senggol Dong`")


@register(outgoing=True, pattern='^p(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("`Awali perkataan dengan dengan salam`")
    sleep(1)
    await typew.edit("`Assalamualaikum Sayang`")


CMD_HELP.update({
    "animasi3":
    "🗿CMD🗿`.pe`\
\nPenjelasan: Cek lah asw.\
\n\n🗿CMD🗿`.feri`\
\nPenjelasan: Cek lah asw.\
\n\n🗿CMD🗿`.ilyu`\
\nPenjelasan: Cek lah asw.\
\n\n🗿CMD🗿`p`\
\nPenjelasan: Cek lah asw.\
\n\n🗿CMD🗿`.semangat`\
\nPenjelasan: Cek lah asw.\
\n\n🗿CMD🗿`.wibu`\
\nPenjelasan: Lari Dari Wibu.\
\n\n🗿CMD🗿`.ganteng`\
\nPenjelasan: Gua Ganteng."
})
