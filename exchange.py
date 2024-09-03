import uuid
from abc import abstractmethod
from decimal import Decimal
from typing import Optional


class Order:
    symbol: str
    price: Decimal
    amount: Decimal
    ord_type: str
    ord_id: Optional[str]
    status: Optional[str]

    def __init__(
            self,
            symbol: str,
            price: Decimal,
            amount: Decimal,
            ord_type: str,
            ord_id: Optional[str] = None,
            status: Optional[str] = None
    ):
        self.symbol = symbol
        self.price = price
        self.amount = amount
        self.ord_type = ord_type
        self.ord_id = ord_id
        self.status = status


class OrderBook:
    pass


class Exchange:
    api_key: str
    secret: str
    password: Optional[str]

    def __init__(
            self,
            api_key: str,
            secret: str,
            password: Optional[str] = None
    ):
        self.api_key = api_key
        self.secret = secret
        self.password = password

    @abstractmethod
    def buy(self, symbol: str, price: Decimal, amount: Decimal) -> Order:
        print("this is cex buying method")
        return Order(
            symbol="btc/usdt",
            price=Decimal(50000.0),
            amount=Decimal(1.0),
            ord_type="buy",
            ord_id=uuid.uuid4().hex,
            status="closed"
        )

    @abstractmethod
    def sell(self, symbol: str, price: Decimal, amount: Decimal) -> Order:
        print("this is cex selling method")
        return Order(
            symbol="btc/krw",
            price=Decimal(100000000.0),
            amount=Decimal(1.0),
            ord_type="sell",
            ord_id=uuid.uuid4().hex,
            status="closed"
        )

    @abstractmethod
    def withdraw_to(self, symbol: str, price: Decimal, amount: Decimal) -> bool:
        print("this is cex withdraw method")
        return True

    @abstractmethod
    def make_sign(self) -> str:
        print("this is make_sign method for private api")
        return uuid.uuid4().hex

    @abstractmethod
    def order_fetch(self, ord_id: str, symbol: str) -> Order:
        print("this is order fetch method for check status of order")
        return Order(
            symbol="usdt/btc",
            price=Decimal(50000.0),
            amount=Decimal(1.0),
            ord_type="buy",
            ord_id=uuid.uuid4().hex,
            status="open"
        )

    @abstractmethod
    def get_orderbook(self, symbol) -> OrderBook:
        print("this is method for get order book")
        return OrderBook()

    @abstractmethod
    def get_coin_list(self) -> list[str]:
        print("this is method for get cex coin pair list")
        return [
            "btc/usdt",
            "btc/krw",
            "usdt/krw",
        ]