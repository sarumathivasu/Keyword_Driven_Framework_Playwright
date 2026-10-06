def open_url(page,url):
    page.goto(url)

def enter_text(page,locator,text):
    page.locator(locator).fill(text)

def click(page,locator):
    page.locator(locator).click()

def select_option(page,locator,value):
    page.locator(locator).select_option(value)

# def verify_text(page,locator,expected_text):
#     actual_text=page.locator(locator).inner_text()
#     assert actual_text == expected_text


def verify_url(page, expected_url):
    print("Actual URL:", page.url)
    print("Expected URL:", expected_url)

    assert page.url == expected_url

