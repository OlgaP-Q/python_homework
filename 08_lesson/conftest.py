import os
import pytest
import requests

from api.projects_api import ProjectsAPI

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

BASE_URL = "https://ru.yougile.com/api-v2"


@pytest.fixture(scope="session")
def api_token():
    token = os.environ.get("YOUGILE_API_TOKEN")
    if not token or token == "your_api_key_here":
        pytest.skip("Переменная YOUGILE_API_TOKEN не задана")
    return token


@pytest.fixture(scope="session")
def auth_headers(api_token):
    return {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_token}",
    }


@pytest.fixture(scope="session")
def session():
    with requests.Session() as s:
        yield s


@pytest.fixture(scope="session")
def projects_api(session, auth_headers):
    """PageObject для /projects, доступный всем тестам."""
    return ProjectsAPI(BASE_URL, session, auth_headers)


@pytest.fixture
def existing_project(projects_api, request):
    """
    Создаёт проект и регистрирует очистку.
    YouGile API v2 не поддерживает DELETE /projects/{id},
    поэтому очистка «мягкая»: пробуем, но не падаем на 404/405.
    """
    project = projects_api.create_and_get()

    def cleanup():
        resp = projects_api.delete_project(project["id"])
        if resp.status_code not in (200, 204, 404, 405):
            print(
                f"Cleanup: проект {project['id']} не удалён. "
                f"Статус: {resp.status_code}. "
                f"YouGile API v2 не поддерживает удаление — удалите вручную."
            )

    request.addfinalizer(cleanup)
    return project
