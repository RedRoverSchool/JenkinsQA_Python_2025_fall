def test_system_message_on_main_page(page):
    system_message_text = "test message"

    manage_jenkins_link_locator = "//*[text()='Manage Jenkins']/parent::a"
    configure_system_link_locator = "//dt[text()='System']/../parent::a"
    system_message_field_locator = "//*[text()='System Message']/following-sibling::div/textarea"
    configure_system_save_button_locator = "//button[contains(text(), 'Save')]"
    system_message_locator = "//*[@id='systemmessage']"

    page.goto("/")

    page.locator(manage_jenkins_link_locator).click()
    page.locator(configure_system_link_locator).click()
    page.locator(system_message_field_locator).fill(system_message_text)
    page.locator(configure_system_save_button_locator).click()

    assert page.locator(system_message_locator).text_content() == system_message_text
