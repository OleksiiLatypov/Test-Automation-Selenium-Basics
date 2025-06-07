import requests

"""
Task 1.
Provide the Python code based on the api_task.py which will test 2 scenarios:
1. Let’s pretend that you’ve loaded the test data for the user with Id=3 and generated 10 valid posts. Verify that 10 posts were created for user 3.
Use: https://jsonplaceholder.typicode.com/ (Resources section)
"""


def test_verify_posts_for_user():
    user_id = 3
    response = requests.get(f"https://jsonplaceholder.typicode.com/posts?userId={user_id}")
    assert response.status_code == 200
    posts = response.json()
    assert len(posts) == 10, f"Expected {10} posts, got {len(posts)}"
