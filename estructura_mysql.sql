create database garras;
use garras;

create table tipo (
    id_tipo int(11) not null,
    cargo varchar(45) not null,
    primary key (id_tipo)
);

create table persona (
    id_persona int(11) not null,
    nombre varchar(45) not null,
    apellido varchar(45) not null,
    primary key (id_persona)
);

create table usuario (
    id_persona int(11) not null,
    id_tipo int(11) not null,
    usuario varchar(45) not null,
    pass varchar(45) not null,
    primary key (id_persona, id_tipo),
    foreign key (id_persona) references persona (id_persona),
    foreign key (id_tipo) references tipo (id_tipo)
);

insert into tipo (id_tipo, cargo) values
(1, 'veterinario'),
(2, 'auxiliar veterinario'),
(3, 'recepcionista'),
(4, 'administrador'),
(5, 'cirujano veterinario'),
(6, 'especialista en fauna silvestre'),
(7, 'zootecnista');

insert into persona (id_persona, nombre, apellido) values
(1, 'sofia', 'valencia'),
(2, 'marco', 'ospina'),
(3, 'lucia', 'gonzalez'),
(4, 'esteban', 'ramirez'),
(5, 'natalia', 'quintero'),
(6, 'julian', 'restrepo'),
(7, 'carolina', 'zapata');


insert into usuario (id_persona, id_tipo, usuario, pass) values
(1, 1, 'sofia_vet', 'vet123'),
(2, 2, 'marco_aux', 'aux234'),
(3, 3, 'lucia_recep', 'recep345'),
(4, 4, 'esteban_admin', 'admin456'),
(5, 5, 'natalia_ciru', 'ciru567'),
(6, 6, 'julian_fauna', 'fauna678'),
(7, 7, 'caro_zoo', 'zoo789');