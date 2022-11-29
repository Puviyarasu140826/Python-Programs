from pathlib import Path

file = Path('my_file.txt')
print(file.stat().st_size)
