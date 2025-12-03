def get_name_loc(name):
    return f"td > a[href='job/{name}/']"

def test_TC_03_001_01(page):
    page.goto("/")

    toggle_loc = 'label[for="enable-disable-project"]'
    save_btn_loc = 'button[formnovalidate="formNoValidate"]'
    main_page_loc = 'span[class="jenkins-mobile-hide"]'

    item_link = page.locator('td > a[href^="job/"]').last
    new_item_name = item_link.text_content()

    status_icon_loc = page.locator(f'tr#job_{new_item_name} svg[tooltip]').nth(0)
    before_status = status_icon_loc.get_attribute("tooltip")

    page.get_by_role("link", name=new_item_name, exact=True).click()
    page.get_by_role("link", name="Configure").click()
    page.locator(toggle_loc).click()
    page.locator(save_btn_loc).click()
    page.locator(main_page_loc).click()

    status_icon_loc = page.locator(f'tr#job_{new_item_name} svg[tooltip]').nth(0)
    after_status = status_icon_loc.get_attribute("tooltip")

    assert before_status != after_status