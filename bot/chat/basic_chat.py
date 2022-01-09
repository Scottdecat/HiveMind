import random

import bot.injector as injector

from ..services.chat_service import ChatService
from .chat_interface import ChatInterface


class BasicChat(ChatInterface):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.chat_service: ChatService = injector.inject(ChatService)
    async def on_step(self, iteration):
        if iteration == 0:
            await self.greet()

    async def greet(self):
        await self.chat_service.send('Hi, uh.. it would be kind of cool if you lost to the zerg army haha, we\'re pretty tough')
        await self.chat_service.send('You should run in fear! *small and weak voice*')
        await self.chat_service.send('Shut up zergling stop using the intercom')
        await self.chat_service.send('*clears throat*')
        await self.chat_service.send('I am the Swarm Lord, leader of the swarm, bow before me or be crushed by my hordes!')
