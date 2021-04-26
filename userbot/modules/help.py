from platform import uname
from userbot.events import register
from userbot import ALIVE_NAME, CMD_HELP
import asyncio
Skip to content
ferikunn
/
King - Userbot
forked from apisuserbot / King - Userbot
Code
Pull requests
Actions
Projects
Wiki
Security
Insights
Settings
King - Userbot / userbot / modules / help.py


@apisuserbot
apisuserbot Update help.py
1 contributor
43 lines(38 sloc)  1.61 KB
# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot help command """


modules = CMD_HELP

# Ported by KENZO (Lynx-Userbot)
# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.help(?: |$)(.*)")
async def help(event):
    """ For .help command,"""
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await event.edit(str(CMD_HELP[args]))
        else:
            await event.edit("**Maaf Tuan Saya Tidak Punya Perintah Itu:)**")
            await asyncio.sleep(200)
            await event.delete()
    else:
        string = ""
        for i in CMD_HELP:
            string += "`" + str(i)
            string += "`\t|  "
        await event.edit("**⚡Saya-Userbot⚡**\n\n"
                         f"**◑» Bᴏᴛ ᴏꜰ {DEFAULTUSER}**\n**◑» Mᴏᴅᴜʟᴇꜱ : {len(modules)}**\n\n"
                         "**• Mᴀɪɴ Mᴇɴᴜ :**\n"
                         f"╰►| {string} ◄─\n\n")
        await event.reply(f"\n**🔥 Contoh** : **Ketik** `.help afk` **Untuk Informasi Pengunaan.\nAtau Bisa Juga Ketik** `.helpme` **Untuk Main Menu Yang Lain-Nya.** 🔥")
        await asyncio.sleep(1000)
        await event.delete()
© 2021 GitHub, Inc.
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
Loading complete
