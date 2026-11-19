
--NIVEL 1 — SELECT básico (Ej 1-8)
-- Ejercicio 1: Mostrar todos los equipos con todas sus columnas.
SELECT * FROM equipos;

SELECT * FROM goles;

SELECT * FROM partidos;

-- Ejercicio 2: Mostrar solo el nombre y el ranking FIFA de cada equipo.
SELECT nombre, ranking_fifa FROM equipos;

--Ejercicio 3: Mostrar el nombre como "pais" y el ranking FIFA como "fifa_rank". Usar alias con AS.
SELECT nombre AS pais, ranking_fifa AS fifa_rank FROM equipos;

-- Ejercicio 4: Mostrar todos los jugadores con todas sus columnas.
SELECT * FROM jugadores;

-- Ejercicio 5: Mostrar las distintas posiciones de jugadores que existen (sin repetir).
SELECT DISTINCT posicion, COUNT(*) FROM jugadores
GROUP BY posicion;

--Ejercicio 6: Mostrar el nombre y dorsal de todos los jugadores.
SELECT nombre, dorsal FROM jugadores;

-- Ejercicio 7: Mostrar todas las filas de la tabla posiciones_por_grupo.
SELECT * FROM posiciones_por_grupo;

--Ejercicio 8: Mostrar el nombre y grupo de cada equipo, ordenado por grupo alfabéticamente.
SELECT
e.nombre,
pg.grupo
FROM equipos e
INNER JOIN  posiciones_por_grupo pg ON e.id = pg.equipo_id
ORDER BY pg.grupo ASC;

SELECT nombre, grupo FROM equipos ORDER BY grupo;

-- NIVEL 2 — WHERE (Ej 9-16)
-- Ejercicio 9: Mostrar los equipos que pertenecen al grupo A.
SELECT * FROM equipos
WHERE grupo = 'A';

-- Ejercicio 10: Mostrar los equipos de la CONMEBOL.
SELECT * FROM equipos
WHERE confederacion = 'CONMEBOL';

--Ejercicio 11: Mostrar todos los jugadores que son arqueros.
SELECT nombre, posicion, dorsal, equipo_id FROM jugadores
WHERE posicion = 'Arquero';

-- Ejercicio 12: Mostrar todos los jugadores que son delanteros.
SELECT nombre, posicion, dorsal, equipo_id FROM jugadores
WHERE posicion = 'Delantero';

--Ejercicio 13: Mostrar los equipos con ranking FIFA menor a 10 (mejor ranking).
SELECT nombre, ranking_fifa FROM equipos
WHERE ranking_fifa <= 10
ORDER BY ranking_fifa ASC;

-- Mostrar los equipos que NO son de la UEFA.
SELECT nombre, confederacion FROM equipos
WHERE confederacion <> 'UEFA';

--Ejercicio 15: Mostrar los jugadores que usan el dorsal 10 (el clásico número de estrella).
SELECT nombre, dorsal, equipo_id FROM jugadores
WHERE dorsal = 10;

--Ejercicio 16: Mostrar los equipos cuyo ranking FIFA está entre 10 y 20 (inclusive).
SELECT nombre, ranking_fifa FROM equipos
WHERE ranking_fifa > 10 AND ranking_fifa < 20
ORDER BY ranking_fifa;

-- NIVEL 3 — ORDER BY + LIMIT (Ej 17-24)
-- Ejercicio 17: Mostrar todos los equipos ordenados por ranking FIFA de mejor a peor.
SELECT nombre, ranking_fifa FROM equipos
ORDER BY ranking_fifa;

-- Ejercicio 18: Mostrar todos los equipos ordenados por ranking FIFA de peor a mejor.
SELECT nombre, ranking_fifa FROM equipos
ORDER BY ranking_fifa DESC;

-- Ejercicio 19: Mostrar los 3 equipos con mejor ranking FIFA (top 3).
SELECT nombre, ranking_fifa FROM equipos
ORDER BY ranking_fifa
LIMIT(3);

-- Ejercicio 20: Mostrar todos los equipos ordenados alfabéticamente por nombre.
SELECT nombre FROM equipos
ORDER BY nombre;

-- Ejercicio 21: Mostrar los 5 equipos con mejor ranking FIFA.
SELECT nombre, ranking_fifa FROM equipos
ORDER BY ranking_fifa
LIMIT(5);

-- Ejercicio 22: Mostrar las posiciones por grupo ordenadas por puntos de mayor a menor.
SELECT equipo_id, grupo, puntos FROM posiciones_por_grupo
ORDER BY puntos DESC;

-- Ejercicio 23: Mostrar los equipos ordenados por ranking FIFA,
-- pero saltando los 3 primeros (paginación, página 2).

