from unittest.mock import MagicMock, patch

import pytest
from src.services import sync_user_profile_data


@patch("src.services.db.update_user_records")
@patch("src.services.requests.get")
def test_profile_sync_success(mock_request, mock_db):

    response = MagicMock()
    response.status_code = 200
    response.json.return_value = {
        "email": "hk@gmail.com",
        "city": "Chennai"
    }

    mock_request.return_value = response

    result = sync_user_profile_data(777)

    assert result == {
        "status": "Synced successfully",
        "user_id": 777
    }

    mock_request.assert_called_once_with(
        "https://api.example.com/v1/profiles/777",
        timeout=5
    )

    mock_db.assert_called_once_with(
        777,
        email="hk@gmail.com",
        city="Chennai"
    )


@patch("src.services.requests.get")
def test_profile_sync_failure(mock_request):

    response = MagicMock()
    response.status_code = 500

    mock_request.return_value = response

    with pytest.raises(RuntimeError):
        sync_user_profile_data(777)