import requests


def test_verify_posts_for_user():
    user_id = 3
    response = requests.get(f"https://jsonplaceholder.typicode.com/posts?userId={user_id}")
    assert response.status_code == 200
    posts = response.json()
    assert len(posts) == 10, f"Expected {10} posts, got {len(posts)}"

