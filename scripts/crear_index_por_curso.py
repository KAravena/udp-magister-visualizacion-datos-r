#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path
import re
import unicodedata
import argparse
import shutil

ROOT = Path(".")
BASE = ROOT / "apuntes"

def strip_accents(s: str) -> str:
    return "".join(
        c for c in unicodedata.normalize("NFD", s)
        if unicodedata.category(c) != "Mn"
    )

def slugify(texto: str) -> str:
    t = strip_accents(texto).lower()
    t = re.sub(r"[^a-z0-9]+", "-", t).strip("-")
    return t or "curso"

def course_title(course_dir: Path) -> str:
    tfile = course_dir / "title.txt"
    if tfile.exists():
        return tfile.read_text(encoding="utf-8").strip() or course_dir.name
    return course_dir.name

def detect_codes(course_dir: Path):
    """
    Devuelve (anio_code, sem_code) tomados del path: .../apuntes/anio-*/sem-*/<curso>
    """
    try:
        sem_code = course_dir.parent.name          # sem-XX
        anio_code = course_dir.parent.parent.name  # anio-X
        return anio_code, sem_code
    except Exception:
        return "anio-?", "sem-??"

TEMPLATE = r'''---
title: "{TITLE}"
description: "Síntesis, resúmenes y apuntes del ramo."
categories: ["{ANIO}", "{SEM}"]
image: /resources/imagenes/cursos/{BANNER}
title-block-banner: true
page-layout: full

listing:
  - id: apuntes-curso
    contents:
      - "*.qmd"
      - "!index.qmd"
    type: table
    sort: "date desc"
    fields: [title, author, date, description]
    filter-ui: true
    sort-ui: true
---

### Apuntes del curso
::: {{#apuntes-curso}}
:::
'''

def backup_file(path: Path) -> Path:
    """
    Crea un respaldo .bak (o .bak.N si ya existe). Devuelve la ruta de backup.
    """
    base_bak = path.with_suffix(path.suffix + ".bak")
    if not base_bak.exists():
        shutil.copy2(path, base_bak)
        return base_bak
    # Encuentra el siguiente índice libre
    i = 1
    while True:
        candidate = path.with_suffix(path.suffix + f".bak.{i}")
        if not candidate.exists():
            shutil.copy2(path, candidate)
            return candidate
        i += 1

def should_process(course_dir: Path, only: str | None) -> bool:
    if not only:
        return True
    # match por nombre de carpeta de curso (case-insensitive, sin acentos)
    target = strip_accents(only).lower()
    name = strip_accents(course_dir.name).lower()
    return target in name

def main():
    parser = argparse.ArgumentParser(
        description="Crea o sobrescribe index.qmd en /apuntes/anio-*/sem-*/<curso>/"
    )
    parser.add_argument(
        "--force", action="store_true",
        help="Sobrescribe index.qmd si ya existe."
    )
    parser.add_argument(
        "--backup", action="store_true",
        help="Guarda un respaldo .bak antes de sobrescribir (requiere --force)."
    )
    parser.add_argument(
        "--only", type=str, default=None,
        help='Procesa solo cursos cuyo nombre contenga este texto (ej: --only "Economía").'
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="No escribe archivos; solo muestra lo que haría."
    )
    args = parser.parse_args()

    if not BASE.exists():
        print("No encuentro la carpeta 'apuntes/'. ¿Estás en la raíz del repo?")
        return

    creados = 0
    sobrescritos = 0
    saltados = 0

    for anio_dir in sorted(BASE.glob("anio-*")):
        for sem_dir in sorted(anio_dir.glob("sem-*")):
            for course_dir in sorted(sem_dir.iterdir()):
                if not course_dir.is_dir():
                    continue
                if not should_process(course_dir, args.only):
                    continue

                index_qmd = course_dir / "index.qmd"
                titulo = course_title(course_dir)
                anio_code, sem_code = detect_codes(course_dir)
                banner_slug = slugify(titulo) + ".jpg"  # cambia a .png si prefieres

                content = TEMPLATE.format(
                    TITLE=titulo.replace('"', '\\"'),
                    ANIO=anio_code,
                    SEM=sem_code,
                    BANNER=banner_slug
                )

                if index_qmd.exists():
                    if not args.force:
                        print(f"⏭  Ya existe, no se sobrescribe (usa --force): {index_qmd}")
                        saltados += 1
                        continue
                    # con --force: opcional backup
                    if args.backup:
                        bak = backup_file(index_qmd)
                        print(f"💾  Backup creado: {bak}")
                    if args.dry_run:
                        print(f"[dry-run] Sobrescribiría: {index_qmd}")
                    else:
                        index_qmd.write_text(content, encoding="utf-8")
                        print(f"🔁 Sobrescrito: {index_qmd}")
                    sobrescritos += 1
                else:
                    if args.dry_run:
                        print(f"[dry-run] Crearía: {index_qmd}")
                    else:
                        index_qmd.write_text(content, encoding="utf-8")
                        print(f"✔ Creado: {index_qmd}")
                    creados += 1

    print("\nResumen:")
    print(f"  ✔ Nuevos creados     : {creados}")
    print(f"  🔁 Sobrescritos       : {sobrescritos}")
    print(f"  ⏭  Saltados (sin force): {saltados}")

if __name__ == "__main__":
    main()
