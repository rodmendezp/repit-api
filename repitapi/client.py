from repitapi.api.twitchdata import TwitchDataAPI
from repitapi.api.highlight import Highlight


class RepitClient(object):
    def __init__(self):
        self._twitch_data = None
        self._highlight = None

    @property
    def twitch_data(self):
        if not self._twitch_data:
            self._twitch_data = TwitchDataAPI()
        return self._twitch_data

    @property
    def highlight(self):
        if not self._highlight:
            self._highlight = Highlight()
        return self._highlight
