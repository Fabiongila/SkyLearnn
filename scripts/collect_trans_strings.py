from pathlib import Path
import re
root = Path(__file__).resolve().parent.parent / 'templates'
strings = set()
for path in sorted(root.rglob('*.html')):
    txt = path.read_text(encoding='utf-8')
    strings.update(re.findall(r"\{\%\s*trans\s+'([^']+)'\s*\%\}", txt))
    strings.update(re.findall(r"\{\%\s*trans\s+\"([^\"]+)\"\s*\%\}", txt))
for s in sorted(strings):
    print(s)
print('TOTAL', len(strings))
