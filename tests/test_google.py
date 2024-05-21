import pytest
from playwright.sync_api import Page
from pages.google import Google


class TestGoogle:
    @pytest.fixture(scope="function", autouse=True)
    def before_each_after_each(self, page: Page):
        # BEFORE
        page.goto("https://google.com")

        yield
        # AFTER
        page.close()

    def test_search(self, page: Page):
        google_page = Google(page)
        google_page.click_on_english()
        google_page.is_search_bar_visible()
        google_page.search("playwright python")
        google_page.click_on_search()
