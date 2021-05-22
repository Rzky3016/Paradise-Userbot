""" Userbot module for other small commands. """
from userbot import CMD_HELP, ALIVE_NAME
from userbot.events import register


# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.lhelp$")
async def usit(e):
    await e.edit(
        f"**Hai Tuan {DEFAULTUSER} Kalau Anda Tidak Tau Perintah Untuk Memerintah Ku Ketik** `.help` Atau Bisa Minta Bantuan Ke:\n"
        "\n[Mastah](t.me/xflicks)"
        "\n[Repo](https://github.com/ferikunn/Linux-Userbot)"
        "\n[Instagram Mastah](Instagram.com/ferikunn)")


@register(outgoing=True, pattern="^.vars$")
async def var(m):
    await m.edit(
        f"**Disini Daftar Vars Dari {DEFAULTUSER}:**\n"
        "\n[DAFTAR VARS](https://raw.githubusercontent.com/ferikunn/Linux-Userbot/Linux-Userbot/varshelper.txt)")


CMD_HELP.update({
    "linuxhelper":
    "🐧CMD🐧`.lhelp`\
\nPenjelasan: Bantuan Untuk saya-Userbot.\
\n🐧CMD🐧`.vars`\
\nPenjelasan: Untuk Melihat Beberapa Daftar Vars."
})
