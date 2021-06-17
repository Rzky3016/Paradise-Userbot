from time import sleep
from userbot.events import register
from userbot import CMD_HELP


@register(outgoing=True, pattern='^.chidori(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("Hello")
    sleep(2)
    await typew.edit("Gua Kakashi Lu Mungkin Mengenal Gua Sebagai Copy Ninja")
    sleep(5)
    await typew.edit("Lu Akan Membayar Untuk Apa yang Lu Lakukan Pada Rekan-Rekan Gua")
    sleep(6)
    await typew.edit("( ◗_ ╂ ) ☞✹)Chidori ")
    sleep(2)
    await typew.edit("You:(✖﹏✖)")
# Create by myself @PashaDIE


@register(outgoing=True, pattern='^.rasengan(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("Hei You")
    sleep(4)
    await typew.edit("Iam Uzumaki Naruto Hokage From Konohagakure")
    sleep(5)
    await typew.edit("You Will Pay For What You Did To My ColleaguesLu will pay for what you did to Konoha's people")
    sleep(4)
    await typew.edit("🔥")
    sleep(6)
    await typew.edit("(Ξ｀Д´)🌀)))Rasengan！")
    sleep(2)
    await typew.edit("You: ( ✖╭╮✖ )")
# create by myself @Nopegoodloking

CMD_HELP.update({
    'nartohh':
    '🗿CMD🗿`.chidori`\
        \nUsage: Mengeluarkan Chidori Dari Mamank Kakashi'
    '🗿CMD🗿`.rasengan`\
        \nUsage: Mengeluarkan Rasengan Dari Mamank Nartoh'
})