SELECT nombre, ranking_fifa
FROM equipos
ORDER BY ranking_fifa ASC
LIMIT 3 OFFSET 3;

-- Ejercicio 24: Mostrar las posiciones por grupo ordenadas por goles a favor (gf) de mayor a menor.
SELECT equipo_id, grupo, gf FROM posiciones_por_grupo
ORDER BY gf DESC;

-- NIVEL 4 — GROUP BY + Agregadas (Ej 25-32)
-- Ejercicio 25: Contar cuántos equipos hay por cada confederación.
SELECT confederacion, COUNT(*) cantidad FROM equipos
GROUP BY confederacion
ORDER BY cantidad DESC;

--Ejercicio 26: Contar cuántos equipos hay por cada grupo.
SELECT grupo, COUNT(*) cantidad from equipos
GROUP BY grupo
ORDER BY grupo;

-- Ejercicio 27: Calcular el promedio del ranking FIFA por confederación.
SELECT confederacion, ROUND(AVG(ranking_fifa),1) AS ranking_promedio FROM equipos
GROUP BY confederacion
ORDER BY ranking_promedio;

-- Ejercicio 28: Calcular el total de goles a favor (gf) por grupo desde la tabla posiciones_por_grupo.
SELECT grupo, SUM(gf) AS total_gf from posiciones_por_grupo
GROUP BY grupo
ORDER BY total_gf DESC;

-- Ejercicio 29: Mostrar el minuto más tardío en el que se anotó un gol en cada partido.
SELECT   MAX(minuto) AS Max_Minuto FROM goles --81

SELECT partido_id, MAX(minuto) AS minuto_maximo
FROM goles
GROUP BY partido_id
ORDER BY partido_id;

-- Ejercicio 30: Mostrar cuántos goles anotó cada jugador, ordenado de mayor a menor

SELECT jugador_id, COUNT(*) AS goles
FROM goles
GROUP BY jugador_id
ORDER BY goles DESC;

-- Ejercicio 31: Mostrar los grupos que tienen más de 5 goles a favor en total. Usar HAVING.
SELECT grupo, SUM(gf) AS goles_favor FROM posiciones_por_grupo
GROUP BY grupo
HAVING SUM(gf) > 5
ORDER BY goles_favor;

-- Ejercicio 32: Contar cuántas posiciones de jugador distintas existen.
SELECT COUNT(DISTINCT(posicion)) AS posiciones_distintas FROM jugadores;

-- NIVEL 5 — JOINs (Ej 33-40)
-- Ejercicio 33: Mostrar todos los jugadores con el nombre de su equipo. INNER JOIN equipos y jugadores.
-- jugador, posicion, equipo
SELECT * FROM jugadores;
SELECT * FROM equipos;

SELECT
j.nombre AS jugador,
j.posicion,
e.nombre AS equipo
FROM equipos e 
INNER JOIN jugadores j ON e.id = j.equipo_id
ORDER BY e.nombre, j.nombre;

-- Ejercicio 34: Mostrar todos los partidos con el nombre del equipo local.
-- id, equipo_local, goles_local, goles_visitante, fase

SELECT
p.id,
e.nombre AS equipo_local,
p.goles_local,
p.goles_visitante,
p.fase
FROM equipos e
INNER JOIN partidos p ON e.id = p.local_id;

-- Ejercicio 35: Mostrar todos los partidos con el nombre del equipo local 
-- Y del equipo visitante. Self-JOIN con alias.
SELECT
p.id,
el.nombre AS equipo_local,
p.goles_local,
ev.nombre AS equipo_visitante,
p.goles_visitante,
p.fase
FROM partidos AS p
INNER JOIN equipos AS el ON el.id = p.local_id
INNER JOIN equipos AS ev ON ev.id = p.visitante_id;

-- Ejercicio 36: Mostrar todos los equipos, incluso aquellos que no hayan jugado 
-- como locales todavía. LEFT JOIN.
-- equipo, partido_id, goles_local

SELECT
e.nombre AS equipo,
p.id AS partido_id,
p.goles_local
FROM equipos AS e
LEFT JOIN partidos AS p ON e.id = p.local_id
ORDER BY e.nombre ASC;


-- Ejercicio 37: Mostrar todos los goles con el nombre del jugador y el ID del partido. 
-- JOIN entre goles y jugadores.
-- gol_id, jugador, minuto, es_penal, partido_id

SELECT
g.id AS gol_id,
j.nombre AS jugador,
g.minuto,
g.es_penal,
g.partido_id
FROM goles as g
INNER JOIN jugadores AS j ON j.id = g.jugador_id




