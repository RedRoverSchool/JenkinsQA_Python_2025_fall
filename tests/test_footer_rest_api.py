import re
from playwright.sync_api import expect


def test_verify_rest_api_link(page):

    page.goto("/")

    rest_api_link = page.locator("a.jenkins-button--tertiary", has_text="REST API")


    expect(rest_api_link).to_be_visible()

    expect(rest_api_link).to_have_attribute("href", "api/")

    rest_api_link.click()


    expect(page).to_have_url(re.compile("api/"))

    expect(page.locator("h1")).to_contain_text("REST API")