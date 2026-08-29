# -*- coding: utf-8 -*-
"""풀이 진행 기록을 저장하는 간단한 SQLite 저장소."""
import os
import sqlite3

DB_PATH = os.path.join(os.path.dirname(__file__), "data", "progress.db")

_SCHEMA = """
CREATE TABLE IF NOT EXISTS submissions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user TEXT NOT NULL,
    problem_id INTEGER NOT NULL,
    passed INTEGER NOT NULL,
    total INTEGER NOT NULL,
    solved INTEGER NOT NULL,
    code TEXT NOT NULL,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
);
"""


def get_connection():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    con = sqlite3.connect(DB_PATH, check_same_thread=False)
    con.row_factory = sqlite3.Row
    con.execute(_SCHEMA)
    con.commit()
    return con


def record_submission(con, user, problem_id, passed, total, code):
    solved = 1 if passed == total and total > 0 else 0
    con.execute(
        "INSERT INTO submissions (user, problem_id, passed, total, solved, code) "
        "VALUES (?, ?, ?, ?, ?, ?)",
        (user, problem_id, passed, total, solved, code),
    )
    con.commit()


def get_solved_ids(con, user):
    rows = con.execute(
        "SELECT DISTINCT problem_id FROM submissions WHERE user = ? AND solved = 1",
        (user,),
    ).fetchall()
    return {r["problem_id"] for r in rows}


def get_best_result(con, user, problem_id):
    row = con.execute(
        "SELECT passed, total, solved, code FROM submissions "
        "WHERE user = ? AND problem_id = ? ORDER BY solved DESC, passed DESC, id DESC LIMIT 1",
        (user, problem_id),
    ).fetchone()
    return dict(row) if row else None


def get_attempt_count(con, user, problem_id):
    row = con.execute(
        "SELECT COUNT(*) AS c FROM submissions WHERE user = ? AND problem_id = ?",
        (user, problem_id),
    ).fetchone()
    return row["c"] if row else 0
