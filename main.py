import Text
import Name
import work_with_words
import letters

Text.Text()
filename = Name.Name()
try:
    work_with_words.Work_with_words(filename)
    letters.Letters(filename)
except FileNotFoundError:
    print(f"Файл '{filename}' не найден.")