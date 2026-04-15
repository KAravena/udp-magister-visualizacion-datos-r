#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Crea SOLO la estructura /apuntes/anio-X/sem-YY/ (sin .qmd).
Agrega un .gitkeep vacío para que Git incluya las carpetas.
"""

from pathlib import Path

BASE = Path("./apuntes")

MALLA = {
    "anio-1": {
        "sem-01": [
            "Filosofía Social",
            "Historia de la Sociedad Moderna",
            "Introducción a la Sociología",
            "Antropología",
            "Psicología Social",
            "Inglés I",
            "Curso Transversal de Facultad"
        ],
        "sem-02": [
            "Teoría Sociológica Clásica",
            "Historia Social de América Latina",
            "Epistemología",
            "Diseño de Investigación",
            "Población y Sociedad",
            "Inglés II"
        ]
    },
    "anio-2": {
        "sem-03": [
            "Teorías Sociológicas de la Sociedad Moderna",
            "Historia Social de Chile",
            "Estrategias de Investigación Cualitativa",
            "Estadística Descriptiva",
            "Economía",
            "Inglés III"
        
        ],
        "sem-04": [
            "Teorías Sociológicas Contemporáneas",
            "Sociología Política",
            "Análisis de Información Cualitativa",
            "Estadística Correlacional",
            "Estrategias de Investigación Cuantitativa",
            "Inglés IV",
            "Curso Transversal de Facultad"
        ]
    },
    "anio-3": {
        "sem-05": [
            "Desigualdades y Estratificación Social",
            "Sociología de la Cultura",
            "Sociología del Género",
            "Estadística Multivariada",
            "Electivo",
        ],
        "sem-06": [
            "Teoría y Sociedad Latinoamericana",
            "Sociología Económica",
            "Sociología de las Políticas Públicas",
            "Electivo"
        ]
    },
    "anio-4": {
        "sem-07": [
            "Transformaciones Sociales del Chile Contemporáneo",
            "Investigación Evaluativa",
            "Electivo"
        ],
        "sem-08": [
            "Seminario de Grado",
            "Electivo"
        ]
    },
    "anio-5": {
        "sem-09": [
            "Seminario de Título I"
        ],
        "sem-10": [
            "Seminario de Título II",
            "Práctica Profesional"
        ]
    }
}

def main():
    creadas = 0
    for anio, semestres in MALLA.items():
        for sem, ramos in semestres.items():
            # crea carpeta del semestre
            sem_dir = BASE / anio / sem
            sem_dir.mkdir(parents=True, exist_ok=True)

            # .gitkeep para que Git suba la carpeta aunque esté vacía
            (sem_dir / ".gitkeep").write_text("", encoding="utf-8")

            # crea carpeta por ramo (sin archivos)
            for ramo in ramos:
                # nombre de carpeta “amable” (sin tildes/espacios no hace falta aún)
                ramo_dir = sem_dir / ramo
                ramo_dir.mkdir(parents=True, exist_ok=True)
                (ramo_dir / ".gitkeep").write_text("", encoding="utf-8")
                creadas += 1

    print(f"Listo ✅  Estructura creada. Carpetas de ramos: {creadas}")

if __name__ == "__main__":
    main()
