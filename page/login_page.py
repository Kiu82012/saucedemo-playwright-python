class LoginPage:
    def __init__(self, page):
        # Initialize the page object with the playwright page instance
        self.page = page

        # Define Locators: Centralize all selectors here for easy maintenance
        self._username_field = page.locator("#user-name")
        self._password_field = page.locator("#password")
        self._login_btn = page.locator("#login-button")

    def navigate(self):
        # Action: Go to the SauceDemo login page
        self.page.goto("https://www.saucedemo.com/")

    def login(self, username, password):
        # Action: Perform a complete login flow
        self._username_field.fill(username)
        self._password_field.fill(password)
        self._login_btn.click()