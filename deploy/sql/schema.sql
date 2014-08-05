/*
    Lunaport Agent database 0.0.1
    https://github.com/greggyNapalm/lunaport_agent
    SQLite v3
*/

CREATE TABLE status (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
);

CREATE TABLE tool (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
);

CREATE TABLE job (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    status_id INTEGER,
    path TEXT UNIQUE,
    hook_enabled BOOLEAN,
    hook_addr TEXT,
    added_at DATE,
    started_at DATE,
    finished_at DATE,
    FOREIGN KEY(status_id) REFERENCES status(id)
);
