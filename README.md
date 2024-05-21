# playwright-page-object-model

Implementation of playwright with page object model(POM)

### Models

Models contain object that we wanted to interact. Here, we utilize python `@property` to define the elements.

```python
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

```

### Pages

Pages contain the page we wanted to interact. It should inherit from `models` to be able accessing element defined there. All actions such as click, fill, expect should be under this package. Later on the test, we only calling function/method from this class.

```python
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

```


### Tests

Since we have everything under pages module, in test we should just construct this and call its functions.


```python

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

```

### Notes
At this stage, our codes are tidy and maintaining them would be easier. When steps too complex, we can introduce new package to handle such ways like `handler` or `wrapper`

