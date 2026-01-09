from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional

@dataclass(frozen=True)
class ProductDescription:
    item_id: str
    description: str
    price: float

@dataclass
class SalesLineItem:
    product: ProductDescription
    quantity: int

    def subtotal(self) -> float:
        return self.product.price * self.quantity

@dataclass
class Payment:
    amount: float

@dataclass
class Sale:
    date_time: datetime = field(default_factory=datetime.now)
    line_items: List[SalesLineItem] = field(default_factory=list)
    payment: Optional[Payment] = None
    is_complete: bool = False

    def add_item(self, product: ProductDescription, quantity: int) -> None:
        if self.is_complete:
            raise ValueError("Cannot add items to a completed sale.")
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        self.line_items.append(SalesLineItem(product=product, quantity=quantity))

    def total(self) -> float:
        return round(sum(li.subtotal() for li in self.line_items), 2)

    def make_payment(self, amount: float) -> None:
        if amount < self.total():
            raise ValueError("Insufficient payment.")
        self.payment = Payment(amount=round(amount, 2))
        self.is_complete = True

    def change_due(self) -> float:
        if not self.payment:
            return 0.0
        return round(self.payment.amount - self.total(), 2)

@dataclass
class ReturnLineItem:
    product: ProductDescription
    quantity: int

    def refund_subtotal(self) -> float:
        return self.product.price * self.quantity

@dataclass
class Return:
    date_time: datetime = field(default_factory=datetime.now)
    line_items: List[ReturnLineItem] = field(default_factory=list)
    refund_payment: Optional[Payment] = None
    is_complete: bool = False

    def add_return_item(self, product: ProductDescription, quantity: int) -> None:
        if self.is_complete:
            raise ValueError("Cannot add items to a completed return.")
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        self.line_items.append(ReturnLineItem(product=product, quantity=quantity))

    def refund_total(self) -> float:
        return round(sum(li.refund_subtotal() for li in self.line_items), 2)

    def refund(self, amount: float) -> None:
        if amount != self.refund_total():
            raise ValueError("Refund amount must equal refund total.")
        self.refund_payment = Payment(amount=round(amount, 2))
        self.is_complete = True
