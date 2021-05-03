# © Copyright 2021 Lynx-Userbot LLC Company. (Axel Alexius Latukolan)
# GPL-3.0 License (General Public License) From Github
# WARNING !! Don't Delete This Hashtag if u Kang it !!
# Ported for Lynx-Userbot by @SyndicateTwenty4 (axel)
# Credits : @Vader and @TeamSecret_Kz (Kenzo)


from faker import Faker
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import CMD_HELP
from userbot.events import register


# Ported for Lynx-Userbot
@register(outgoing=True, pattern=r"^\.gencc(?: |$)(.*)")
async def gencc(lynxevent):
    if lynxevent.fwd_from:
        return
    lynxcc = Faker()
    lynxname = lynxcc.name()
    lynxadre = lynxcc.address()
    lynxcard = lynxcc.credit_card_full()

    await edit_or_reply(lynxevent, f"__**👤 NAME :- **__\n`{lynxname}`\n\n__**🏡 ADDRESS :- **__\n`{lynxadre}`\n\n__**💸 CARD :- **__\n`{lynxcard}`")


# Ported for Lynx-Userbot
@register(outgoing=True, pattern=r"^\.bin(?: |$)(.*)")
async def bin(event):
    if event.fwd_from:
        return
    lynx_input = event.pattern_match.group(1)
    chat = "@carol5_bot"
    await event.edit("Checking...")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=1448477501))
            await event.client.send_message(chat, f"/bin {lynx_input}")
            response = await response
        except YouBlockedUserError:
            await event.reply("Please Unblock @carol5_bot")
            return
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)


# Ported for Lynx-Userbot
@register(outgoing=True, pattern=r"^\.vbv(?: |$)(.*)")
async def vbv(event):
    if event.fwd_from:
        return
    lynx_input = event.pattern_match.group(1)
    chat = "@carol5_bot"
    await event.edit("Checking...")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=1448477501))
            await event.client.send_message(chat, f"/vbv {lynx_input}")
            response = await response
        except YouBlockedUserError:
            await event.reply("Please Unblock @carol5_bot")
            return
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)


# Ported for Lynx-Userbot
@register(outgoing=True, pattern=r"^\.key(?: |$)(.*)")
async def key(event):
    if event.fwd_from:
        return
    lynx_input = event.pattern_match.group(1)
    chat = "@carol5_bot"
    await event.edit("Checking...")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=1448477501))
            await event.client.send_message(chat, f"/key {lynx_input}")
            response = await response
        except YouBlockedUserError:
            await event.reply("Please Unblock @carol5_bot")
            return
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)


# Ported for Lynx-Userbot
@register(outgoing=True, pattern=r"^\.iban(?: |$)(.*)")
async def iban(event):
    if event.fwd_from:
        return
    lynx_input = event.pattern_match.group(1)
    chat = "@carol5_bot"
    await event.edit("Checking...")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=1448477501))
            await event.client.send_message(chat, f"/iban {lynx_input}")
            response = await response
        except YouBlockedUserError:
            await event.reply("Please Unblock @carol5_bot")
            return
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)


# Ported for Lynx-Userbot
@register(outgoing=True, pattern=r"^\.ccheck(?: |$)(.*)")
async def ccheck(event):
    if event.fwd_from:
        return
    lynx_input = event.pattern_match.group(1)
    chat = "@carol5_bot"
    await event.edit("Checking...")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=1448477501))
            await event.client.send_message(chat, f"/ss {lynx_input}")
            response = await response
        except YouBlockedUserError:
            await event.reply("Please Unblock @carol5_bot")
            return
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)


# Ported for Lynx-Userbot
@register(outgoing=True, pattern=r"^\.ccbin(?: |$)(.*)")
async def ccbin(event):
    if event.fwd_from:
        return
    lynx_input = event.pattern_match.group(1)
    chat = "@carol5_bot"
    await event.edit(f"Trying to generate CC from the given bin `{lynx_input}`")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=1448477501))
            await event.client.send_message(chat, f"/gen {lynx_input}")
            response = await response
        except YouBlockedUserError:
            await event.reply("Please Unblock @carol5_bot")
            return
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)


# Ported for Lynx-Userbot
CMD_HELP.update({
    "ccarder": "⚡CMD⚡: `.gencc`\
\n↳ : Generates Fake CC.\
\n\n⚡CMD⚡: `.ccheck` <query>\
\n↳ : Checks That The Given CC is Live or Not.\
\n\n⚡CMD⚡: `.iban` <query>\
\n↳ : Checks That The Given IBAN ID is Live or Not.\
\n\n⚡CMD⚡: `.key` <query>\
\n↳ : Checks the status of probided key.\
\n\n⚡CMD⚡: `.vbv` <query>\
\n↳ : Checks the vbv status of given card.\
\n\n⚡CMD⚡: `.bin` <query>\
\n↳ : Checks that the given bin is valid or not.\
\n\n⚡CMD⚡: `.ccbin` <bin>\
\n↳ : Generates CC from the given bin."
})
