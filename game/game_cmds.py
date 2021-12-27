import redis
import json
import asyncio


async def start(self):
    await self.channel_layer.group_send(
        'user',
        {
            'type': 'send_group',
            'message': 'start:'
        }
    )


async def set_players(players):
    r = redis.Redis('localhost')
    r.set('players', players)
    print(players)
    print(type(players))


async def get_players(self):
    r = redis.Redis('localhost')
    players = r.get('players')
    players = json.loads(players)
    for i in players:
        i['role'] = ""
    players = json.dumps(players)
    if type(players) == bytes:
        players = players.decode()
    await self.channel_layer.group_send(
        'user',
        {
            'type': 'send_group',
            'message': 'get_players:' + players
        }
    )


async def get_players_all(self):
    r = redis.Redis('localhost')
    players = r.get('players')
    if type(players) == bytes:
        players = players.decode()
    await self.channel_layer.group_send(
        'admin',
        {
            'type': 'send_group',
            'message': 'get_players_all:' + players
        }
    )


async def kill_player(self, name):
    r = redis.Redis('localhost')
    players = r.get('players')
    players = json.loads(players)
    for i in range(len(players)):
        if players[i]['name'] == name:
            del players[i]
            break
    players = json.dumps(players)
    r.set('players', players)
    # await self.channel_layer.group_send(
    #     'admin',
    #     {
    #         'type': 'send_group',
    #         'message': 'kill_player:1'
    #     }
    # )
    await get_players_all(self)
    await asyncio.sleep(.1)
    await get_players(self)


async def show_stream(self):
    await self.channel_layer.group_send(
        'user',
        {
            'type': 'send_group',
            'message': 'show_stream:1'
        }
    )


async def start_vote(self):
    await self.channel_layer.group_send(
        'user',
        {
            'type': 'send_group',
            'message': 'start_vote:1'
        }
    )


async def end_vote(self):
    await self.channel_layer.group_send(
        'user',
        {
            'type': 'send_group',
            'message': 'end_vote:1'
        }
    )


async def start_vote_2(self):
    await self.channel_layer.group_send(
        'user',
        {
            'type': 'send_group',
            'message': 'start_vote_2:1'
        }
    )


async def end_vote_2(self):
    await self.channel_layer.group_send(
        'user',
        {
            'type': 'send_group',
            'message': 'end_vote_2:1'
        }
    )


async def game_over(self):
    await self.channel_layer.group_send(
        'user',
        {
            'type': 'send_group',
            'message': 'game_over:1'
        }
    )