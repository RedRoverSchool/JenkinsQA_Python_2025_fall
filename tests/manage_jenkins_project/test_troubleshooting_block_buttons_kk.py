def test_troubleshooting_block_buttons(page):
    page.goto("/manage/")

    troubleshooting_block_expected_content = [
        "Manage Old Data"
    ]

    troubleshooting_block_actual_content = []

    page_blocks = page.locator("section[class='jenkins-section jenkins-section--bottom-padding']").all()


    items_missed = []

    for block in page_blocks:
        if block.locator("h2[class='jenkins-section__title']").text_content() == "Troubleshooting":
            block_items = block.locator("div[class='jenkins-section__item']").all()

            for item in block_items:
                troubleshooting_block_actual_content.append(item.locator("dt").text_content())

    for item in troubleshooting_block_expected_content:
        if item not in troubleshooting_block_actual_content:
            items_missed.append(item)

    assert items_missed == [], f"Items missed: {', '.join(items_missed)}"