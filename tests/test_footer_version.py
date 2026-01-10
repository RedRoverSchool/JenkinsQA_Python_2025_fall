from playwright.sync_api import expect


def test_verify_footer_version(page):

    page.goto("/")

    footer_version_btn = page.locator("footer button.jenkins-button--tertiary")

    expect(footer_version_btn).to_be_visible()

    expect(footer_version_btn).to_contain_text("Jenkins")