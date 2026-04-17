# SauceDemo Playwright Automation

This project demonstrates a automated testing framework using **Python** and **Playwright**.

## 🚀 Key Improvements (2026 Update)
* **Page Object Model (POM):** Decoupled test logic from page elements for better maintainability.
* **Pytest Integration:** Leveraged Pytest's powerful fixtures and assertions for standardized test execution.
* **E-commerce Flow:** Automated the full end-to-end journey from Login to Purchase Confirmation.

## 📂 Project Structure
* `page/`: Contains all Page Objects (Address Books for selectors and actions).
* `test_sauce_demo.py`: The main test suite using the Pytest framework.
* `main.py`: Legacy script for standalone execution.

## 🛠️ Setup & Execution
1. Install dependencies: `pip install -r requirements.txt`
2. Install browsers: `playwright install`
3. Run tests: `pytest --headed`
