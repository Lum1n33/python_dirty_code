import Text
import Name
import Osnova
import Funk

Text.Text()
filename = Name.Name()
try:
    Osnova.Osnova(filename)
    Funk.Funk(filename)
except FileNotFoundError:
    print(f"Файл '{filename}' не найден.")