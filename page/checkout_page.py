class CheckoutPage:
    def __init__(self, page):
        self.page = page
        # Define the locators for the checkout form
        self._first_name = page.locator("[data-test='firstName']")
        self._last_name = page.locator("[data-test='lastName']")
        self._zip_code = page.locator("[data-test='postalCode']")
        self._continue_btn = page.locator("[data-test='continue']")
        self._finish_btn = page.locator("[data-test='finish']")

    def fill_checkout_info(self, first, last, zip):
        # Action: Fill the form and click continue
        self._first_name.fill(first)
        self._last_name.fill(last)
        self._zip_code.fill(zip)
        self._continue_btn.click()

    def finish_checkout(self):
        # Action: Click the finish button
        self._finish_btn.click()