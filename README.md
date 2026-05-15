# ING Cookie testing with python playwright 

The project contains a repeatable automated test that verifies the cookie management process on the `ing.pl` website. The tests were implemented in Python using the Playwright framework (`pytest-playwright`). 
The project also includes a CI/CD configuration that enables parallel test execution across multiple browsers within the GitHub Actions environment.

## Test scope & explanation

The automated test executes the following end-to-end user flow to verify cookie compliance on the website:

1. The test launches a clean browser instance and creates a dedicated context.
2. Navigates directly to the: `https://ing.pl`.
3. Locates and clicks the **"Dostosuj"**  button using its accessible role name.
4. Enables Analytical Cookies:
   - Pinpoints the specific switch element responsible for analytical tracking (`[name="CpmAnalyticalOption"]`).
   - Checks the current state using the `aria-checked` attribute. If it is set to `"false"`, the test performs a `.click()` action to toggle it on.
   - Asserts that the switch status is now successfully checked using Playwright's `expect(toggle).to_be_checked()`.
5.  Locates and clicks the **"Zaakceptuj zaznaczone"** button to save the updated cookie configuration.
6. Cookie Storage Verification:
   - Retrieves the full list of active cookies directly from the browser context via `context.cookies()`.
   - Isolates two critical privacy-related cookies: `cookiePolicyGDPR` and `cookiePolicyGDPR__details`.
   - Asserts that both cookies are successfully created and present in the storage  and checks their values.

## Requirements

- Python 3.8 or newer
- Pip packet manager

## Installation

1. Download or clone repository<br>
2. Create and activate virtual environment in project directory
```bash
python -m venv venv
.\venv\Scripts\activate
```
3. Install dependencies
```bash
pip install -r requirements.txt
playwright install
```

## Usage

To run test:

```bash
pytest tests/test_ing.py
```

To run test on multiple browsers in the same time:
```bash
pytest tests/test_ing.py --browser chromium --browser firefox --browser webkit -n 3
```

## Pipeline (Github Actions)

The project is equipped with full CI/CD automation (configured in the `.github/workflows/playwright.yml` file).

Tests are triggered automatically on every `push` and `pull_request` event to the main branch. By leveraging a build matrix (`matrix`), the pipeline runs tests simultaneously across three major browser engines:
- **Chromium**
- **Firefox**
- **Webkit** 

Additionally, thanks to the `pytest-xdist` plugin and the `-n auto` flag, the tests are parallelized at the CPU process level, which minimizes the overall pipeline execution time.

## Issue with CI/CD pipeline

While deploying the test to the cloud, local tests encountered the additional security infrastructure barriers of the live ING production environment (Captcha). 
It's most likely due to the fact that GitHub pipelines tried to connect from foreign ip (outside of Poland) which results in additional security check on the webpage.

