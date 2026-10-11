from sqlalchemy import text


def test_add_user(db_session, cleanup_users):
    """Тест добавления пользователя."""
    db_session.execute(
        text(
            'INSERT INTO "users" (user_email, subject_id) '
            "VALUES (:email, :subject_id)"
        ),
        {"email": "test_add@example.com", "subject_id": None},
    )
    db_session.commit()

    result = db_session.execute(
        text('SELECT user_email FROM "users" WHERE user_email = :email'),
        {"email": "test_add@example.com"},
    ).fetchone()

    assert result is not None
    assert result[0] == "test_add@example.com"


def test_update_user(db_session, cleanup_users):
    """Тест изменения email пользователя."""
    db_session.execute(
        text(
            'INSERT INTO "users" (user_email, subject_id) '
            "VALUES (:email, :subject_id)"
        ),
        {"email": "test_upd_old@example.com", "subject_id": None},
    )
    db_session.commit()

    db_session.execute(
        text(
            'UPDATE "users" SET user_email = :new '
            "WHERE user_email = :old"
        ),
        {"new": "test_upd_new@example.com", "old": "test_upd_old@example.com"},
    )
    db_session.commit()

    result = db_session.execute(
        text('SELECT user_email FROM "users" WHERE user_email = :email'),
        {"email": "test_upd_new@example.com"},
    ).fetchone()

    assert result is not None
    assert result[0] == "test_upd_new@example.com"


def test_delete_user(db_session):
    """Тест удаления пользователя."""
    db_session.execute(
        text(
            'INSERT INTO "users" (user_email, subject_id) '
            "VALUES (:email, :subject_id)"
        ),
        {"email": "test_delete@example.com", "subject_id": None},
    )
    db_session.commit()

    db_session.execute(
        text('DELETE FROM "users" WHERE user_email = :email'),
        {"email": "test_delete@example.com"},
    )
    db_session.commit()

    count = db_session.execute(
        text('SELECT COUNT(*) FROM "users" WHERE user_email = :email'),
        {"email": "test_delete@example.com"},
    ).scalar()

    assert count == 0
