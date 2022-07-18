import wikipediaapi

LETTERS = [
    'А', 'Б', 'В', 'Г',
    'Д', 'Е', 'Ё', 'Ж',
    'З', 'И', 'К', 'Л',
    'М', 'Н', 'О', 'П',
    'Р', 'С', 'Т', 'У',
    'Ф', 'Х', 'Ц', 'Ч',
    'Ш', 'Щ', 'Э', 'Ю',
    'Я',
]
ANIMALS = []


def animals_count(categorymembers, level=0, max_level=1):
    for member in categorymembers.values():
        if member.title == 'Категория:Животные по алфавиту':
            animals = member.categorymembers.keys()

    for animal in animals:
        ANIMALS.append(animal)

    for letter in LETTERS:
        count = 0
        for animal in ANIMALS:
            if letter == animal[0]:
                count = count + 1
        print(letter + ':', count)


wiki = wikipediaapi.Wikipedia('ru')
category = wiki.page("Категория:Животные")
animals_count(category.categorymembers)
