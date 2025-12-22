from playwright.sync_api import expect


def test_05_002_03(page,new_folder):
    folder_name = new_folder
    configure_loc = "svg[class='icon-gear icon-md']"
    health_metric_button_loc = "button[data-section-id='health-metrics']"
    advanced_metric_button_loc = "button[class*='advanced-button']"
    add_metric_button_loc = "button[class*='hetero']"
    hamburger_loc = "div[class='dd-handle']"

    page.goto(f"/job/{folder_name}/")
    page.click(configure_loc)
    page.locator(health_metric_button_loc).click()
    page.click(advanced_metric_button_loc)
    page.click(add_metric_button_loc)
    dropdown = page.locator("div.jenkins-dropdown")
    dropdown.click()

    page.locator("div.jenkins-dropdown-item:has-text('Child item with the given name')")
    page.locator("div.jenkins-dropdown-item:has-text('Child item with worst health')")


    """Ожидаем появление значка гамбургера"""
    expect(page.locator(hamburger_loc)).to_be_visible()