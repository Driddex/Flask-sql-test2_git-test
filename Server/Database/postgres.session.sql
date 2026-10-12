CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(20),
    email VARCHAR(20),
    is_active BOOLEAN DEFAULT TRUE
);