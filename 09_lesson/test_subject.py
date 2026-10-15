from sqlalchemy import text


def test_add_subject(db_session, cleanup_subjects):
    """Тест добавления предмета."""
    db_session.execute(
        text("INSERT INTO subject (subject_title) VALUES (:title)"),
        {"title": "TEST_Mathematics"},
    )
    db_session.commit()

    result = db_session.execute(
        text("SELECT subject_title FROM subject WHERE subject_title = :t"),
        {"t": "TEST_Mathematics"},
    ).fetchone()

    assert result is not None
    assert result[0] == "TEST_Mathematics"


def test_update_subject(db_session, cleanup_subjects):
    """Тест изменения названия предмета."""
    db_session.execute(
        text("INSERT INTO subject (subject_title) VALUES (:title)"),
        {"title": "TEST_OldSubject"},
    )
    db_session.commit()

    db_session.execute(
        text(
            "UPDATE subject SET subject_title = :new "
            "WHERE subject_title = :old"
        ),
        {"new": "TEST_NewSubject", "old": "TEST_OldSubject"},
    )
    db_session.commit()

    result = db_session.execute(
        text("SELECT subject_title FROM subject WHERE subject_title = :t"),
        {"t": "TEST_NewSubject"},
    ).fetchone()

    assert result is not None
    assert result[0] == "TEST_NewSubject"


def test_delete_subject(db_session):
    """Тест удаления предмета."""
    db_session.execute(
        text("INSERT INTO subject (subject_title) VALUES (:title)"),
        {"title": "TEST_ToDelete"},
    )
    db_session.commit()

    db_session.execute(
        text("DELETE FROM subject WHERE subject_title = :t"),
        {"t": "TEST_ToDelete"},
    )
    db_session.commit()

    count = db_session.execute(
        text("SELECT COUNT(*) FROM subject WHERE subject_title = :t"),
        {"t": "TEST_ToDelete"},
    ).scalar()

    assert count == 0
