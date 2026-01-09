from __future__ import annotations
from dataclasses import dataclass
from typing import Optional
from .domain import Sale, Return
from .inventory import Inventory

@dataclass
class Register:
    register_id: str
    inventory: Inventory
    current_sale: Optional[Sale] = None
    current_return: Optional[Return] = None

    # --- Process Sale (Controller-like operations) ---
    def start_new_sale(self) -> None:
        self.current_sale = Sale()

    def enter_item(self, item_id: str, quantity: int) -> float:
        if not self.current_sale:
            raise ValueError("No sale started.")
        product = self.inventory.get_product(item_id)
        if not product:
            raise ValueError("Unknown item_id.")
        self.inventory.remove_stock(item_id, quantity)
        self.current_sale.add_item(product, quantity)
        return self.current_sale.total()

    def end_sale(self) -> float:
        if not self.current_sale:
            raise ValueError("No sale started.")
        return self.current_sale.total()

    def make_payment(self, amount: float) -> float:
        if not self.current_sale:
            raise ValueError("No sale started.")
        self.current_sale.make_payment(amount)
        return self.current_sale.change_due()

    # --- Handle Return ---
    def start_return(self) -> None:
        self.current_return = Return()

    def enter_return_item(self, item_id: str, quantity: int) -> float:
        if not self.current_return:
            raise ValueError("No return started.")
        product = self.inventory.get_product(item_id)
        if not product:
            raise ValueError("Unknown item_id.")
        self.inventory.add_stock(item_id, quantity)
        self.current_return.add_return_item(product, quantity)
        return self.current_return.refund_total()

    def end_return(self) -> float:
        if not self.current_return:
            raise ValueError("No return started.")
        return self.current_return.refund_total()

    def refund(self) -> float:
        if not self.current_return:
            raise ValueError("No return started.")
        amount = self.current_return.refund_total()
        self.current_return.refund(amount)
        return amount
