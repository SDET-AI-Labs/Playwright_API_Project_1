import pytest
from playwright.sync_api import *

@pytest.fixture
def api_context_setup(playwright: Playwright) -> APIRequestContext:
    api_context = playwright.request.new_context(
        ignore_https_errors=True,
        base_url="https://dummyjson.com"
    )
    yield api_context
    api_context.dispose()

def test_api_user_search_query(api_context_setup: APIRequestContext):
    query = "Johnson"
    response = api_context_setup.get(f"/users/search?q={query}")
    user_datas = response.json()

    print("Users found: ", user_datas["total"])

    for user in user_datas["users"]:
        assert query in user["firstName"] or query in user["lastName"]
        print(f"User: {user['firstName']} {user['lastName']}")
    assert response.ok


