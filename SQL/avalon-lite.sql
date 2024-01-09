--==============================================================
-- DBMS name:      ANSI Level 2
-- Created on:     7/01/2024 5:10:18 p.�m.
--==============================================================


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
-- Table: integrantes
--==============================================================
create table integrantes (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name                 varchar(200)         not null,
rango_id             integer              not null,
datecreate           date                 not null,
dateupdate           date                  default null,
foreign key (rango_id)
      references rangos (id)
);

--==============================================================
-- Table: participaciones
--==============================================================
create table participaciones (
id INTEGER PRIMARY KEY AUTOINCREMENT,
integrante_id        integer              not null,
evento_id            integer              not null,
"date"               date                 not null,
foreign key (integrante_id)
      references integrantes (id),
foreign key (evento_id)
      references eventos (id)
);

