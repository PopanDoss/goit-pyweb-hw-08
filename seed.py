import json
from datetime import datetime
from models import Author, Quote
import connect


with open('files\\authors.json', 'r', encoding='utf-8') as file:
    authors_data = json.load(file)
    for author_info in authors_data:
        born_date = datetime.strptime(author_info['born_date'], '%B %d, %Y')
        author = Author(
            fullname=author_info['fullname'],
            born_date=born_date,
            born_location=author_info['born_location'],
            description=author_info['description']
        )
        author.save()

# Зчитуємо дані з файлу quotes.json та зберігаємо їх у колекції цитат
with open('files\\qoutes.json', 'r', encoding='utf-8') as file:
    quotes_data = json.load(file)
    for quote_info in quotes_data:
        author_name = quote_info['author']
        author = Author.objects(fullname=author_name).first()  # Знаходимо автора за ім'ям
        if author:
            quote = Quote(
                tags=quote_info['tags'],
                quote=quote_info['quote'],
                author=author
            )
            quote.save()
        else:
            print(f"Author '{author_name}' not found.")