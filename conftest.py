import pytest
from datetime import datetime

from src.catsRequests import Cat
from src.readEnv import API_KEY


@pytest.fixture(scope='function', autouse=False)
def auth():
    return API_KEY


@pytest.fixture(scope="class", autouse=False)
def cat():
    return Cat()


@pytest.hookimpl(tryfirst=True)
def pytest_html_report_title(report):
    now = datetime.now()
    report.title = f'Test Report - {now.strftime("%Y-%m-%d")}'

