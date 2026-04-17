class CartPage:
    def __init__(self, page):
        self.page = page
        self._checkout_button = page.locator("[data-test='checkout']")

    def proceed_to_checkout(self):
        # Action: Click the checkout button to go to the information page
        self._checkout_button.click()