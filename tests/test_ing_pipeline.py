from playwright.sync_api import Page, expect

def test_ing_cookies(page: Page, context):

    page.goto("https://ing.pl")

    check = page.get_by_role("checkbox", name="a11y-label")
    if check.get_attribute("aria-checked") == "false":
        check.click()

    page.get_by_role("button", name="Dostosuj").click()

    toggle = page.locator('[name="CpmAnalyticalOption"]')
    if toggle.get_attribute("aria-checked") == "false":
        toggle.click()

    expect(toggle).to_be_checked()

    page.get_by_role("button", name="Zaakceptuj zaznaczone").click()

    cookies = context.cookies()

    cookie_GDPR = next((c for c in cookies if c['name'] == 'cookiePolicyGDPR'), None)
    cookie_GDPR_details = next((c for c in cookies if c['name'] == 'cookiePolicyGDPR__details'), None)


    assert cookie_GDPR is not None, "cookiePolicyGDPR not found"
    assert cookie_GDPR_details is not None, "cookiePolicyGDPR__details not found"

    assert cookie_GDPR["value"] == "3", "cookiePolicyGDPR has unexpected value"
    assert cookie_GDPR_details["value"] != "", "cookiePolicyGDPR__details should not be empty"





