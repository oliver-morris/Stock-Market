


class Candlestick:
    def __init__(self, date, data):
        self.date = date
        self.open = None
        self.high = None
        self.low = None
        self.close = None
        self.volume = None
        self.__initialise_candlestick(data)

    def __initialise_candlestick(self, data):
        self.open = data["1. open"]
        self.high = data["2. high"]
        self.low = data["3. low"]
        self.close = data["4. close"]
        self.volume = data["5. volume"]