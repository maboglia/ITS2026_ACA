create database  libreria;
use libreria;
-- table editori
create table editori(
	editore_id int primary key auto_increment,
	nome varchar(100),
	contatto varchar(100)
);

-- table libri
create table libri(
	libro_id int primary key auto_increment,
	titolo varchar(100),
	prezzo decimal(6, 2),
	pagine int,
	editore_id int
);

-- table autori
create table autori(
	autore_id int primary key auto_increment,
	nome varchar(30),
	cognome varchar(50),
	nazionalita char(2)
);


-- table autori_libri
create table autori_libri(
	autore_id int,
	libro_id int,
	primary key(autore_id, libro_id)
);


insert into editori
select * from editore;

insert into libri
select * from libro;

insert into autori
select * from autore;

insert into autori_libri
select * from autore_libro;

select * 
from libri as l, editori e
where l.editore_id = e.editore_id 
;

select count(*) from editori;

select l.*, e.nome 
from libri l right join editori e on l.editore_id = e.editore_id;

select
l.titolo,
concat(a.nome, ' ' ,a.cognome) as autore,
e.nome as editore
from libri l
 join editori e on l.editore_id = e.editore_id 
 join autori_libri al on l.libro_id = al.libro_id
 join autori a on a.autore_id = al.autore_id;

truncate autori_libri;

insert into autori_libri
select autore_id, libro_id from autore_libro;

use its2026;

select 
genere, 
count(nome) as totale
from games
group by genere
order by totale desc 


;
select 
platform , 
count(nome) as totale
from games
group by platform
order by totale desc 


;









