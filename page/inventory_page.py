class InventoryPage:
    def __init__(self, page):
        # Initialize with the playwright page instance
        self.page = page

        # Define Locators for elements in the Inventory page
        self._page_title = page.locator(".title")
        self._backpack_add_btn = page.locator('[data-test="add-to-cart-sauce-labs-backpack"]')
        self._cart_link = page.locator(".shopping_cart_link")

    def get_title(self):
        # Action: Return the header text (e.g., "Products") to verify successful login
        return self._page_title.text_content()

    def add_backpack_to_cart(self):
        # Action: Click the "Add to cart" button for the backpack
        self._backpack_add_btn.click()

    def go_to_cart(self):
        # Action: Click the shopping cart icon to navigate to the cart page
        self._cart_link.click()