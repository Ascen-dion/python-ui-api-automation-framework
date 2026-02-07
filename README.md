# Python UI + API Automation Framework

A production-style **test automation framework template** built using:

- Python
- Pytest
- Selenium (UI automation)
- Requests (API automation)
- Page Object Model (POM)
- Wrapper layer over Selenium
- Config-driven execution
- Cross-browser support (local execution)
- GitHub Actions CI (Chrome via Docker Selenium)
- Parallel execution (pytest-xdist)
- Allure-ready reporting

This project can be used for:
- Client demos
- Automation framework starter template
- Real project foundation

---

## Project Structure

```
python-ui-api-automation-framework/
│
├── config/
├── core/
├── pages/
├── api/
├── tests/
├── docker/
├── requirements.txt
├── pytest.ini
└── README.md
```

---

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running Tests

Run all tests:

```bash
pytest
```

Run tests in parallel:

```bash
pytest -n 2
```

Run UI tests only:

```bash
pytest tests/ui
```

Run API tests only:

```bash
pytest tests/api
```

---

## Cross-Browser Execution (Local)

Update:

```
config/config.yaml
```

Example:

```yaml
browser: firefox
```

Supported browsers:

- chrome
- firefox
- edge

---

## GitHub Actions Execution

CI pipeline:
- Uses Docker Selenium Chrome
- Runs pytest automatically on push

Workflow file:

```
.github/workflows/ci.yml
```

---

## Selenium Wrapper Example

Instead of raw Selenium commands like:

```python
driver.find_element(...).click()
```

Use the wrapper:

```python
self.ui.click(locator)
self.ui.enter_text(locator, "Laptop")
```

Benefits:
- Built-in waits
- Cleaner tests
- Reusable actions
- Less flaky automation

---

## Page Object Example

```python
amazon.search("laptop")
amazon.verify_results_loaded()
```

Tests remain readable and maintainable.

---

## API Automation Example

```python
api = APIClient()
response = api.get("https://httpbin.org/get")
assert response.status_code == 200
```

---

## Docker Execution

Build image:

```bash
docker build -t automation-framework .
```

Run tests:

```bash
docker run automation-framework
```

---

## Reporting (Allure Ready)

Generate results:

```bash
pytest --alluredir=reports
```

Serve report:

```bash
allure serve reports
```

---

## Recommended Future Enhancements

- Screenshot capture on failure
- RemoteWebDriver execution switch
- Environment profiles (dev / qa / prod)
- Test data management layer
- Retry mechanism
- Selenium Grid support
- Advanced logging
- Playwright adapter option
