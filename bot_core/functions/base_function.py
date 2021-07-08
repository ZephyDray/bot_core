from abc import ABC, abstractmethod

from telethon import TelegramClient
from telethon.events.common import EventBuilder, EventCommon


class Functionality(ABC):
    @property
    @abstractmethod
    def event(self) -> EventBuilder:
        raise NotImplementedError

    def register(self, client: TelegramClient):
        client.add_event_handler(self.call, self.event)

    @abstractmethod
    async def call(self, event: EventCommon):
        raise NotImplementedError
