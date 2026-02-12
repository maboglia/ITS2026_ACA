SELECT * FROM its2026.studenti;

show create table studenti;

create table amici like studenti;

insert into amici select * from studenti;

select * from amici;

CREATE TABLE `studenti` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(30) NOT NULL,
  `cognome` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

alter table studenti
rename to studenti_its;

select 
	name, 
    price, 
    (price * 0.90) as 'Prezzo scontato' 
    from products
    where price > 4 and price < 10
    ;


DROP TABLE IF EXISTS studenti;

CREATE TABLE studenti (
  id INT AUTO_INCREMENT,
  nome VARCHAR(50),
  cognome VARCHAR(50),
  genere ENUM('M', 'F'),
  indirizzo VARCHAR(100),
  citta VARCHAR(50),
  provincia CHAR(2) DEFAULT 'To',
  regione VARCHAR(50) DEFAULT 'Piemonte',
  email VARCHAR(50) NOT NULL UNIQUE,
  data_nascita DATE,
  ins TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY(id)
);










