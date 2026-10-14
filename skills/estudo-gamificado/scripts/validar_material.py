"""Verificar recursos Markdown locais sem rede ou execução de código.

Uso: python validar_material.py PASTA [--check-python]
"""
from __future__ import annotations
import argparse
import ast
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

LINK = re.compile(r'!?\[[^\]\n]*\]\(\s*(?:<([^>\n]+)>|([^\s)]+))(?:\s+["\'][^\n]*?["\'])?\s*\)')
REFERENCE = re.compile(r'^\s*\[[^\]]+\]:\s*(?:<([^>\n]+)>|(\S+))', re.M)
IGNORED = {'.git', '.venv', 'venv', '__pycache__', 'node_modules'}


def markdown_links(text):
    visible, fence = [], None
    for line in text.splitlines():
        marker = re.match(r'^\s{0,3}(`{3,}|~{3,})', line)
        if marker:
            token = marker.group(1)
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence):
                fence = None
            continue
        if fence is None:
            visible.append(line)
    text = '\n'.join(visible)
    for pattern in (LINK, REFERENCE):
        for match in pattern.finditer(text):
            yield match.group(1) or match.group(2)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('pasta', type=Path)
    parser.add_argument('--check-python', action='store_true', help='Conferir sintaxe .py sem executar')
    args = parser.parse_args()
    root = args.pasta.resolve()
    if not root.is_dir():
        parser.error('A pasta deve existir')
    errors, checked, links = [], 0, 0
    for file in sorted(root.rglob('*')):
        if not file.is_file() or any(p in IGNORED for p in file.relative_to(root).parts):
            continue
        if file.suffix.lower() != '.md' and not (args.check_python and file.suffix.lower() == '.py'):
            continue
        try:
            text = file.read_text(encoding='utf-8-sig')
        except UnicodeError as error:
            errors.append(f'{file.relative_to(root)}: texto não é UTF-8: {error}')
            continue
        checked += 1
        if file.suffix.lower() == '.py':
            try:
                ast.parse(text, filename=str(file))
            except SyntaxError as error:
                errors.append(f'{file.relative_to(root)}:{error.lineno}: sintaxe Python: {error.msg}')
            continue
        for target in markdown_links(text):
            if target.startswith('#') or urlsplit(target).scheme or target.startswith('//'):
                continue
            path = unquote(urlsplit(target).path)
            # Rotas /arquivo dependem da raiz de publicação, não desta pasta.
            if not path or path.startswith('/'):
                continue
            links += 1
            if not (file.parent / path).exists():
                errors.append(f'{file.relative_to(root)}: recurso local ausente: {target}')
    for error in errors:
        print(f'ERRO: {error}', file=sys.stderr)
    print(f'{checked} arquivos conferidos; {links} referências locais; {len(errors)} erros.')
    return 1 if errors else 0


if __name__ == '__main__':
    sys.exit(main())
