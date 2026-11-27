# T15-E11 - Challenge: test a shopping cart end to end
#
# Write a complete test suite for the shopping cart. Read the rules in the docstring of `cart.py` first. Put shared fixtures in `conftest.py`:
#
# - `tea` = `Product("T1", "Tea", 4.50)`, `book` = `Product("B1", "Book", 12.00)`, `lamp` = `Product("L1", "Lamp", 35.00)`;
# - `cart`: an empty `Cart`;
# - `filled_cart`: the `cart` with two teas and one book (subtotal 21.00).
#
# Group the tests in classes (`TestProduct`, `TestEmptyCart`, `TestAddAndRemove`, `TestSubtotal`, `TestCoupons`, `TestShippingAndTax`, `TestTotal`, `TestCheckout`). Cover every rule:
#
# - Product: a negative price raises `ValueError`; a product is frozen (assigning to `price` raises `dataclasses.FrozenInstanceError`).
# - Empty cart: empty, no items, quantity 0, subtotal / shipping / total all 0, checkout raises `EmptyCartError`.
# - Add and remove: add one; adding the same product twice adds the quantities; quantity 0 and -1 are rejected (parametrize); remove some, remove all (`None`), removing more than there is removes the product, unknown SKU raises `KeyError`, removing quantity 0 raises `ValueError` and changes nothing.
# - Subtotal: 21.00 for the filled cart; three items at 0.10 give exactly `0.3` (rounding).
# - Coupons: `SAVE10` takes 10 percent (2.10 off 21.00); the code is trimmed and case-insensitive; `FIVER` takes 5.00 off; `FIVER` is refused below a subtotal of 20.00 and accepted at exactly 20.00; unknown code raises `ValueError`; a second coupon is refused and the first stays; no coupon means no discount.
# - Shipping and tax: shipping 4.99 below 50, free at exactly 50.00; the free-shipping test uses the price AFTER the coupon (55.00 with `SAVE10` is 49.50, so shipping is charged); tax is 8 percent of the price after the coupon (1.68, and 1.51 with `SAVE10`).
# - Totals (parametrize with `pytest.param(..., id=...)`): filled cart is 27.67 without a coupon, 25.40 with `SAVE10`, 22.27 with `FIVER`; two lamps (70.00) cost 75.60 with free shipping. Compare money with `pytest.approx`.
# - Checkout: the receipt dictionary has `items`, `subtotal`, `discount`, `tax`, `shipping` and `total` (check the whole dictionary for the `SAVE10` case); after checkout the cart is empty and the coupon is gone; the cart can be used again.
#
# Finally run `py -m pytest --cov=cart --cov-report=term-missing --cov-fail-under=90` and make sure the coverage is above 90 percent.
#
# Behaviours to test
#
# See the list above; the table gives the numbers to expect.
#
# | Case | Expected |
# |------|----------|
# | filled cart, no coupon | subtotal 21.00, tax 1.68, shipping 4.99, total 27.67 |
# | filled cart, `SAVE10` | discount 2.10, tax 1.51, total 25.40 |
# | filled cart, `FIVER` | discount 5.00, total 22.27 |
# | 2 lamps | subtotal 70.00, shipping 0.00, total 75.60 |
# | 55.00 item with `SAVE10` | price after coupon 49.50, shipping 4.99 |
