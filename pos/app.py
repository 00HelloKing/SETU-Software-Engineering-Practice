from __future__ import annotations
from .domain import ProductDescription
from .inventory import Inventory
from .register import Register

def seed_inventory(inv: Inventory) -> None:
    inv.add_product(ProductDescription("A100", "Apple", 3.50), 100)
    inv.add_product(ProductDescription("B200", "Bread", 5.00), 50)
    inv.add_product(ProductDescription("M300", "Milk", 4.20), 60)

def process_sale_demo(reg: Register) -> None:
    print("\n=== Process Sale ===")
    reg.start_new_sale()
    while True:
        item_id = input("Enter item id (or 'done'): ").strip()
        if item_id.lower() == "done":
            break
        qty = int(input("Quantity: ").strip())
        total = reg.enter_item(item_id, qty)
        print(f"Running total: {total:.2f}")
    total_due = reg.end_sale()
    print(f"Total due: {total_due:.2f}")
    paid = float(input("Cash paid: ").strip())
    change = reg.make_payment(paid)
    print(f"Change due: {change:.2f}")
    print("Receipt printed.\n")

def handle_return_demo(reg: Register) -> None:
    print("\n=== Handle Return ===")
    reg.start_return()
    while True:
        item_id = input("Enter return item id (or 'done'): ").strip()
        if item_id.lower() == "done":
            break
        qty = int(input("Quantity: ").strip())
        refund_total = reg.enter_return_item(item_id, qty)
        print(f"Refund total so far: {refund_total:.2f}")
    refund_due = reg.end_return()
    print(f"Refund due: {refund_due:.2f}")
    amount = reg.refund()
    print(f"Refunded: {amount:.2f}")
    print("Return receipt printed.\n")

def main() -> None:
    inv = Inventory()
    seed_inventory(inv)
    reg = Register(register_id="R1", inventory=inv)

    while True:
        print("1) Process Sale")
        print("2) Handle Return")
        print("3) Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            process_sale_demo(reg)
        elif choice == "2":
            handle_return_demo(reg)
        elif choice == "3":
            break
        else:
            print("Invalid choice.\n")

if __name__ == "__main__":
    main()
