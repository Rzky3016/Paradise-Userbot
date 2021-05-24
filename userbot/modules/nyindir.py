from time import sleep
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^.tua(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("**EH BOCAH TUA HINA, KALO TUANYA TUA AJA GOBLOK GA COCOK BOCAH TUA KAYA LU MAIN KEK GINIAN TOLOL UDAH BAU TANAH JADINYA GAUSAH BELAGU KONTOL.**")
    sleep(5)
    await typew.edit("**URUSIN AJA BEGO KUBURAN LU ITU BESOK CALON RUMAH LU SEKALI SEKALI YEKAN LU TINGGAL DIRUMAH GA DI RONGSOKAN MULU**")


@register(outgoing=True, pattern='^.gajelas(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("**YA AMPUN LU NGOMONG APA? GA NYAMBUNG KONTOL KAYA KEHIDUPAN LU MAKANYA ORG ORG KAYA LU GABAKALN MAJU HIDUPNYA APA LAGI ORG ORG BAWAHAN KAYA LU.**")


CMD_HELP.update({
    "nyindir1":
    "`•🐧CMD🐧: .tua`\
    \n•Penjelasan: Gatau cek sendiri asu\
    \n\n`•🐧CMD🐧: .gajelas`\
    \n•Penjelasan: Nyindir orang Goblok."


})
