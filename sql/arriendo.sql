/*==============================================================*/
/* Table: ARRIENDO                                              */
/*==============================================================*/
create table ARRIENDO (
   ID_ARRIENDO          serial               not null,
   ID_INQUILINO         INT4                 not null,
   ID_DEPARTAMENTO      INT4                 not null,
   FECHA_INICIO         DATE                 null,
   DIA_CORTE            INT4                 null,
   constraint PK_ARRIENDO primary key (ID_ARRIENDO)
);

/*==============================================================*/
/* Table: DEPARTAMENTO                                          */
/*==============================================================*/
create table DEPARTAMENTO (
   ID_DEPARTAMENTO      SERIAL               not null,
   PISO                 VARCHAR(25)          null,
   PRECIO               DECIMAL(5,2)         null,
   GARANTIA             DECIMAL(5,2)         null,
   constraint PK_DEPARTAMENTO primary key (ID_DEPARTAMENTO)
);

/*==============================================================*/
/* Table: INQUILINO                                             */
/*==============================================================*/
create table INQUILINO (
   ID_INQUILINO         SERIAL               not null,
   NOMBRE               VARCHAR(50)          null,
   APELLIDO             VARCHAR(50)          null,
   CEDULA               VARCHAR(10)          null,
   constraint PK_INQUILINO primary key (ID_INQUILINO)
);

alter table ARRIENDO
   add constraint FK_ARRIENDO_REFERENCE_INQUILIN foreign key (ID_INQUILINO)
      references INQUILINO (ID_INQUILINO)
      on delete restrict on update restrict;

alter table ARRIENDO
   add constraint FK_ARRIENDO_REFERENCE_DEPARTAM foreign key (ID_DEPARTAMENTO)
      references DEPARTAMENTO (ID_DEPARTAMENTO)
      on delete restrict on update restrict;

