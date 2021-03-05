from Connection.con_object import ws


class InfoController(object):
    def __init__(self):
        self.ws = ws

    def get_data(self):
        self.ws.subscribe_instrument_info(symbol='BTCUSD')
        while True:
            data = self.ws.get_data('instrument_info.100ms.BTCUSD')
            try:
                price = data['update'][0]['last_price_e4']/(10**4) if data else None
                print(price) if price else None
            except KeyError:
                pass


a = InfoController()
a.get_data()
