def test_tc_05_002_02(page,new_folder):
    folder_name = new_folder
    """Метрики выпадающего списка из acceptance Criteria"""
    metric = ["Child item with the given name", "Child item with worst health"]

    health_metric_button_loc = "button[data-section-id='health-metrics']"
    health_metric_dropdown_button_loc = "button[class*='advancedButton']"
    add_metric_button_loc = "button[class*='hetero-list-add']"
    dropdown_text_loc = "button.jenkins-dropdown__item"

    page.goto(f"/job/{folder_name}/configure")
    page.click(health_metric_button_loc)
    page.click(health_metric_dropdown_button_loc)
    page.click(add_metric_button_loc)
    """Получить все опции выпадающего меню"""
    all_options_button = page.locator(dropdown_text_loc).all_inner_texts()
    """Проверка, что все опции из Acceptance Criteria присутствуют в выпадающем меню"""
    assert all_options_button == metric
