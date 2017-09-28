PRAGMA foreign_keys=on;

CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    password TEXT,
    email TEXT,
    firstname TEXT,
    lastname TEXT,
    UNIQUE(username),
    UNIQUE(email)
);

CREATE TABLE sessions (
    id INTEGER PRIMARY KEY,
    cookie TEXT NOT NULL,
    user_id INTEGER NOT NULL,
    UNIQUE(cookie),
    FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE
);
