/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     16/02/2024 8:51:06 p. m.                     */
/*==============================================================*/


/*==============================================================*/
/* Table: asistencias                                           */
/*==============================================================*/
create table asistencias
(
   id                   bigint not null auto_increment,
   integrante_id        bigint not null,
   evento_id            bigint not null,
   fecha                date not null,
   primary key (id)
);

/*==============================================================*/
/* Table: eventos                                               */
/*==============================================================*/
create table eventos
(
   id                   bigint not null auto_increment,
   nombre               varchar(200) not null,
   puntos               numeric(12,2) not null default 0,
   descripcion          varchar(1000) not null,
   primary key (id)
);

/*==============================================================*/
/* Table: integrantes                                           */
/*==============================================================*/
create table integrantes
(
   id                   bigint not null auto_increment,
   nombre               varchar(200) not null,
   rango_id             bigint not null,
   principal_id         bigint default null,
   fechacreacion        date not null,
   fechamodificacion    date default null,
   column_7             char(10),
   primary key (id)
);

/*==============================================================*/
/* Table: rangos                                                */
/*==============================================================*/
create table rangos
(
   id                   bigint not null auto_increment,
   nombre               varchar(200) not null,
   control              bigint not null,
   descripcion          varchar(1000) not null,
   primary key (id)
);

alter table asistencias add constraint fk_asistenc_reference_integran foreign key (integrante_id)
      references integrantes (id) on delete cascade on update cascade;

alter table asistencias add constraint fk_asistenc_reference_eventos foreign key (evento_id)
      references eventos (id) on delete restrict on update cascade;

alter table integrantes add constraint fk_integran_reference_rangos foreign key (rango_id)
      references rangos (id) on delete restrict on update cascade;

