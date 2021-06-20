# Ikyy Modules
# Ciee LDR

from time import sleep
from userbot.events import register
from userbot import CMD_HELP


@register(outgoing=True, pattern='^.ldr(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Ekhemm...**")
    sleep(3)
    await typew.edit("**Ciee Virtual...**")
    sleep(3)
    await typew.edit("**Situ Darling Atau Daring?**")
    sleep(3)
    await typew.edit("**Pacaran Kok Lewat Hp?**")
    sleep(3)
    await typew.edit("**Baper Kok Sama Ketikan? Aowkwk**")
    sleep(3)
    await typew.edit("**LDR, Long Distance Relationship**")
    sleep(3)
    await typew.edit("**Wifi Sama Bluetooth Aja Ga Bisa Jarak Jauh, Kok Lu Malah Nyaman Sama Yang Jauh?**")
    sleep(3)
    await fry.client.send_file(fry.chat_id, "https://telegra.ph/file/63fb1ed0b40f7dbddc001.png")


CMD_HELP.update({
    "ldr":
    "🗿CMD🗿:`.ldr`\
  \nPenjelasan:Buat Org Yang LDR."
})
