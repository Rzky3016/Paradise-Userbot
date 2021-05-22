# BASED FROM ULTROID PORTED FOR LORD USERBOT BY ALVIN / @LIUALVINAS
# THANKS ULTROID
# DONT REMOVE THIS
# @USERBOT_GROUP

from telethon import events
from userbot import CMD_HELP, bot
from userbot.events import register
from telethon.errors.rpcerrorlist import YouBlockedUserError
import asyncio


@register(outgoing=True, pattern=r"^\.tm(?: |$)(.*)")
async def _(event):
    chat = "@TempMailBot"
    await event.edit("`Sedang Memprosess...`")
    async with bot.conversation(chat) as conv:
        try:
            response = conv.wait_event(events.NewMessage(
                incoming=True,
                from_users=220112646
            )
            )
            await conv.send_message("/start")
            await asyncio.sleep(1)
            await conv.send_message("Generate New")
            response = await response
            ((response).reply_markup.rows[2].buttons[0].url)
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit("`Mohon buka blokir` @TempMailBot `lalu coba lagi`")
            return
        await event.edit(f"**LINUX TEMPMAIL** ~ `{response.message.message}`\n\n[KLIK DISINI UNTUK VERIFIKASI]({sayauserbot})")


CMD_HELP.update({"tempmail": "**Modules:** __Temp Mail__\n\n🐧CMD🐧: `.tm`"
                 "\n**Penjelasan:** Mendapatkan Email Gratis Dari Temp Mail"})
