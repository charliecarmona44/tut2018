#drop database kuorra_login;
#CREATE DATABASE kuorra_login;
#USE kuorra_login;

create database utec_tutoria;

use utec_tutoria;

CREATE TABLE users(
    user varchar(64) NOT NULL PRIMARY KEY,
    privilege integer NOT NULL DEFAULT -1,
    status integer NOT NULL DEFAULT 1,
    name varchar(150) NOT NULL,
    email varchar(100) NOT NULL,
    other_data varchar(50) NOT NULL,
    user_hash varchar(32) NOT NULL,
    change_pwd integer NOT NULL DEFAULT 1,
    created timestamp NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE sessions(
    session_id char(128) UNIQUE NOT NULL,
    atime timestamp NOT NULL default current_timestamp,
    data text
)ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE logs(
    id_log integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    user varchar(64) NOT NULL,
    ip varchar(16) NOT NULL,
    access timestamp NOT NULL,
    FOREIGN KEY (user) REFERENCES users(user)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE programas_educativos(
    id_programa_educativo integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    programa varchar(100) NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE periodos(
    id_periodo integer NOT NUll PRIMARY KEY AUTO_INCREMENT,
    periodo varchar(60) NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE grupos(
    id_grupo integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    id_programa_educativo integer NOT NULL,
    id_periodo integer NOT NULL,
    grupo varchar(32) NOT NULL,
    clave_grupo varchar(10) NOT NULL,
    status integer NOT NULL DEFAULT 1,
    FOREIGN KEY (id_programa_educativo) REFERENCES programas_educativos(id_programa_educativo)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE tutores_grupos(
    id_tutor_grupo integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    user varchar(64) NOT NULL,
    id_grupo integer NOT NULL,
    FOREIGN KEY (user) REFERENCES users(user),
    FOREIGN KEY (id_grupo) REFERENCES grupos(id_grupo)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;



CREATE TABLE alumnos(
    email varchar(50) NOT NULL PRIMARY KEY,
    id_grupo integer NOT NULL,
    matricula varchar(15) NOT NULL,
    fecha_alta timestamp NOT NULL,
    nombre varchar(100) NOT NULL,
    ap_paterno varchar(100) NOT NULL,
    ap_materno varchar(100) NOT NULL,
    fecha_nacimiento date NOT NULL,
    curp varchar(20) NOT NULL,
    cuatrimestre integer NOT NULL,
    telefono_celular varchar(10) NOT NULL,
    telefono_casa varchar(10) NOT NULL,
    email_institucional varchar(50) NOT NULL,
    email_personal varchar(50) NOT NULL,
    calle varchar(50) NOT NULL,
    colonia varchar(50) NOT NULL,
    cp varchar(6) NOT NULL,
    no_exterior varchar(10) NOT NULL,
    no_interior varchar(10) NOT NULL,
    municipio varchar(50) NOT NULL,
    referencias varchar(300) NOT NULL,
    idioma_principal varchar(20) NOT NULL,
    segundo_idioma varchar(20) NOT NULL,
    FOREIGN KEY (id_grupo) REFERENCES grupos(id_grupo)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE padres_tutores(
    id_padre_tutor integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    email varchar(50) NOT NULL UNIQUE,
    nombre varchar(50) NOT NULL,
    ap_paterno varchar(50) NOT NULL,
    ap_materno varchar(50) NOT NULL,
    parentesco varchar(50) NOT NULL,
    telefono_celular varchar(10) NOT NULL,
    telefono_casa varchar(10) NOT NULL,
    telefono_trabajo varchar(10) NOT NULL,
    email_tutor varchar(51) NOT NULL,
    calle varchar(50) NOT NULL,
    colonia varchar(50) NOT NULL,
    cp varchar(6) NOT NULL,
    no_exterior varchar(10) NOT NULL,
    no_interior varchar(10) NOT NULL,
    municipio varchar(50) NOT NULL,
    referencias varchar(300) NOT NULL,
    FOREIGN KEY (email) REFERENCES alumnos(email)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE historiales_medicos(
    id_historial_medico integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    email varchar(50) NOT NULL UNIQUE,
    imss varchar(2) NOT NULL,
    no_imss varchar(50) NOT NULL,
    institucion_salud varchar(2) NOT NULL,
    nombre_institucion_salud varchar(30) NOT NULL,
    no_afiliacion_otra varchar(50) NOT NULL,
    tipo_sangre varchar(4) NOT NULL,
    alergias varchar(20) NOT NULL,
    descripcion_alergias varchar(300) NOT NULL,
    enfermedades varchar(50) NOT NULL,
    descripcion_enfermedad varchar(300) NOT NULL,
    medicamentos varchar(200) NOT NULL,
    descripcion_medicamentos varchar(200) NOT NULL,
    FOREIGN KEY (email) REFERENCES alumnos(email)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE aspectos_economicos(
    id_aspecto_economico integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    email varchar(50) NOT NULL UNIQUE,
    beca varchar(10) NOT NULL,
    nombre_beca varchar(50) NOT NULL,
    depende_economicamente varchar(50) NOT NULL,
    tiene_computadora varchar(2) NOT NULL,
    tiene_telefono varchar(2) NOT NULL,
    trabaja varchar(2) NOT NULL,
    empresa varchar(100) NOT NULL,
    jefe_inmediato varchar(100) NOT NULL,
    telefono_trabajo varchar(10) NOT NULL,
    email_trabajo varchar(50) NOT NULL,
    actividad varchar(200) NOT NULL,
    jornada_laboral varchar(200) NOT NULL,
    calle varchar(50) NOT NULL,
    colonia varchar(50) NOT NULL,
    cp varchar(6) NOT NULL,
    no_exterior varchar(10) NOT NULL,
    no_interior varchar(10) NOT NULL,
    municipio varchar(50) NOT NULL,
    referencias varchar(300) NOT NULL,
    FOREIGN KEY (email) REFERENCES alumnos(email)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE aspectos_personales(
    id_aspecto_personal integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    email varchar(50) NOT NULL UNIQUE,
    estado_civil varchar(50) NOT NULL,
    numero_hijos integer NOT NULL,
    quien_los_cuida varchar(50) NOT NULL,
    no_integrantes_familia varchar(50) NOT NULL,
    comunicacion_familiar varchar(2) NOT NULL,
    responsable varchar(2) NOT NULL,
    respetuosa varchar(2) NOT NULL,
    trabajo_equipo varchar(2) NOT NULL,
    FOREIGN KEY (email) REFERENCES alumnos(email)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE trayectorias_academicas(
    id_trayectoria_academica integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    email varchar(50) NOT NULL UNIQUE,
    primaria_institucion varchar(50) NOT NULL,
    primaria_promedio varchar(4) NOT NULL,
    secundaria_institucion varchar(50) NOT NULL,
    secundadria_promedio varchar(50) NOT NULL,
    bachillerato_institucion varchar(50) NOT NULL,
    bachillerato_promedio varchar(50) NOT NULL,
    tsu_institucion varchar(50) NOT NULL,
    tsu_promedio float NOT NULL default 0.0,
    cuatrimestre_promedio01 float NOT NULL default 0.0,
    cuatrimestre_promedio02 float NOT NULL default 0.0,
    cuatrimestre_promedio03 float NOT NULL default 0.0,
    cuatrimestre_promedio04 float NOT NULL default 0.0,
    cuatrimestre_promedio05 float NOT NULL default 0.0,
    cuatrimestre_promedio06 float NOT NULL default 0.0,
    cuatrimestre_promedio07 float NOT NULL default 0.0,
    cuatrimestre_promedio08 float NOT NULL default 0.0,
    cuatrimestre_promedio09 float NOT NULL default 0.0,
    cuatrimestre_promedio10 float NOT NULL default 0.0,
    FOREIGN KEY (email) REFERENCES alumnos(email)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE grupos_alumnos(
    id_grupos_alumnos integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    id_grupo integer NOT NULL,
    email varchar(64) NOT NULL UNIQUE,
    FOREIGN KEY (id_grupo) REFERENCES grupos(id_grupo),
    FOREIGN KEY (email) REFERENCES alumnos(email)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE observaciones_grupales(
    id_observacion_grupal integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    id_grupo integer NOT NULL,
    user varchar(64) NOT NULL,
    fecha_observaciones timestamp NOT NULL,
    observaciones varchar(1000) NOT NULL,
    acciones varchar(1000) NOT NULL,
    resultados varchar(1000) NOT NULL,
    fecha_atencion datetime NOT NULL,
    estado varchar(10) NOT NULL, #en tramite, atendido
    FOREIGN KEY (id_grupo) REFERENCES grupos(id_grupo)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE observaciones_individuales(
    id_observacion_individual integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    email varchar(50) NOT NULL,
    user varchar(64) NOT NULL,
    fecha_observaciones timestamp NOT NULL,
    observaciones varchar(1000) NOT NULL,
    fecha_atencion datetime NOT NULL,
    acciones varchar(1000) NOT NULL,
    resultados varchar(1000) NOT NULL,
    semaforo varchar(10) NOT NULL,
    FOREIGN KEY (email) REFERENCES alumnos(email)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE area_atencion(
    id_area_atencion integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    area varchar(123) NOT NULL,
    descripcion varchar(121) NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE tutoria_especial(
    id_tutoria_especial integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    id_area_atencion integer NOT NULL,
    email varchar(50) NOT NULL UNIQUE,
    user varchar(64) NOT NULL,
    id_grupo integer NOT NULL,
    id_programa_educativo integer NOT NULL,
    fecha date NOT NULL,
    motivo_tutoria varchar(129) NOT NULL,
    acciones varchar(150) NOT NULL,
    resolucion_tutoria varchar(138) NOT NULL,
    nota varchar(100) NOT NULL,
    FOREIGN KEY (id_area_atencion) REFERENCES area_atencion(id_area_atencion),
    FOREIGN KEY (email) REFERENCES alumnos(email),
    FOREIGN KEY (user) REFERENCES users(user),
    FOREIGN KEY (id_grupo) REFERENCES grupos(id_grupo),
    FOREIGN KEY (id_programa_educativo) REFERENCES programas_educativos(id_programa_educativo)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;


INSERT INTO users (user, privilege, status, name, email, other_data, user_hash, change_pwd)
VALUES ('admin', 0, 1, 'Admin', 'admin@gmail.com','TIC:SI', MD5(concat('admin', 'kuorra_key', '2016/06/04')), 0),
('guess',MD5(concat('guess', 'kuorra_key')), 1, 1, 'Guess', 'guess@gmail.com','TIC:SI', MD5(concat('guess', 'kuorra_key','2016/06/04')), 0);

INSERT INTO users (user, privilege, status, name, email, other_data, user_hash, change_pwd)
VALUES ('admingeneral', 0, 1, 'admingeneral', 'admin@gmail.com','TIC:SI', MD5(concat('admingeneral', 'kuorra_key', '2016/06/04')), 0);

INSERT INTO users (user, privilege, status, name, email, other_data, user_hash, change_pwd)
VALUES ('1715110737@utectulancingo.edu.mx', 0, 1, 'admingeneral', '1715110737@utectulancingo.edu.mx','TIC:SI', MD5(concat('admingeneral', 'kuorra_key', '2016/06/04')), 0);

INSERT INTO users (user, privilege, status, name, email, other_data, user_hash, change_pwd)
VALUES ('carloscarmonaperez44@gmail.com', 0, 1, 'carlos carmona', 'carloscarmonaperez44@gmail.com','TIC:SI', MD5(concat('admingeneral', 'kuorra_key', '2016/06/04')), 0);

INSERT INTO programas_educativos VALUES (1, 'Tecnologías de la Información y Comunicación');
INSERT INTO programas_educativos VALUES (2, 'Desarollo y inovación´empresarial');
INSERT INTO programas_educativos VALUES (4, 'Contaduria');
INSERT INTO programas_educativos vALUES (5, 'Energias Renovables');
INSERT INTO programas_educativos VALUES (6, 'Terapia fisica');
INSERT INTO programas_educativos VALUES (7, 'enfermeria');
INSERT INTO programas_educativos VALUES (8, 'criminalistia');
INSERT INTO programas_educativos VALUES (9, 'Nanotecnologia');

INSERT INTO grupos VALUES (1, 1, 'TIC11', 'Sep-Dic 2017');
INSERT INTO grupos VALUES (2, 1, 'TIC12', 'Sep-Dic 2017');
INSERT INTO grupos VALUES (3, 1, 'TIC31', 'Sep-Dic 2018');
INSERT INTO grupos VALUES (4, 1, 'TIC32', 'sep-Dic 2018');
INSERT INTO grupos VALUES (5, 1, 'TIC61', 'Sep-Dic 2019');
INSERT INTO grupos VALUES (6, 1, 'TIC62', 'Sep-Dic 2019');




INSERT INTO tutores_grupos VALUES (1, 'tutor', 1);
INSERT INTO tutores_grupos VALUES (2, 'tutor', 2);


create view grupos_tutores_users as (
select u.user, u.name, t.id_tutor_grupo, p.periodo, concat(g.grupo,' ', p.periodo) as grupo
from users u, tutores_grupos t, grupos g, periodos p
where u.user = t.user and g.id_grupo = t.id_grupo and g.id_grupo = p.id_periodo);


create view alumnos_observaciones as (
select
    a.email,
    a.id_grupo,
    concat(a.nombre, ' ', a.ap_paterno, ' ', a.ap_materno) as nombre,
    concat(g.grupo,' ', p.periodo) as grupo,
    o.id_observacion_individual,
    o.semaforo,
    o.fecha_observaciones
from grupos g, alumnos a, observaciones_individuales o, periodos p
where o.email = a.email and g.id_grupo = a.id_grupo and g.id_grupo = p.id_periodo);

create view alumnos_grupos as (
    select
        a.email,
        a.id_grupo,
        p.periodo,
        concat(a.nombre, ' ', a.ap_paterno, ' ', a.ap_materno) as nombre,
        concat(g.grupo,' ', p.periodo) as grupo
    from grupos g, alumnos a, periodos p
    where a.id_grupo = g.id_grupo and g.id_grupo = p.id_periodo)
    ;

SELECT * FROM users;
SELECT * FROM sessions;
SELECT * FROM tutoria;
SELECT * FROM logs;


CREATE USER 'kuorra'@'localhost' IDENTIFIED BY 'kuorra.2018';
GRANT ALL PRIVILEGES ON kuorra_login.* TO 'kuorra'@'localhost';
FLUSH PRIVILEGES;





