from playwright.sync_api import Page, expect, BrowserContext

def test_ing_cookies(page: Page, context: BrowserContext, browser: BrowserContext):

    page.goto("https://ing.pl")

    #captcha checkbox check
    hcaptcha_frame = page.frame_locator("iframe[src*='hcaptcha.com']")
    checkbox = hcaptcha_frame.locator("#checkbox")
    checkbox.wait_for(state="visible", timeout=10000)
    checkbox.click()

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





