def test_manage_jenkins_blocks_availability(page):
    page.goto("/manage/")

    """Collect blocks on Manage Jenkins page from requirements"""
    blocks_to_test = [
        "System Configuration",
        "Security",
        "Status Information",
        "Troubleshooting",
        "Tools and Actions"
    ]

    """Collect actual list of blocks on Manage Jenkins page"""
    blocks_on_page = [block.text_content() for block in page.locator("h2[class='jenkins-section__title']").all()]

    """Empty list to collect missed blocks on Manage Jenkins page"""
    blocks_missed = []

    """Collect missed blocks"""
    for block in blocks_to_test:
        if block not in blocks_on_page:
            blocks_missed.append(block)

    assert blocks_missed == [], f"Blocks missed: {', '.join(blocks_missed)}"

