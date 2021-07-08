import json
from typing import List

from telethon import TelegramClient

from bot_core.functions.base_function import Functionality
from bot_core.functions.beep import Beep


class Bot:
    def __init__(self, config_file):
        with open(config_file, "r") as c:
            config = json.load(c)
        self.client = TelegramClient(
            config["bot_name"],
            config["api_id"],
            config["api_hash"]
        )
        self.client.start(bot_token=config["bot_token"])

    @property
    def functions(self) -> List[Functionality]:
        return [Beep()]

    def start(self):
        for function in self.functions:
            function.register(self.client)
        self.client.run_until_disconnected()
