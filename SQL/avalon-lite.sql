--==============================================================
-- DBMS name:      ANSI Level 2
-- Created on:     7/01/2024 2:56:14 p. m.
--==============================================================


--==============================================================
-- Table: EVENTOS
--==============================================================
create table EVENTOS (
ID                   NUMERIC(6)           not null,
NAME                 VARCHAR(200)         not null,
POINTS               NUMERIC(12,2)        not null default 0,
DESCRIPTION          VARCHAR(1000)        not null,
primary key (ID)
);

--==============================================================
-- Table: RANGOS
--==============================================================
create table RANGOS (
ID                   NUMERIC(6)           not null,
NAME                 VARCHAR(200)         not null,
DESCRIPTION          VARCHAR(1000)        not null,
primary key (ID)
);

--==============================================================
-- Table: INTEGRANTES
--==============================================================
create table INTEGRANTES (
ID                   NUMERIC(6)           not null,
NAME                 VARCHAR(200)         not null,
RANGO_ID             INTEGER              not null,
DATECREATE           DATE                 not null,
DATEUPDATE           DATE                  default NULL,
primary key (ID),
foreign key (RANGO_ID)
      references RANGOS (ID)
);

--==============================================================
-- Table: PARTICIPACION
--==============================================================
create table PARTICIPACION (
ID                   NUMERIC(6)           not null,
INTEGRANTE_ID        INTEGER              not null,
EVENTO_ID            INTEGER              not null,
"DATE"               DATE                 not null,
primary key (ID),
foreign key (INTEGRANTE_ID)
      references INTEGRANTES (ID),
foreign key (EVENTO_ID)
      references EVENTOS (ID)
);

