import pytest
from page.login_page import LoginPage
from page.inventory_page import InventoryPage
from page.cart_page import CartPage
from page.checkout_page import CheckoutPage


def test_complete_purchase_flow(page):
    """
    Test Goal: Verify a user can log in and complete a full purchase flow.
    """
    # 1. Login
    login = LoginPage(page)
    login.navigate()
    login.login("standard_user", "secret_sauce")

    # 2. Add product to cart
    inventory = InventoryPage(page)
    inventory.add_backpack_to_cart()
    inventory.go_to_cart()

    # 3. Handle Cart page
    cart = CartPage(page)
    cart.proceed_to_checkout()

    # 4. Fill and finish checkout
    checkout = CheckoutPage(page)
    checkout.fill_checkout_info("John", "Lam", "22222")
    checkout.finish_checkout()

    # 5. Assertion: The "Moment of Truth" for any test
    # We check if the successful header exists and contains the expected text
    success_text = page.locator(".complete-header").text_content()
    assert success_text == "Thank you for your order!"