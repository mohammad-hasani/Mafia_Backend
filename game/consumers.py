from channels.consumer import AsyncConsumer
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync
import channels
import json
from .game_cmds import *
from .game_cmds_user import *


class GameConsumerAdmin(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add('admin', self.channel_name)
        await self.accept()

        await self.channel_layer.group_send(
            'user',
            {
                'type': 'send_group',
                'message': 'Hallo'
            }
        )

    async def send_group(self, event):
        await self.send(text_data=event['message'])

    async def disconnect(self, code):
        await self.channel_layer.group_discard('admin', self.channel_name)
        await self.close()

    async def receive(self, text_data=None, bytes_data=None):
        print(text_data)
        data = text_data.split(':', 1)
        if data[0] == 'start':
            await start(self)
        elif data[0] == 'set_players':
            await set_players(data[1])
        elif data[0] == 'get_players_all':
            await get_players_all(self)
        elif data[0] == 'kill_player':
            await kill_player(self, data[1])
        elif data[0] == 'show_stream':
            await show_stream(self)
        elif data[0] == 'start_vote':
            await start_vote(self)
        elif data[0] == 'end_vote':
            await end_vote(self)
        elif data[0] == 'start_vote_2':
            await start_vote_2(self)
        elif data[0] == 'end_vote_2':
            await end_vote_2(self)
        elif data[0] == 'game_over':
            await game_over(self)


class GameConsumerUser(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add('user', self.channel_name)
        await self.accept()

        await self.channel_layer.group_send(
            'user',
            {
                'type': 'send_group',
                'message': 'Hallo'
            }
        )

    async def send_group(self, event):
        await self.send(text_data=event['message'])

    async def disconnect(self, code):
        await self.channel_layer.group_discard('user', self.channel_name)
        await self.close()

    async def receive(self, text_data=None, bytes_data=None):
        data = text_data.split(':', 1)
        if data[0] == 'get_players':
            await get_players(self)
        elif data[0] == 'end_vote':
            await end_vote_user(self)
        elif data[0] == 'end_vote_2':
            await end_vote_2_user(self)
        elif data[0] == 'pick_role':
            await pick_role_user(self, data[1])
        elif data[0] == 'kill_player_user':
            await kill_player_user(self, data[1])
