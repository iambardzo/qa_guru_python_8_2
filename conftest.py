import pytest


@pytest.fixture(scope="session")
def user():
    print("Тестовый пользователь перед тестом")

    yield

    print("Откат тестового пользователя")