class Television:
    """
    A class to represent a television with basic functionality
    such as power toggle, mute, channel, and volume control.
    """

    # Class variables
    MIN_VOLUME: int = 0  # Minimum volume constant
    MAX_VOLUME: int = 2  # Maximum volume constant
    MIN_CHANNEL: int = 0  # Minimum channel constant
    MAX_CHANNEL: int = 3  # Maximum channel constant

    def __init__(self) -> None:
        """
        Initializes the Television with default settings.
        The TV is off, not muted, volume at MIN_VOLUME,
        and channel at MIN_CHANNEL.
        """
        self.__status: bool = False  # Power status of the TV (False means off)
        self.__muted: bool = False  # Mute status of the TV (False means not muted)
        self.__volume: int = Television.MIN_VOLUME  # Current volume level
        self.__channel: int = Television.MIN_CHANNEL  # Current channel

    def power(self) -> None:
        """
        Toggles the power status of the television.
        If the TV is off, it turns on, and vice versa.
        """
        self.__status = not self.__status

    def mute(self) -> None:
        """
        Toggles the mute status of the television.
        Only works if the TV is on.
        """
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """
        Increases the channel number by 1.
        If the channel is at MAX_CHANNEL, it wraps around to MIN_CHANNEL.
        Only works if the TV is on.
        """
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        Decreases the channel number by 1.
        If the channel is at MIN_CHANNEL, it wraps around to MAX_CHANNEL.
        Only works if the TV is on.
        """
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        Increases the volume level by 1.
        If muted, it unmutes the TV.
        Volume does not go above MAX_VOLUME.
        Only works if the TV is on.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Decreases the volume level by 1.
        If muted, it unmutes the TV.
        Volume does not go below MIN_VOLUME.
        Only works if the TV is on.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Returns a string representation of the television's state.
        Displays the power status, current channel, and volume.
        If muted, the volume is displayed as MIN_VOLUME.
        
        Returns:
            str: A formatted string representing the TV's state.
        """
        volume_display: int = Television.MIN_VOLUME if self.__muted else self.__volume
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {volume_display}"
