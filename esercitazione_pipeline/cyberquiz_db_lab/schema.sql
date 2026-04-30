PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS attempt_answers;

DROP TABLE IF EXISTS attempts;

DROP TABLE IF EXISTS questions;

DROP TABLE IF EXISTS categories;

DROP TABLE IF EXISTS users;

CREATE TABLE users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT NOT NULL UNIQUE,
  created_at TEXT NOT NULL DEFAULT (datetime ('now'))
);

CREATE TABLE categories (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL UNIQUE
);

CREATE TABLE questions (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  category_id INTEGER NOT NULL,
  difficulty INTEGER NOT NULL CHECK (difficulty BETWEEN 1 AND 5),
  question_text TEXT NOT NULL,
  option_a TEXT NOT NULL,
  option_b TEXT NOT NULL,
  option_c TEXT NOT NULL,
  option_d TEXT NOT NULL,
  correct_option TEXT NOT NULL CHECK (correct_option IN ('A', 'B', 'C', 'D')),
  FOREIGN KEY (category_id) REFERENCES categories (id) ON DELETE CASCADE
);

CREATE TABLE attempts (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER NOT NULL,
  started_at TEXT NOT NULL DEFAULT (datetime ('now')),
  ended_at TEXT,
  duration_seconds INTEGER NOT NULL DEFAULT 0 CHECK (duration_seconds >= 0),
  score INTEGER NOT NULL DEFAULT 0 CHECK (score >= 0),
  FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
);

CREATE TABLE attempt_answers (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  attempt_id INTEGER NOT NULL,
  question_id INTEGER NOT NULL,
  user_answer TEXT NOT NULL CHECK (user_answer IN ('A', 'B', 'C', 'D')),
  is_correct INTEGER NOT NULL CHECK (is_correct IN (0, 1)),
  FOREIGN KEY (attempt_id) REFERENCES attempts (id) ON DELETE CASCADE,
  FOREIGN KEY (question_id) REFERENCES questions (id) ON DELETE CASCADE
);

DROP TRIGGER IF EXISTS trg_update_score;

CREATE TRIGGER trg_update_score
AFTER INSERT ON attempt_answers
BEGIN
UPDATE attempts
SET
  score = score + NEW.is_correct
WHERE
  id = NEW.attempt_id;

END;

DROP TRIGGER IF EXISTS trg_duration;

CREATE TRIGGER trg_duration
AFTER
UPDATE OF ended_at ON attempts WHEN NEW.ended_at IS NOT NULL
BEGIN
UPDATE attempts
SET
  duration_seconds = CAST(
    (
      julianday (NEW.ended_at) - julianday (NEW.started_at)
    ) * 86400 AS INTEGER
  )
WHERE
  id = NEW.id;

END;


DROP VIEW IF EXISTS v_user_stats;

CREATE VIEW v_user_stats AS
SELECT
  u.id AS user_id,
  u.username,
  COUNT(a.id) AS attempts_count,
  AVG(a.score) AS avg_score,
  MAX(a.score) AS best_score
FROM
  users u
  LEFT JOIN attempts a ON a.user_id = u.id
GROUP BY
  u.id,
  u.username;