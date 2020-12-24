Determine si un tablero de sudoku 9x9 es válido. Sólo hay que validar las celdas que vienen completadas.
Se deben validar las siguientes reglas:
- El caracter '.' significa que esa celda está vacía y debe ser ignorado.
- Cada fila sólo puede contener los dígitos 1-9 sin repeticiones.
- Cada columna sólo puede contener los dígitos 1-9 sin repeticiones.
- Cada uno de los nueve sub-grillas 3x3 del tablero sólo puede contener los dígitos 1-9 sin repeticiones.
Notas:
- El tablero puede ser válido pero no necesariamente completable, esto no importa y debe devolver true.
- Solo las celdas completadas deben ser validadas de acuerdo a las reglas mencionadas (un tablero vacío sería válido, por ejemplo).