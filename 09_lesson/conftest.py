import pytest
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker


DATABASE_URL = ("postgresql+psycopg2://root:9786534210KOb"
                "@localhost:5432/lesson_1_sql"
                )

engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


@pytest.fixture(scope="function")
def db_session():
    """Сессия БД с автоматическим коммитом/откатом."""
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


@pytest.fixture(scope="function")
def cleanup_users(db_session):
    """Удаляет тестовых пользователей по маркеру в email."""
    yield
    db_session.execute(
        text(
            "DELETE FROM \"users\" "
            "WHERE user_email LIKE 'test_%@example.com'"
        )
    )
    db_session.commit()


@pytest.fixture(scope="function")
def cleanup_subjects(db_session):
    """Удаляет тестовые предметы по маркеру."""
    yield
    db_session.execute(
        text("DELETE FROM subject WHERE subject_title LIKE 'TEST_%'")
    )
    db_session.commit()


@pytest.fixture(scope="function")
def cleanup_teachers(db_session):
    """Удаляет тестовых учителей по маркеру."""
    yield
    db_session.execute(
        text("DELETE FROM teacher WHERE email LIKE 'test_%@example.com'")
    )
    db_session.commit()
