# Feri Gans

from userbot import CMD_HELP
from userbot.events import register
import asyncio


@register(outgoing=True, pattern="^.jawa$")
async def koc(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("Baik")
        await asyncio.sleep(1)
        await e.edit("Tidak sombong")
        await asyncio.sleep(1)
        await e.edit("Ganteng")
        await asyncio.sleep(1)
        await e.edit("Sopan")
        await asyncio.sleep(1)
        await e.edit("Rajin")
        await asyncio.sleep(1)
        await e.edit("Budiman")
        await asyncio.sleep(1)
        await e.edit("Alim")
        await asyncio.sleep(1)
        await e.edit("Berguna")
        await asyncio.sleep(1)
        await e.edit("Nguli juga")
        await asyncio.sleep(1)
        await e.edit("Pemaaf")
        await asyncio.sleep(1)
        await e.edit("Jujur")
        await asyncio.sleep(1)
        await e.edit("Ga Sombong")
        await asyncio.sleep(1)
        await e.edit("Kaya")
        await asyncio.sleep(1)
        await e.edit("Pokoknya Jawa pro")
        await asyncio.sleep(1)
        await e.edit("Tidak seperti Sunda sama Betawi")
        await asyncio.sleep(1)
        await e.edit("Intinya Jawa Cakep Cakep")


@register(outgoing=True, pattern="^.sunda")
async def koc(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("Apa itu sunda?")
        await asyncio.sleep(1)
        await e.edit("Sunda adalah suku")
        await asyncio.sleep(1)
        await e.edit("Suku yg sangat sombong")
        await asyncio.sleep(1)
        await e.edit("aowkwkwwkwkwk")
        await asyncio.sleep(1)
        await e.edit("lariiiiii ada sunda")
        await asyncio.sleep(1)
        await e.edit("Sundanya ngejarrr ajgggg")
        await asyncio.sleep(1)
        await e.edit("Lariiiiiii cokkkk")
        await asyncio.sleep(1)
        await e.edit("nanti kalau kena sunda jadi korepen")
        await asyncio.sleep(1)
        await e.edit("ajggg ajgg")
        await asyncio.sleep(1)
        await e.edit("dasar sunda")
        await asyncio.sleep(1)
        await e.edit("Offf Sunda baperan aowkwkwwk")


@register(outgoing=True, pattern='^.betawi(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`\nHuu Ada Betawi`")
    await asyncio.sleep(1)
    await typew.edit("`\nLari Lari Cuk`")
    await asyncio.sleep(1)
    await typew.edit("`\nBetawi ngejarrrr`")
    await asyncio.sleep(1)
    await typew.edit("`\nLariii ada dikejar Betawi`")
    await asyncio.sleep(1)
    await typew.edit("`\nAoskswkwkwkwmwk Asuuuuu`")
    await asyncio.sleep(1)
    await typew.edit("`\nOff Betawi Baperan 🏃🏃🏃🏃🏃🏃🏃🏃`")


@register(outgoing=True, pattern="^.jakarta$")
async def koc(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("Jakarta keras")
        await asyncio.sleep(1)
        await e.edit("Tidak sombong")
        await asyncio.sleep(1)
        await e.edit("Banyak Tingkah")
        await asyncio.sleep(1)
        await e.edit("Aslinya Sopan")
        await asyncio.sleep(1)
        await e.edit("Lu jangan ngusik Ajg")
        await asyncio.sleep(1)
        await e.edit("Lu Sopan Kami Sopan")
        await asyncio.sleep(1)
        await e.edit("Dan")
        await asyncio.sleep(1)
        await e.edit("Duarrrr Kontol")
        await asyncio.sleep(1)
        await e.edit("⚡")
        await asyncio.sleep(3)
        await e.edit("Jakarta Nih Bos")


# Feri Imut
# Feri Gans
# FB
CMD_HELP.update({
    "gjm":
    "`.sunda` ; `.betawi` ; `.jawa` ; `jakarta`\
    \nPenjelasan: liat sendiri Tololll"
})
