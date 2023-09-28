CREATE TABLE disciplinasprof(
	id int primary key not null auto_increment,
    coddisciplina int not null,
    codprofessor int not null,
    curso int,
    cargahoraria int,
    anoletivo int,
	foreign key (coddisciplina) references disciplinas(codigodisc),
	foreign key (codprofessor) references professores(registro)
);