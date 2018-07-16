DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;
DROP TABLE IF EXISTS MediaType;
DROP TABLE IF EXISTS recommendations;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL,
  email TEXT NOT NULL
);

CREATE TABLE MediaType (
    mediaType TEXT PRIMARY KEY NOT NULL,
    Seq INTEGER
);
INSERT INTO MediaType VALUES ('YouTube', 1);
INSERT INTO MediaType VALUES ('Movie', 2);

CREATE TABLE recommendations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id_Recommender INTEGER NOT NULL,
    user_id_Recommendee INTEGER NOT NULL,
    media_type TEXT NOT NULL REFERENCES MediaType(mediaType),
    title TEXT NOT NULL,
    link TEXT NOT NULL,
    watched BOOLEAN NOT NULL CHECK (watched IN (0,1)) DEFAULT 0,
    message TEXT,
    sent TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id_Recommender) REFERENCES user (id),
    FOREIGN KEY (user_id_Recommendee) REFERENCES user (id)
);