"""A small shopping cart. This is the code under test: do not change it.

Rules:
- Prices are floats with two decimals; every money result is rounded to 2 places.
- Adding a product that is already in the cart increases its quantity.
- One coupon at a time: SAVE10 takes 10 percent off the subtotal; FIVER takes 5.00
  off but only when the subtotal is at least 20.00.
- Tax is 8 percent and is charged on the price AFTER the coupon.
- Shipping is 4.99, or free when the subtotal AFTER the coupon is 50.00 or more.
"""

from dataclasses import dataclass

TAX_RATE = 0.08
SHIPPING_FEE = 4.99
FREE_SHIPPING_FROM = 50.00


class EmptyCartError(Exception):
    """Raised when checking out an empty cart."""


@dataclass(frozen=True)
class Product:
    sku: str
    name: str
    price: float

    def __post_init__(self):
        if self.price < 0:
            raise ValueError("price cannot be negative")


class Cart:
    def __init__(self):
        self._items = {}
        self.coupon = None

    def add(self, product, quantity=1):
        if quantity < 1:
            raise ValueError("quantity must be at least 1")
        if product.sku in self._items:
            old_product, old_quantity = self._items[product.sku]
            self._items[product.sku] = (old_product, old_quantity + quantity)
        else:
            self._items[product.sku] = (product, quantity)

    def remove(self, sku, quantity=None):
        """Remove `quantity` of a product, or all of it when quantity is None."""
        if sku not in self._items:
            raise KeyError(f"not in cart: {sku}")
        product, current = self._items[sku]
        if quantity is None or quantity >= current:
            del self._items[sku]
        elif quantity < 1:
            raise ValueError("quantity must be at least 1")
        else:
            self._items[sku] = (product, current - quantity)

    def quantity_of(self, sku):
        if sku not in self._items:
            return 0
        return self._items[sku][1]

    def item_count(self):
        return sum(quantity for _, quantity in self._items.values())

    def is_empty(self):
        return not self._items

    def subtotal(self):
        return round(
            sum(product.price * quantity for product, quantity in self._items.values()), 2
        )

    def apply_coupon(self, code):
        if self.coupon is not None:
            raise ValueError("a coupon is already applied")
        code = code.strip().upper()
        if code not in ("SAVE10", "FIVER"):
            raise ValueError(f"invalid coupon: {code}")
        if code == "FIVER" and self.subtotal() < 20.00:
            raise ValueError("FIVER needs a subtotal of at least 20.00")
        self.coupon = code

    def discount(self):
        if self.coupon == "SAVE10":
            return round(self.subtotal() * 0.10, 2)
        if self.coupon == "FIVER":
            return 5.00
        return 0.0

    def shipping(self):
        if self.is_empty():
            return 0.0
        if self.subtotal() - self.discount() >= FREE_SHIPPING_FROM:
            return 0.0
        return SHIPPING_FEE

    def tax(self):
        return round((self.subtotal() - self.discount()) * TAX_RATE, 2)

    def total(self):
        return round(self.subtotal() - self.discount() + self.tax() + self.shipping(), 2)

    def checkout(self):
        """Return a receipt dictionary and empty the cart."""
        if self.is_empty():
            raise EmptyCartError("cannot check out an empty cart")
        receipt = {
            "items": self.item_count(),
            "subtotal": self.subtotal(),
            "discount": self.discount(),
            "tax": self.tax(),
            "shipping": self.shipping(),
            "total": self.total(),
        }
        self._items = {}
        self.coupon = None
        return receipt
