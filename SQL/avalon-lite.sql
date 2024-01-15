--==============================================================
-- DBMS name:      ANSI Level 2
-- Created on:     7/01/2024 5:10:18 p.�m.
--==============================================================
-- Activar el soporte para claves foráneas
PRAGMA foreign_keys = ON;
--==============================================================
-- Table: eventos
--==============================================================
create table eventos (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name                 varchar(200)         not null,
points               numeric(12,2)        not null default 0,
description          varchar(1000)        not null
);

--==============================================================
-- Table: rangos
--==============================================================
create table rangos (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name                 varchar(200)         not null,
description          varchar(1000)        not null
);

--==============================================================
-- Table: miembros
--==============================================================
create table miembros (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name                 varchar(200)         not null,
rango_id             integer              default null,
datecreate           date                 not null,
dateupdate           date                 default null,
foreign key (rango_id) references rangos (id) ON DELETE SET DEFAULT
);

--==============================================================
-- Table: asistencias
--==============================================================
create table asistencias (
id INTEGER PRIMARY KEY AUTOINCREMENT,
miembro_id           integer              not null,
evento_id            integer              default null,
"date"               date                 not null,
foreign key (miembro_id) references miembros (id) ON DELETE CASCADE,
foreign key (evento_id) references eventos (id) ON DELETE SET DEFAULT
);

