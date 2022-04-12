PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE employees(
	id INTEGER NOT NULL, 
	name VARCHAR, 
	email VARCHAR, 
	department VARCHAR, 
	salary FLOAT NOT NULL, 
	birth_date DATE
	PRIMARY KEY (id)
);
INSERT INTO employees VALUES(1,'Anakin Skywalker','skywalker@ssys.com.br','Architecture',4000.00,'1983-01-01');
INSERT INTO employees VALUES(2,'Obi-Wan Kenobi','kenobi@ssys.com.br','Back-End',3000.00,'1977-01-01');
INSERT INTO employees VALUES(3,'Leia Organa','organa@ssys.com.br','DevOps",',5000.00,'1980-01-01');
INSERT INTO employees VALUES(4,'Mateus Rodrigues','mateus@ssys.com.br','Front-End',8000.00,'1996-03-20');
INSERT INTO employees VALUES(5,'Will Smith','will@oscar.com.br','Security',10000.00,'1983-01-01');
CREATE INDEX ix_employees_id ON employees (id);
COMMIT;