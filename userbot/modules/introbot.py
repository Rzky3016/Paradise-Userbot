# PARADISE PROJECT
# COPYRIGHT 2021
# Ikyy
# Don't Remove Credit

from random import choice
from userbot import CMD_HELP
from userbot.events import register
import asyncio


# ================= CONSTANT =================

@register(outgoing=True, pattern="^.introbot(?: |$)(.*)")
async def _(event):
await event.edit(
    " Hei, Welcome...",
    " Let Me Introduce Myself"
    " __Iam A Paradise__",
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
    " __Paradise Out Of Conversation__")


CMD_HELP.update(
    {
        "introbot": "**✘ Plugin :** introbot\
        \n\n  •  Perintah : .introbot\
        \n  •  Function : Intro Untuk Memulai Perkenalan Dengan Paradise Ubotmu\
    "
    }
)
