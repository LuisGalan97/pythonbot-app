/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     14/01/2024 6:47:56 p. m.                     */
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
/* Table: miembros                                              */
/*==============================================================*/
create table miembros
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

alter table asistencias add constraint fk_asistenc_reference_miembros foreign key (integrante_id)
      references miembros (id) on delete cascade on update cascade;

alter table asistencias add constraint fk_asistenc_reference_eventos foreign key (evento_id)
      references eventos (id) on delete restrict on update cascade;

alter table miembros add constraint fk_miembros_reference_rangos foreign key (rango_id)
      references rangos (id) on delete restrict on update cascade;

