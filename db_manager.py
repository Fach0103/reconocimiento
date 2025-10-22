import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), 'registro.db')

def conectar():
    return sqlite3.connect(DB_PATH)

def inicializar_db():
    with conectar() as conn:
        with open(os.path.join(os.path.dirname(__file__), 'db_schema.sql'), 'r') as f:
            conn.executescript(f.read())

def insertar_persona(nombre, apellido, email):
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO personas (nombre, apellido, email) VALUES (?, ?, ?)", (nombre, apellido, email))
        conn.commit()
        return cursor.lastrowid

def insertar_embedding(persona_id, vector_str):
    with conectar() as conn:
        conn.execute("INSERT INTO embeddings (persona_id, vector) VALUES (?, ?)", (persona_id, vector_str))
        conn.commit()

def obtener_todos_los_embeddings():
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT personas.id, personas.nombre, personas.apellido, personas.email, embeddings.vector
            FROM personas
            JOIN embeddings ON personas.id = embeddings.persona_id
        """)
        return cursor.fetchall()
