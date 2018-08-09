class TwitchUser:
    def __init__(self, id, twid, name):
        self.id = id
        self.twid = twid
        self.name = name


class Channel:
    def __init__(self, id, twid):
        self.id = id
        self.twid = twid


class Streamer:
    def __init__(self, id, twitch_user, channel):
        self.id = id
        self.twitch_user = TwitchUser(**twitch_user)
        self.channel = Channel(**channel)


class Game:
    def __init__(self, id, twid, name):
        self.id = id,
        self.twid = twid
        self.name = name


class Video:
    def __init__(self, id, twid, streamer, game, recorded, length) :
        self.id = id
        self.twid = twid
        self.streamer = Streamer(**streamer)
        self.game = Game(**game)
        self.recorded = recorded
        self.length = length


class Clip:
    def __init__(self, id, twid, streamer, video, creator, offset,
                 duration, created, added, slug, title, views):
        self.id = id
        self.twid = twid
        self.streamer = Streamer(**streamer)
        self.video = Video(**video)
        self.creator = TwitchUser(**creator)
        self.offset = offset
        self.duration = duration
        self.created = created
        self.added = added
        self.slug = slug
        self.title = title
        self.views = views


class Emoticon:
    def __init__(self, id, twid, set_id, streamer, text):
        self.id = id
        self.twid = twid
        self.set_id = set_id
        self.streamer = Streamer(**streamer)
        self.text = text


class Chat:
    def __init__(self, id, video):
        self.id = id
        self.video = Video(**video)


class Message:
    def __init__(self, chat, twitch_user, text, time):
        self.chat = Chat(**chat)
        self.twitch_user = TwitchUser(**twitch_user)
        self.text = text
        self.time = time
