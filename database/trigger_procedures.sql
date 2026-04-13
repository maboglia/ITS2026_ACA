DROP PROCEDURE AddArtist;

DELIMITER $$

CREATE PROCEDURE AddArtist(IN id INT, IN nome VARCHAR(30))
BEGIN
    INSERT INTO artist (ArtistId, `name`) value (id, nome);
END $$

DELIMITER ;

CALL AddArtist(277, "Ghali");

CREATE TABLE artist_log (
	log_id int primary key auto_increment,
    Evento varchar(50), 
    DataEvento date
);

DROP trigger LogArtisti;
DELIMITER $$
CREATE TRIGGER LogArtisti
AFTER INSERT -- , UPDATE, DELETE
ON artist FOR EACH ROW
BEGIN
    INSERT INTO artist_log (Evento, DataEvento)
    VALUES ('Modifica agli ordini', curdate());
END $$

DELIMITER ;

