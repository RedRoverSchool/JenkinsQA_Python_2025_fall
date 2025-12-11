from playwright.sync_api import expect



def test_tc_21_009_01_create_new_view(page, new_view):

    expect(page.get_by_text(new_view)).to_be_visible()
