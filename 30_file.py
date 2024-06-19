from pathlib import Path

path = Path()
# print(path.exists())
# print((path.rmdir()))
# print((path.mkdir()))
for file in path.glob('*'):
    print(file)
# for file in path.glob('*.py'):
#     print(file)

