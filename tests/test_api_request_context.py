from playwright.sync_api import *

def test_api_user_request_context(playwright: Playwright):
    
    api_context = playwright.request.new_context(
        ignore_https_errors=True
        )

    response =  api_context.get("https://dummyjson.com/users/1")

    user_data = response.json()
    print(user_data)

    assert "firstName" in user_data
    assert user_data["firstName"] == "Emily"
    assert "lastName" in user_data
    assert user_data["lastName"] == "Johnson"   
