from repitapi.api.base import RepitAPI
from repitapi.api.twitchobject import *

BASE_URL = 'twitchdata/'
TWITCH_USER_URL = BASE_URL + 'twitch_user/'
CHANNEL_URL = BASE_URL + 'channel/'
STREAMER_URL = BASE_URL + 'streamer/'
GAME_URL = BASE_URL + 'game/'
VIDEO_URL = BASE_URL + 'video/'
CLIP_URL = BASE_URL + 'clip/'
EMOTICON_URL = BASE_URL + 'emoticon/'
CHAT_URL = BASE_URL + 'chat/'
MESSAGE_URL = BASE_URL + 'message/'


class BaseTwitchObjectAPI(RepitAPI):
    def __init__(self, path, constructor):
        self.constructor = constructor
        self.path = path
        super().__init__()

    def get_objects(self, params=None, limit=100, offset=0):
        if limit != 100:
            params['limit'] = limit
        if offset != 0:
            params['offset'] = offset
        response = self._request_get(self.path, params)
        return [self.constructor(**x) for x in response]

    def get_object(self, pk):
        response = self._request_get(self.path + str(pk))
        return self.constructor(**response)

    def post_object(self, data):
        response = self._request_post(self.path, data)
        return response

    def put_object(self, pk, data):
        response = self._request_put(self.path + str(pk), data)
        return response

    def delete_object(self, pk):
        response = self._request_delete(self.path + str(pk))
        return response


class TwitchUserAPI(BaseTwitchObjectAPI):
    def __init__(self):
        super().__init__(TWITCH_USER_URL, TwitchUser)


class ChannelAPI(BaseTwitchObjectAPI):
    def __init__(self):
        super().__init__(CHANNEL_URL, Channel)


class StreamerAPI(BaseTwitchObjectAPI):
    def __init__(self):
        super().__init__(STREAMER_URL, Streamer)


class GameAPI(BaseTwitchObjectAPI):
    def __init__(self):
        super().__init__(GAME_URL, Game)


class VideoAPI(BaseTwitchObjectAPI):
    def __init__(self):
        super().__init__(VIDEO_URL, Video)


class ClipAPI(BaseTwitchObjectAPI):
    def __init__(self):
        super().__init__(CLIP_URL, Clip)


class EmoticonAPI(BaseTwitchObjectAPI):
    def __init__(self):
        super().__init__(EMOTICON_URL, Emoticon)


class ChatAPI(BaseTwitchObjectAPI):
    def __init__(self):
        super().__init__(CHAT_URL, Chat)


class MessageAPI(BaseTwitchObjectAPI):
    def __init__(self):
        super().__init__(MESSAGE_URL, Message)


class TwitchDataAPI:
    def __init__(self):
        self._twitch_user = None
        self._channel = None
        self._streamer = None
        self._game = None
        self._video = None
        self._clip = None
        self._emoticon = None
        self._chat = None
        self._message = None
        super().__init__()

    @property
    def twitch_user(self):
        if not self._twitch_user:
            self._twitch_user = TwitchUserAPI()
        return self._twitch_user

    @property
    def channel(self):
        if not self._channel:
            self._channel = ChannelAPI()
        return self._channel
    
    @property
    def streamer(self):
        if not self._streamer:
            self._streamer = StreamerAPI()
        return self._streamer
    
    @property
    def game(self):
        if not self._game:
            self._game = GameAPI()
        return self._game
    
    @property
    def video(self):
        if not self._video:
            self._video = VideoAPI()
        return self._video
    
    @property
    def clip(self):
        if not self._clip:
            self._clip = ClipAPI()
        return self._clip

    @property
    def emoticon(self):
        if not self._emoticon:
            self._emoticon = EmoticonAPI()
        return self._emoticon

    @property
    def chat(self):
        if not self._chat:
            self._chat = ChatAPI()
        return self._chat

    @property
    def message(self):
        if not self._message:
            self._message = MessageAPI()
        return self._message



