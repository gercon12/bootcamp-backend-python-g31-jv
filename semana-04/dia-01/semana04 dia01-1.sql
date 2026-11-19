-- Construi una tabla usando DDL
CREATE TABLE equipos (
--     COL TIPO REGLAS
    id SERIAL PRIMARY KEY,    
    nombre VARCHAR(100) NOT NULL,
    confederacion VARCHAR(50) NOT NULL,
    grupo CHAR(1),
    ranking_fifa INTEGER NOT NULL,
    clasificado BOOLEAN DEFAULT TRUE,
-- NOW ( ) => La hora actual de la operacion
    fecha_creacion TIMESTAMP DEFAULT NOW()
);


CREATE TABLE jugadores (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    posicion VARCHAR(50) NOT NULL,
    dorsal INTEGER NOT NULL,
    activo BOOLEAN DEFAULT TRUE,
    fecha_nacimiento DATE,
    equipo_id INTEGER NOT NULL REFERENCES equipos(id)
);

-- RETO 02
-- Construir la tabla posiciones_por_grupo
-- Construir la tabla partidos
-- OPCIONAL : Construir la tabla goles

CREATE TABLE posiciones_por_grupo(
    id SERIAL PRIMARY KEY,
    grupo CHAR(1) NOT NULL,
    pj INTEGER NOT NULL,
    pg INTEGER NOT NULL,
    pe INTEGER NOT NULL,
    gf INTEGER NOT NULL,
    gc INTEGER NOT NULL,
    puntos INTEGER NOT NULL,
    equipo_id INTEGER NOT NULL REFERENCES equipos(id)
);

CREATE TABLE partidos(
    id SERIAL PRIMARY KEY,
    goles_local INTEGER DEFAULT 0,
    goles_visitante INTEGER DEFAULT 0,
    fase VARCHAR(50),
    fecha TIMESTAMP NOT NULL,
    local_id INTEGER NOT NULL REFERENCES equipos(id),
    visitante_id INTEGER NOT NULL REFERENCES equipos(id)
);

CREATE TABLE goles(
    id SERIAL PRIMARY KEY,
    minuto INTEGER NOT NULL,
    es_penal BOOLEAN DEFAULT TRUE,
    partido_id INTEGER NOT NULL REFERENCES partidos(id),
    jugador_id INTEGER NOT NULL REFERENCES jugadores(id)
);


-- GRUPO A
INSERT INTO equipos (nombre, confederacion, grupo, ranking_fifa) VALUES
    ('Argentina', 'CONMEBOL', 'A', 1),
    ('Perú', 'CONMEBOL', 'A', 31),
    ('Chile', 'CONMEBOL', 'A', 42),
    ('Canadá', 'CONCACAF', 'A', 48);


-- GRUPO B
INSERT INTO equipos (nombre, confederacion, grupo, ranking_fifa) VALUES
    ('España', 'UEFA', 'B', 8),
    ('Países Bajos', 'UEFA', 'B', 6),
    ('Japón', 'AFC', 'B', 17),
    ('Marruecos', 'CAF', 'B', 13);

-- GRUPO C
INSERT INTO equipos (nombre, confederacion, grupo, ranking_fifa) VALUES
    ('Brasil', 'CONMEBOL', 'C', 5),
    ('Uruguay', 'CONMEBOL', 'C', 14),
    ('Croacia', 'UEFA', 'C', 9),
    ('Camerún', 'CAF', 'C', 38);

-- GRUPO D
INSERT INTO equipos (nombre, confederacion, grupo, ranking_fifa) VALUES
    ('Francia', 'UEFA', 'D', 2),
    ('Inglaterra', 'UEFA', 'D', 4),
    ('EE.UU.', 'CONCACAF', 'D', 11),
    ('Australia', 'AFC', 'D', 39);

-- GRUPO E
INSERT INTO equipos (nombre, confederacion, grupo, rankig_figa) VALUES
	('Bolivia', 'CONMEBOL', 'E', 44);

--CONSULTAR LA INFORMACION (VER)
SELECT nombre, confederacion FROM equipos;


--Con filtros (WHER)