# PARADISE PROJECT
# COPYRIGHT 2021
# Ikyy
# Don't Remove Credit

from userbot import CMD_HELP
from userbot.events import register


# ================= CONSTANT =================

@register(outgoing=True, pattern="^.introbot(?: |$)(.*)")
async def _(event):
    event.pattern_match.group(1)
    await event.edit(
        " Hei, Welcome...\n",
        " Let Me Introduce Myself\n",
        " __Iam A Paradise__\n",
        " Iam Here To Help You Make Your Work Easier\n",
        " I Have Some Interesting Modules\n",
        " `Translating To Indonesian...\n",
        " Hei, Selamat Datang...\n",
        " Izinkan Saya Memperkenalkan Diri\n",
        " Aku Adalah Paradise\n",
        " Aku Disini Untuk Membantumu Mempermudah Pekerjaanmu\n",
        " Aku Mempunyai Berbagai Macam Modul Yang Menarik\n",
        " `Paradise Beralih Ke Bahasa Indonesia..`\n"
        " Bersenang-Senang Lah Denganku...\n"
        " Jika Kamu Kesulitan Silahkan Ketik .helpme\n"
        " Dan Aku Akan Membantumu\n",
        " Lihatlah Projects Paradise Yang Lainnya Mungkin Itu Akan Membuat Kau Bahagia\n",
        " Perkenalkan Juga Penciptaku [ɪᴋʏʏ](https://t.me/Nopegoodloking)\n",
        " Kau Bisa Mengenal Dia Dengan Ketik .ikyy\n",
        " Segitu Saja Percakapan Kita Kali Ini\n",
        " Sekian Terimakasih...\n"
        " __Paradise Out Of Conversation__")


CMD_HELP.update(
    {
        "introbot": "**✘ Plugin :** introbot\
        \n\n  •  Perintah : .introbot\
        \n  •  Function : Intro Untuk Memulai Perkenalan Dengan Paradise Ubotmu\
    "
    }
)
