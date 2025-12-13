

def test_05_002_01(page, new_folder):
    folder_name = new_folder
    configure_loc = "svg[class='icon-gear icon-md']"
    health_metric_button_loc = "button[data-section-id='health-metrics']"

    page.goto(f"/job/{folder_name}/")
    page.click(configure_loc)
    button_hm = page.locator(health_metric_button_loc)
    if button_hm.is_enabled():
        # Кнопка кликабельна
        button_hm.click()
    else:
        print("Кнопка неактивна")
