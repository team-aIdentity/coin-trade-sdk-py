from decimal import Decimal

from exchange import Exchange, Order, OrderBook


class Okx(Exchange):
    def __init__(self, api_key: str, secret: str, password: str):
        super().__init__(
            api_key=api_key,
            secret=secret,
            password=password
        )

    def buy(self, symbol: str, price: Decimal, amount: Decimal) -> Order:
        pass

    def sell(self, symbol: str, price: Decimal, amount: Decimal) -> Order:
        pass

    def withdraw_to(self, symbol: str, price: Decimal, amount: Decimal) -> bool:
        pass

    def make_sign(self) -> str:
        pass

    def order_fetch(self, ord_id: str, symbol: str) -> Order:
        pass

    def get_orderbook(self, symbol) -> OrderBook:
        pass

    def get_coin_list(self) -> list[str]:
        pass