/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     14/01/2024 7:43:19 p. m.                     */
/*==============================================================*/


/*==============================================================*/
/* Table: asistencias                                           */
/*==============================================================*/
create table asistencias
(
   id                   bigint not null auto_increment,
   integrante_id        bigint not null,
   evento_id            bigint not null,
   date                 date not null,
   primary key (id)
);

/*==============================================================*/
/* Table: eventos                                               */
/*==============================================================*/
create table eventos
(
   id                   bigint not null auto_increment,
   name                 varchar(200) not null,
   points               numeric(12,2) not null default 0,
   description          varchar(1000) not null,
   primary key (id)
);

/*==============================================================*/
/* Table: integrantes                                           */
/*==============================================================*/
create table integrantes
(
   id                   bigint not null auto_increment,
   name                 varchar(200) not null,
   rango_id             bigint not null,
   datecreate           date not null,
   dateupdate           date default null,
   primary key (id)
);

/*==============================================================*/
/* Table: rangos                                                */
/*==============================================================*/
create table rangos
(
   id                   bigint not null auto_increment,
   name                 varchar(200) not null,
   description          varchar(1000) not null,
   primary key (id)
);

alter table asistencias add constraint fk_asistenc_reference_integran foreign key (integrante_id)
      references integrantes (id) on delete cascade on update cascade;

alter table asistencias add constraint fk_asistenc_reference_eventos foreign key (evento_id)
      references eventos (id) on delete restrict on update cascade;

alter table integrantes add constraint fk_integran_reference_rangos foreign key (rango_id)
      references rangos (id) on delete restrict on update cascade;

