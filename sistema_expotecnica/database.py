import sqlite3

DB_NAME = "expotecnica.db"


def get_db():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()
    cursor = conn.cursor()

    # 1. Configuración Institucional
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS configuracion (
        id INTEGER PRIMARY KEY CHECK (id = 1),
        nombre_institucion TEXT NOT NULL DEFAULT 'Colegio Técnico Profesional'
    )
    ''')
    cursor.execute('''
    INSERT OR IGNORE INTO configuracion (id, nombre_institucion) 
    VALUES (1, 'Colegio Técnico Profesional')
    ''')

    # 2. Proyectos
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS proyectos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        codigo TEXT UNIQUE NOT NULL,
        nombre TEXT NOT NULL,
        especialidad TEXT NOT NULL,
        seccion TEXT NOT NULL,
        estudiante_1 TEXT NOT NULL,
        estudiante_2 TEXT,
        estudiante_3 TEXT,
        descripcion TEXT
    )
    ''')

    # 3. Jueces
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS jueces (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cedula TEXT UNIQUE NOT NULL,
        nombre TEXT NOT NULL,
        email TEXT,
        especialidad TEXT NOT NULL,
        telefono TEXT
    )
    ''')

    # 4. Asignaciones
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS asignaciones (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        proyecto_id INTEGER NOT NULL,
        juez_id INTEGER NOT NULL,
        estado TEXT DEFAULT 'PENDIENTE',
        FOREIGN KEY (proyecto_id) REFERENCES proyectos(id) ON DELETE CASCADE,
        FOREIGN KEY (juez_id) REFERENCES jueces(id) ON DELETE CASCADE,
        UNIQUE(proyecto_id, juez_id)
    )
    ''')

    # 5. Evaluaciones Oficiales STEAM (37 indicadores = 111 pts)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS evaluaciones (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        asignacion_id INTEGER UNIQUE NOT NULL,
        i_a INTEGER NOT NULL, i_b INTEGER NOT NULL, i_c INTEGER NOT NULL, i_d INTEGER NOT NULL, i_e INTEGER NOT NULL,
        ii_a INTEGER NOT NULL, ii_b INTEGER NOT NULL, ii_c INTEGER NOT NULL, ii_d INTEGER NOT NULL, ii_e INTEGER NOT NULL, ii_f INTEGER NOT NULL,
        iii_a INTEGER NOT NULL, iii_b INTEGER NOT NULL, iii_c INTEGER NOT NULL, iii_d INTEGER NOT NULL, iii_e INTEGER NOT NULL, iii_f INTEGER NOT NULL, iii_g INTEGER NOT NULL, iii_h INTEGER NOT NULL,
        iv_a INTEGER NOT NULL, iv_b INTEGER NOT NULL, iv_c INTEGER NOT NULL, iv_d INTEGER NOT NULL, iv_e INTEGER NOT NULL, iv_f INTEGER NOT NULL, iv_g INTEGER NOT NULL, iv_h INTEGER NOT NULL, iv_i INTEGER NOT NULL, iv_j INTEGER NOT NULL,
        v_a_inf INTEGER NOT NULL, v_b_inf INTEGER NOT NULL, v_c_inf INTEGER NOT NULL,
        v_a_bit INTEGER NOT NULL, v_b_bit INTEGER NOT NULL, v_c_bit INTEGER NOT NULL,
        v_a_car INTEGER NOT NULL, v_b_car INTEGER NOT NULL,
        puntaje_total INTEGER NOT NULL,
        nota_final REAL NOT NULL,
        observaciones TEXT,
        recomendaciones TEXT,
        fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (asignacion_id) REFERENCES asignaciones(id) ON DELETE CASCADE
    )
    ''')

    conn.commit()
    conn.close()


if __name__ == "__main__":
    init_db()