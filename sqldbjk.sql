CREATE DATABASE IF NOT EXISTS album;
CREATE TABLE registro (
   id_registro int(11) NOT NULL AUTO_INCREMENT,
   nombre_musica varchar(50) NOT NULL,
   autor varchar(60) DEFAULT NULL,
   genero varchar(30) DEFAULT NULL,
   año varchar(10) DEFAULT NULL,
   duracion varchar(10) DEFAULT NULL,
  PRIMARY KEY (id_registro)
);
SELECT * FROM album.registro;