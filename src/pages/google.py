from models.google import GoogleModel
from playwright.sync_api import Page, expect


class Google(GoogleModel):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

    def is_search_bar_visible(self) -> None:
        expect(self.search_field).to_be_visible()

    def search(self, text: str) -> None:
        self.search_field.fill(text)

    def click_on_search(self) -> None:
        self.search_btn.click()

    def click_on_english(self) -> None:
        self.english_txt.click()
