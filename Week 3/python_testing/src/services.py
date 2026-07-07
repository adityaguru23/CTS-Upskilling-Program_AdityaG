import requests

from . import db

def save_user_data(user_id, email, city):
    """Placeholder function for testing."""
    pass

def sync_profile(user_id):

    url = f"https://api.example.com/v1/profiles/{user_id}"
    result = requests.get(url, timeout=5)

    if result.status_code == 200:
        profile = result.json()

        db.update_user_records(
            user_id,
            email=profile.get("email"),
            city=profile.get("city")
        )

        return {
            "status": "Profile synchronized",
            "user_id": user_id
        }

    raise RuntimeError("Failed to communicate with API")