import uuid
import pytest


# Общая фикстура: создаёт проект через PageObject
@pytest.fixture
def existing_project(projects_api):
    return projects_api.create_and_get()


# ==================== POST /projects ====================

class TestCreateProject:

    def test_create_project_positive(self, projects_api):
        title = f"pytest-project-{uuid.uuid4().hex[:8]}"

        resp = projects_api.create_project(title)

        assert resp.status_code == 201
        assert "id" in resp.json()

    def test_create_project_negative_missing_title(self, projects_api):
        resp = projects_api.create_project_raw({})

        assert resp.status_code in (400, 422)
        assert "error" in resp.json()


# ==================== PUT /projects/{id} ====================

class TestUpdateProject:

    def test_update_project_positive(self, projects_api, existing_project):
        project_id = existing_project["id"]
        new_title = f"pytest-updated-{uuid.uuid4().hex[:8]}"

        resp = projects_api.update_project(project_id, new_title)
        assert resp.status_code == 200

        get_resp = projects_api.get_project(project_id)
        assert get_resp.status_code == 200
        assert get_resp.json().get("title") == new_title

    def test_update_project_negative_invalid_id(self, projects_api):
        fake_id = "00000000-0000-0000-0000-000000000000"

        resp = projects_api.update_project(fake_id, "should-not-exist")

        assert resp.status_code == 404
        assert "error" in resp.json()


# ==================== GET /projects/{id} ====================

class TestGetProject:

    def test_get_project_positive(self, projects_api, existing_project):
        project_id = existing_project["id"]

        resp = projects_api.get_project(project_id)

        assert resp.status_code == 200
        data = resp.json()
        assert data.get("id") == project_id
        assert "title" in data

    def test_get_project_negative_not_found(self, projects_api):
        fake_id = "00000000-0000-0000-0000-000000000000"

        resp = projects_api.get_project(fake_id)

        assert resp.status_code == 404
        assert "error" in resp.json()
