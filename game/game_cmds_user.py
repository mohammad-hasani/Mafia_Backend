import redis
import json
import management.models


async def end_vote_user(self):
    print(self.scope['user'])


async def end_vote_2_user(self):
    print(self.scope['user'])


async def pick_role_user(self, data):
    data = json.loads(data)
    r = redis.Redis('localhost')
    players = r.get('players')
    players = json.loads(players)
    score = 0
    for i in range(len(players)):
        for j in range(len(data)):
            if players[i]['name'] == data[j]['name'] and players[i]['role'] == data[j]['role']:
                score += 1

    add_score = management.models.GameState()
    add_score.user = self.scope['user']
    add_score.score = score
    add_score.save()


async def kill_player_user(self, data):
    data = json.loads(data)
    r = redis.Redis('localhost')
    players = r.get('players')
    players = json.loads(players)
    score = 0
    for i in range(len(players)):
        for j in range(len(data)):
            if players[i]['name'] == data[j]['name'] and players[i]['role'] == data[j]['role'] and players[i]['role'].lower() == 'mafia':

                score += 1


    add_score = management.models.GameState()
    add_score.user = self.scope['user']
    add_score.score = score
    add_score.save()