use its2026;

# libri

create table libri (
	libro_id int primary key auto_increment,
    titolo varchar(50) not null,
    pagine int not null default 0,
    prezzo decimal(5,2) not null default 0,
    editore_id int not null
);

describe libri;

# editori

create table editori (
	editore_id int primary key auto_increment,
    nome varchar(30) not null,
    email varchar(100),
    contatto varchar(200)
);

insert into editori (nome, email, contatto) values('Mondadori', 'vendite@mondadori.it', 'Sig. Giovanni 345.67.89.102');

insert into libri (titolo, editore_id) values ('Io robot', 1);
insert into libri (titolo, editore_id) values ('Egli robot', 2);
update libri set editore_id = 1 where libro_id = 2;

select 
	libri.titolo, 
    editori.nome 
    from libri, editori
    where libri.editore_id = editori.editore_id;

ALTER TABLE libri
ADD CONSTRAINT fk_libri_editori FOREIGN KEY (editore_id)
REFERENCES editori(editore_id);




