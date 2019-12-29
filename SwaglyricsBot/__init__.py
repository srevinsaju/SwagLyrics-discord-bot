name = 'SwaglyricsBot'
__version__ = '0.0.1'


class LyricsError(Exception):

    def __init__(self, message):
        super().__init__(message)


class LyricsNotFound(LyricsError):

    def __init__(self, message):
        super().__init__(message)


class SpotifyClosed(LyricsError):

    def __init__(self, message="You are not listening to anything or Spotify is not connected to discord! \n "
                               "Make sure you have enabled status in Settings -> Connections -> Spotify -> Display "
                               "Spotify as your status"):
        super().__init__(message)