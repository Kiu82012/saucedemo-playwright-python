from playwright.sync_api import sync_playwright
import time


def run_test():
    # 1. Start Playwright and launch browser
    with sync_playwright() as p:
        # headless=False means you will see the browser window
        # slow_mo=800 means it will wait 0.8s between each action so you can follow
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()

        print("Step 1: Navigating to SauceDemo website...")
        page.goto("https://www.saucedemo.com/")

        # Step 2: Login
        print("Step 2: Performing Login...")
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")

        # Step 3: Add product to cart
        print("Step 3: Adding 'Sauce Labs Backpack' to cart...")
        page.click('[data-test="add-to-cart-sauce-labs-backpack"]')

        # Step 4: Go to Cart
        print("Step 4: Opening Shopping Cart...")
        page.click(".shopping_cart_link")
        # Take a screenshot of the cart
        page.screenshot(path="1_cart_view.png")

        # Step 5: Checkout - Part 1 (Information)
        print("Step 5: Entering Checkout Information...")
        page.click('[data-test="checkout"]')
        page.fill('[data-test="firstName"]', "John")
        page.fill('[data-test="lastName"]', "Doe")
        page.fill('[data-test="postalCode"]', "123456")
        page.click('[data-test="continue"]')

        # Step 6: Checkout - Part 2 (Overview)
        print("Step 6: Reviewing Order...")
        page.screenshot(path="2_checkout_overview.png")
        page.click('[data-test="finish"]')

        # Step 7: Verify Success and Take Final Screenshot
        print("Step 7: Verifying Order Completion...")
        success_text = page.locator(".complete-header").text_content()

        if success_text == "Thank you for your order!":
            print("TEST PASSED: Order completed successfully.")
            page.screenshot(path="3_final_success.png")
            print("Final screenshot saved: 3_final_success.png")
        else:
            print(f"TEST FAILED: Expected success message but got '{success_text}'")

        time.sleep(3)
        browser.close()


if __name__ == "__main__":
    run_test()