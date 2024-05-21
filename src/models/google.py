from playwright.sync_api import Page


class GoogleModel:
    def __init__(self, page: Page):
        self.page = page

    @property
    def search_field(self):
        return self.page.get_by_label(text="Search", exact=True)

    @property
    def search_btn(self):
        return self.page.get_by_role(role="button", name="Google Search")

    @property
    def english_txt(self):
        return self.page.get_by_text(text="English")
