--CREATE EXTENSION pgcrypto;

DROP TABLE IF EXISTS reviews;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS books;

CREATE TABLE users (
	id SERIAL UNIQUE NOT NULL,
	username VARCHAR UNIQUE NOT NULL,
	password VARCHAR NOT NULL,
	fav_genre VARCHAR DEFAULT null,
	date_joined TIMESTAMP NOT NULL,
	is_admin BOOLEAN DEFAULT False
);

CREATE TABLE books (
	isbn VARCHAR PRIMARY KEY UNIQUE NOT NULL,
	title VARCHAR NOT NULL,
	author VARCHAR NOT NULL,
	edition INTEGER,
	genre VARCHAR,
	media_type VARCHAR
);

CREATE TABLE reviews (
	isbn VARCHAR NOT NULL,
	review VARCHAR NOT NULL,
	usr VARCHAR NOT NULL,
	rating VARCHAR NOT NULL,
	CONSTRAINT fk_usr FOREIGN KEY (usr) REFERENCES users(username),
	CONSTRAINT fk_isbn FOREIGN KEY (isbn) REFERENCES books(isbn)
);

SELECT * FROM reviews;
SELECT * FROM books;
SELECT * FROM users;

SELECT * FROM reviews INNER JOIN books ON reviews.isbn = books.isbn;
