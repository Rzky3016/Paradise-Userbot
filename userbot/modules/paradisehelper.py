""" Userbot module for other small commands. """
from userbot import CMD_HELP, ALIVE_NAME
from userbot.events import register


# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.phelp$")
async def usit(e):
    await e.edit(
        f"**Hai Tuan {DEFAULTUSER} Kalau Anda Tidak Tau Perintah Untuk Memerintah Ku Ketik** `.help` Atau Bisa Minta Bantuan Ke:\n"
        "\n[Dev](t.me/Nopegoodloking)"
        "\n[Repo](https://github.com/Rzky3016/Paradise-Userbot)"
        "\n[Instagram Dev](Instagram.com/_rizky3016_)")


@register(outgoing=True, pattern="^.vars$")
async def var(m):
    await m.edit(
        f"**Disini Daftar Vars Dari {DEFAULTUSER}:**\n"
        "\n[DAFTAR VARS](https://raw.githubusercontent.com/Rzky3016/Paradise-Userbot/Paradise-Userbot/varshelper.txt)")


CMD_HELP.update({
    "paradisehelper":
    "🗿CMD🗿`.phelp`\
\nPenjelasan: Bantuan Untuk saya-Userbot.\
\n🗿CMD🗿`.vars`\
\nPenjelasan: Untuk Melihat Beberapa Daftar Vars."
})
