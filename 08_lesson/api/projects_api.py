import uuid
import requests


class ProjectsAPI:
    """
    PageObject для эндпоинта /projects YouGile API.
    Инкапсулирует URL, заголовки, тело запроса и проверки статусов.
    """

    def __init__(self, base_url: str, session: requests.Session, headers: dict):
        self.base_url = base_url.rstrip("/")
        self.session = session
        self.headers = headers

    # ---------- POST ----------

    def create_project(self, title: str | None = None) -> requests.Response:
        """Создаёт проект. Если title не передан — генерирует уникальный.
        Возвращает Response для возможных дополнительных проверок в тесте."""
        if title is None:
            title = f"pytest-project-{uuid.uuid4().hex[:8]}"

        return self.session.post(
            f"{self.base_url}/projects",
            json={"title": title},
            headers=self.headers,
        )

    # ---------- PUT ----------

    def update_project(self, project_id: str, title: str) -> requests.Response:
        """Обновляет название проекта по id."""
        return self.session.put(
            f"{self.base_url}/projects/{project_id}",
            json={"title": title},
            headers=self.headers,
        )

    # ---------- GET ----------

    def get_project(self, project_id: str) -> requests.Response:
        """Получает проект по id."""
        return self.session.get(
            f"{self.base_url}/projects/{project_id}",
            headers=self.headers,
        )

    # ---------- Хелперы ----------

    def create_and_get(self, title: str | None = None) -> dict:
        """Создаёт проект и возвращает его JSON.
        Удобно для фикстур, которым нужен id."""
        resp = self.create_project(title)
        assert resp.status_code == 201, f"Не удалось создать проект: {resp.text}"
        return resp.json()



 # ----------Отдельный метод для негативного теста POST ----------

    def create_project_raw(self, payload: dict) -> requests.Response:
        """Создаёт проект с произвольным телом — для негативных тестов."""
        return self.session.post(
            f"{self.base_url}/projects",
            json=payload,
            headers=self.headers,
        )
