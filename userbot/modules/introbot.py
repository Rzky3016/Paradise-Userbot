# PARADISE PROJECT
# COPYRIGHT 2021
# Ikyy
# Don't Remove Credit

from random import choice
from userbot import CMD_HELP
from userbot.events import register


# ================= CONSTANT =================

INTROBOT_STRINGS = [
    " Hei, Welcome...",
    " Let Me Introduce Myself"
    " Iam A Paradise",
    " Iam Here To Help You Make Your Work Easier",
    " I Have Some Interesting Modules",
    " `Translating To Indonesian...",
    " Hei, Selamat Datang...",
    " Izinkan Saya Memperkenalkan Diri",
    " Aku Adalah Paradise",
    " Aku Disini Untuk Membantumu Mempermudah Pekerjaanmu",
    " Aku Mempunyai Berbagai Macam Modul Yang Menarik", " `Paradise Beralih Ke Bahasa Indonesia..`
    " Bersenang-Senang Lah Denganku..."
    " Jika Kamu Kesulitan Silahkan Ketik .helpme"
    " Dan Aku Akan Membantumu",
    " Lihatlah Projects Paradise Yang Lainnya Mungkin Itu Akan Membuat Kau Bahagia",
    " Segitu Saja Percakapan Kita Kali Ini",
    " Sekian Terimakasih..."
    " __Paradise Out Of Conversation__",
]


@register(outgoing=True, pattern="^.introbot$")
async def introbot(introbot):
    await introbot.edit(choice(INTROBOT_STRINGS))

CMD_HELP.update(
    {
        "introbot": "**✘ Plugin :** introbot\
        \n\n  •  Perintah : .introbot\
        \n  •  Function : Intro Untuk Memulai Perkenalan Dengan Paradise Ubotmu\
    "
    }
)
