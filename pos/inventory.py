from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, Optional
from .domain import ProductDescription

@dataclass
class Inventory:
    # item_id -> (ProductDescription, stock_qty)
    catalog: Dict[str, ProductDescription] = field(default_factory=dict)
    stock: Dict[str, int] = field(default_factory=dict)

    def add_product(self, product: ProductDescription, quantity: int) -> None:
        self.catalog[product.item_id] = product
        self.stock[product.item_id] = self.stock.get(product.item_id, 0) + quantity

    def get_product(self, item_id: str) -> Optional[ProductDescription]:
        return self.catalog.get(item_id)

    def remove_stock(self, item_id: str, quantity: int) -> None:
        if self.stock.get(item_id, 0) < quantity:
            raise ValueError("Not enough inventory.")
        self.stock[item_id] -= quantity

    def add_stock(self, item_id: str, quantity: int) -> None:
        self.stock[item_id] = self.stock.get(item_id, 0) + quantity
