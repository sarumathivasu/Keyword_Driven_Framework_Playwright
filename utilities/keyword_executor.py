# import json
# from keywords.browser_keywords import open_url

# with open("test_data/login_steps.json") as file:
#     steps=json.load(file)

# for step in steps:
#     keyword=step["keyword"]
#     print(keyword)


# keyword_map={
#     "OPEN_URL":open_url
# }
# keyword="OPEN_URL"
# function=keyword_map[keyword]
# print(function)


# from playwright.sync_api import sync_playwright
# from keywords.browser_keywords import open_url

# with sync_playwright() as p:

#     browser = p.chromium.launch(headless=False)

#     page = browser.new_page()

#     open_url(page, "https://www.saucedemo.com/")

#     page.wait_for_timeout(3000)

#     browser.close()





# import json
# from playwright.sync_api import sync_playwright
# from keywords.browser_keywords import open_url,enter_text,click


# with open("test_data/login_data.json") as file:
#     test_data = json.load(file)


# with sync_playwright() as p:

#     browser = p.chromium.launch(headless=False)

#     page = browser.new_page()

#     url = test_data["url"]

#     open_url(page, url)
#     enter_text(page, "input[name='username']", test_data["username"])
#     enter_text(page,"input[name='password']",test_data["password"])
#     click(page,"button:has-text('Login')")

#     page.wait_for_timeout(3000)

#     browser.close()





# import json

# from playwright.sync_api import sync_playwright

# from keywords.browser_keywords import open_url, enter_text, click,verify_url


# with open("test_data/login_data.json") as file:
#     test_data = json.load(file)

# with open("test_data/login_steps.json") as file:
#     steps = json.load(file)


# keyword_map = {
#     "OPEN_URL": open_url,
#     "ENTER_TEXT": enter_text,
#     "CLICK": click,
#     "VERIFY_URL":verify_url
# }


# with sync_playwright() as p:

#     browser = p.chromium.launch(headless=False)

#     page = browser.new_page()

#     for step in steps:

#         keyword = step["keyword"]

#         function = keyword_map[keyword]

#         if keyword == "OPEN_URL":

#             function(page, test_data["url"])

#         elif keyword == "ENTER_TEXT":

#             locator = step["locator"]

#             data_key = step["data"]

#             value = test_data[data_key]

#             function(page, locator, value)

#         elif keyword == "CLICK":

#             locator = step["locator"]

#             function(page, locator)

#         elif keyword == "VERIFY_URL":
#             expected_url = step["expected_url"]
#             function(page, expected_url)

#     page.wait_for_timeout(3000)

#     browser.close()


# with fixtures
import json

from keywords.browser_keywords import (
    open_url,
    enter_text,
    click,
    verify_url
)


def execute_keywords(page):

    with open("test_data/login_data.json") as file:
        test_data = json.load(file)

    with open("test_data/login_steps.json") as file:
        steps = json.load(file)

    keyword_map = {
        "OPEN_URL": open_url,
        "ENTER_TEXT": enter_text,
        "CLICK": click,
        "VERIFY_URL": verify_url
    }

    for step in steps:

        keyword = step["keyword"]

        function = keyword_map[keyword]

        if keyword == "OPEN_URL":

            function(page, test_data["url"])

        elif keyword == "ENTER_TEXT":

            locator = step["locator"]

            data_key = step["data"]

            value = test_data[data_key]

            function(page, locator, value)

        elif keyword == "CLICK":

            locator = step["locator"]

            function(page, locator)

        elif keyword == "VERIFY_URL":

            expected_url = step["expected_url"]

            function(page, expected_url)