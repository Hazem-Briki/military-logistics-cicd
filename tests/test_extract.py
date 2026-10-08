from src.extract.postgresql import extract_purchase_orders


purchase_orders = extract_purchase_orders()

print(purchase_orders)
print()
print(f"Number of rows: {len(purchase_orders)}")