--CREATE TABLE IF NOT EXISTS users (
--    id INTEGER PRIMARY KEY AUTOINCREMENT,
--    username TEXT,
--    email TEXT,
--    password TEXT
--);

--WITH RECURSIVE
--    generate_user(id) AS (
--        SELECT 1
--        UNION ALL
--        SELECT id + 1 FROM generate_user WHERE id < 800000
--    )
--INSERT INTO users (username, email, password)
--SELECT
--    'user' || id,
--    'user' || id || '@example.com',
--    'password' || (id + 100)
--FROM generate_user;

--CREATE INDEX idx_customers_name
--ON users(username);

--PRAGMA index_list('username');

SELECT * FROM users WHERE username = "user1"