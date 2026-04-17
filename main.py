from playwright.sync_api import sync_playwright
from page.login_page import LoginPage
from page.inventory_page import InventoryPage
from page.checkout_page import CheckoutPage
from page.cart_page import CartPage
def run_test():
    with sync_playwright() as p:
        # Launch browser (headless=False so you can see the magic happen)
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()

        # --- TEST EXECUTION START ---

        # Step 1: Initialize Login Page and perform login
        login = LoginPage(page)
        login.navigate()
        login.login("standard_user", "secret_sauce")

        # Step 2: Verify if we are on the correct page and add product
        inventory = InventoryPage(page)

        # Assertion: Check if the title is "Products"
        if inventory.get_title() == "Products":
            print("Login Successful: Navigation verified.")

        # Perform shopping actions
        inventory.add_backpack_to_cart()
        inventory.go_to_cart()

        cart = CartPage(page)
        cart.proceed_to_checkout()

        checkout = CheckoutPage(page)
        checkout.fill_checkout_info("John","Lam","22222")
        checkout.finish_checkout()

        print("Test completed successfully!")

        # Cleanup
        browser.close()


if __name__ == "__main__":
    run_test()