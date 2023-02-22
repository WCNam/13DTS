CREATE TABLE product (
	id integer PRIMARY KEY AUTOINCREMENT,
	name varchar,
	description varchar,
	size varchar,
	image varchar,
	price float,
	cat_id integer
);

CREATE TABLE category (
	id integer PRIMARY KEY AUTOINCREMENT,
	name varchar
);



