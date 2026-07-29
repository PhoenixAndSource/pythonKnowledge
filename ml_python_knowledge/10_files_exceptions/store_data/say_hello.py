from pathlib import Path
import json

path = Path('name.json')
info = path.read_text()
name = json.loads(info)

print(f"Hi {name}!")
