/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     7/01/2024 2:34:29 p. m.                      */
/*==============================================================*/


/*==============================================================*/
/* Table: EVENTOS                                               */
/*==============================================================*/
create table EVENTOS
(
   ID                   bigint not null auto_increment,
   NAME                 varchar(200) not null,
   POINTS               numeric(12,2) not null default 0,
   DESCRIPTION          varchar(1000) not null,
   primary key (ID)
);

/*==============================================================*/
/* Table: INTEGRANTES                                           */
/*==============================================================*/
create table INTEGRANTES
(
   ID                   bigint not null auto_increment,
   NAME                 varchar(200) not null,
   RANGO_ID             bigint not null,
   DATECREATE           date not null,
   DATEUPDATE           date default NULL,
   primary key (ID)
);

/*==============================================================*/
/* Table: PARTICIPACION                                         */
/*==============================================================*/
create table PARTICIPACION
(
   ID                   bigint not null auto_increment,
   INTEGRANTE_ID        bigint not null,
   EVENTO_ID            bigint not null,
   DATE                 date not null,
   primary key (ID)
);

/*==============================================================*/
/* Table: RANGOS                                                */
/*==============================================================*/
create table RANGOS
(
   ID                   bigint not null auto_increment,
   NAME                 varchar(200) not null,
   DESCRIPTION          varchar(1000) not null,
   primary key (ID)
);

alter table INTEGRANTES add constraint FK_INTEGRAN_REFERENCE_RANGOS foreign key (RANGO_ID)
      references RANGOS (ID) on delete restrict on update cascade;

alter table PARTICIPACION add constraint FK_PARTICIP_REFERENCE_INTEGRAN foreign key (INTEGRANTE_ID)
      references INTEGRANTES (ID) on delete restrict on update cascade;

alter table PARTICIPACION add constraint FK_PARTICIP_REFERENCE_EVENTOS foreign key (EVENTO_ID)
      references EVENTOS (ID) on delete restrict on update cascade;

