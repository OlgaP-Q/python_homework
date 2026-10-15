from sqlalchemy import text


def test_add_teacher(db_session, cleanup_teachers):
    """Тест добавления учителя."""
    db_session.execute(
        text("INSERT INTO teacher (email, group_id) VALUES (:email, :gid)"),
        {"email": "test_teacher_add@example.com", "gid": None},
    )
    db_session.commit()

    result = db_session.execute(
        text("SELECT email FROM teacher WHERE email = :email"),
        {"email": "test_teacher_add@example.com"},
    ).fetchone()

    assert result is not None
    assert result[0] == "test_teacher_add@example.com"


def test_update_teacher(db_session, cleanup_teachers):
    """Тест изменения email учителя."""
    db_session.execute(
        text("INSERT INTO teacher (email, group_id) VALUES (:email, :gid)"),
        {"email": "test_teacher_old@example.com", "gid": None},
    )
    db_session.commit()

    db_session.execute(
        text(
            "UPDATE teacher SET email = :new WHERE email = :old"
        ),
        {"new": "test_teacher_new@example.com",
         "old": "test_teacher_old@example.com"},
    )
    db_session.commit()

    result = db_session.execute(
        text("SELECT email FROM teacher WHERE email = :email"),
        {"email": "test_teacher_new@example.com"},
    ).fetchone()

    assert result is not None
    assert result[0] == "test_teacher_new@example.com"


def test_delete_teacher(db_session):
    """Тест удаления учителя."""
    db_session.execute(
        text("INSERT INTO teacher (email, group_id) VALUES (:email, :gid)"),
        {"email": "test_teacher_del@example.com", "gid": None},
    )
    db_session.commit()

    db_session.execute(
        text("DELETE FROM teacher WHERE email = :email"),
        {"email": "test_teacher_del@example.com"},
    )
    db_session.commit()

    count = db_session.execute(
        text("SELECT COUNT(*) FROM teacher WHERE email = :email"),
        {"email": "test_teacher_del@example.com"},
    ).scalar()

    assert count == 0
