# POS System (Python) — Process Sale & Handle Return

This is a small, object-oriented Point-of-Sale (POS) console application that supports:
- Process Sale (scan items, compute total, pay, print receipt, update inventory)
- Handle Return (record returned items, compute refund, refund, print return receipt, update inventory)

## Run
```bash
python -m pos.app
```

## Structure
- `pos/domain.py` — Domain model (Sale, LineItem, Return, etc.)
- `pos/inventory.py` — Inventory and product catalog
- `pos/register.py` — Register controller-like coordination
- `pos/app.py` — CLI demo
