import copy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


INITIAL_ACTIVITIES = copy.deepcopy(activities)


def reset_activities() -> None:
    activities.clear()
    activities.update(copy.deepcopy(INITIAL_ACTIVITIES))


@pytest.fixture(autouse=True)
def restore_activities_state():
    reset_activities()
    yield
    reset_activities()


@pytest.fixture()
def client():
    with TestClient(app) as test_client:
        yield test_client