def remove_duplicates(customer_ids):
    return set(customer_ids)

# Example data
customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]

# Remove duplicates and display unique customer IDs
print("Unique Customer IDs:", remove_duplicates(customer_ids))