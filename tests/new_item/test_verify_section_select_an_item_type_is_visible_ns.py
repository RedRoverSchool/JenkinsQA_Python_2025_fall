from pages.new_item_page import NewItemPage



def test_verify_section_select_an_item_type_is_visible(page):
    """TC_POM_01.004.01 | 01.004.01 | New Item > Select an Item type > Verify section "Select an item type" is visible
    """
    new_item_page = NewItemPage(page)

    new_item_page.open_new_item_page()

    assert new_item_page.is_new_item_page_opened(), "New Item page was not opened"





