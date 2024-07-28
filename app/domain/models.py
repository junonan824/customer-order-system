from dataclasses import dataclass


@dataclass
class Order:
    id: int
    customer_id: int
    status: str
    total_amount: float


@dataclass
class Payment:
    id: int
    order_id: int
    status: str
    amount: float
