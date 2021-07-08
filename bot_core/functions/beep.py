from telethon.events import NewMessage
from telethon.events.common import EventBuilder

from bot_core.functions.base_function import Functionality


class Beep(Functionality):
    @property
    def event(self) -> EventBuilder:
        return NewMessage(pattern="beep")

    async def call(self, event: NewMessage.Event):
        await event.reply("boop")
