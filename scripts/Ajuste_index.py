#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path
import re
import argparse
import shutil

BASE = Path("apuntes")
NEW_DESC = 'Síntesis, resúmenes y apuntes del ramo.'  # ← la nueva descripción

def backup_file(path: Path) -> Path:
    bak = path.with_suffix(path.suffix + ".bak")
    if not bak.exists():
        shutil.copy2(path, bak)
        return bak
    i = 1
    while True:
        cand = path.with_suffix(path.suffix + f".bak.{i}")
        if not cand.exists():
            shutil.copy2(path, cand)
            return cand
        i += 1

def replace_description(frontmatter: str) -> str:
    """
    Reemplaza (o inserta si no existiera) description: "<...>" dentro del YAML.
    Solo actúa sobre el texto de frontmatter recibido (entre los ---).
    """
    # Si ya hay description: ... (en una línea)
    if re.search(r'(?m)^description:\s*(?:"[^"]*"|[^\n]+)\s*$', frontmatter):
        return re.sub(
            r'(?m)^(description:\s*)(?:"[^"]*"|[^\n]+)\s*$',
            rf'\1"{NEW_DESC}"',
            frontmatter
        )
    # Si no hay, lo insertamos tras 'title:' (si existe) o al inicio
    if re.search(r'(?m)^title:\s*', frontmatter):
        return re.sub(
            r'(?m)^(title:\s*[^\n]*\n)',
            rf'\1description: "{NEW_DESC}"\n',
            frontmatter,
            count=1
        )
    else:
        # lo ponemos al principio
        return f'description: "{NEW_DESC}"\n' + frontmatter

def remove_sobre_este_curso(body: str) -> str:
    """
    Elimina el bloque que inicia en '## Sobre este curso' hasta el siguiente encabezado
    (## o ###), o el bloque de listado, o el final del archivo.
    Es tolerante con espacios y variaciones leves.
    """
    patrón = (
        r'(?ms)'                                   # multi-línea + dotall
        r'^\s*##\s*Sobre\s+este\s+curso\s*\n'      # el título
        r'(?:.*?\n)*?'                              # contenido del bloque (no codicioso)
        r'(?='
        r'^\s*#{2,}\s'                              # siguiente encabezado (## o ###)
        r'|^\s*:::\s*\{#apuntes-curso\}'            # o el bloque de listing
        r'|\Z'                                      # o final de archivo
        r')'
    )
    return re.sub(patrón, '', body)

def process_file(path: Path, apply: bool, no_backup: bool) -> bool:
    text = path.read_text(encoding="utf-8")

    # separar front matter YAML y el resto del documento
    m = re.match(r'(?ms)^---\n(.*?)\n---\n(.*)$', text)
    if not m:
        # archivo sin front matter: solo eliminamos el bloque si existiera
        new_body = remove_sobre_este_curso(text)
        changed = (new_body != text)
        if changed and apply:
            if not no_backup: backup_file(path)
            path.write_text(new_body, encoding="utf-8")
        return changed

    fm, body = m.group(1), m.group(2)
    new_fm = replace_description(fm)
    new_body = remove_sobre_este_curso(body)

    new_text = f"---\n{new_fm}\n---\n{new_body}"
    changed = (new_text != text)

    if changed and apply:
        if not no_backup: backup_file(path)
        path.write_text(new_text, encoding="utf-8")

    return changed

def main():
    ap = argparse.ArgumentParser(
        description="Ajusta description y elimina bloque '## Sobre este curso' en todos los index.qmd."
    )
    ap.add_argument("--dry-run", action="store_true", help="Muestra cambios, no escribe.")
    ap.add_argument("--no-backup", action="store_true", help="No crear .bak antes de sobrescribir.")
    args = ap.parse_args()

    if not BASE.exists():
        print("No encuentro 'apuntes/'. Ejecútalo desde la raíz del repo.")
        return

    files = list(BASE.glob("anio-*/sem-*/**/index.qmd"))
    if not files:
        print("No se encontraron index.qmd.")
        return

    changed = 0
    for f in sorted(files):
        did = process_file(f, apply=not args.dry_run, no_backup=args.no_backup)
        if did:
            changed += 1
            print(("Modificado " if not args.dry_run else "[dry-run] Modificaría ") + str(f))

    print(f"\nListo. {('Modificados' if not args.dry_run else 'Marcaría para modificar')}: {changed} / {len(files)}")

if __name__ == "__main__":
    main()
