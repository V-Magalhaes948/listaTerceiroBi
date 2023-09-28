CREATE TABLE professores(
	registro int primary key not null auto_increment,
    nomeprof varchar(255) not null,
    telefone varchar(255) not null,
    idade varchar(255),
    salario float
);