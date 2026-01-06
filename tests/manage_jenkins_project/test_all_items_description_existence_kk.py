def test_all_items_description_existence(page):
    page.goto("/manage/")

    items_to_check = {}

    blocks = page.locator("div[class='jenkins-section__item'] dl").all()
    for block in blocks:
        items_to_check[block.locator("dt").text_content()] = block.locator("dd").first.text_content()

    items_without_description = []

    for item in items_to_check:
        if items_to_check[item] == "":
            items_without_description.append(item)

    assert items_without_description == [], f"Items without description: {items_without_description}"

    # main-panel > section:nth-child(5) > div > div:nth-child(1) > a > dl > dd:nth-child(2)
    # / html / body / div[2] / div / section[2] / div / div[1] / a / dl / dd[1]

    # tools_and_actions_block_actual_content = []
    #
    # page_blocks = page.locator("section[class='jenkins-section jenkins-section--bottom-padding']").all()
    #
    #
    # items_missed = []
    #
    # for block in page_blocks:
    #     if block.locator("h2[class='jenkins-section__title']").text_content() == "Tools and Actions":
    #         block_items = block.locator("div[class='jenkins-section__item']").all()
    #
    #         for item in block_items:
    #             tools_and_actions_block_actual_content.append(item.locator("dt").text_content())
    #
    # for item in tools_and_actions_block_expected_content:
    #     if item not in tools_and_actions_block_actual_content:
    #         items_missed.append(item)
    #
    # assert items_missed == [], f"Items missed: {', '.join(items_missed)}"