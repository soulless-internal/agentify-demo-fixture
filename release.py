def release_total_cents(line_items):
    """Total synthetic order lines, each (unit price in cents, quantity)."""
    return sum(price * quantity for price, quantity in line_items)
