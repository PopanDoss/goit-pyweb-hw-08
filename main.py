from models import  Author, Quote
import connect


def parse_input(user_input):
    cmd, *args = user_input.split(":")
    cmd = cmd.strip().lower()
    return cmd, *args


print("Welcome to db_web_8")
    
while True:
    user_input = input("Enter a command: ")
    command, *args = parse_input(user_input)
    value = "".join(args)
    
    if command in ["close", "exit"]:
        print("Good bye!")
        break

    elif command == "name":

        author = Author.objects.get(fullname=value)
        quotes = Quote.objects(author=author)
        for quote in quotes:
            print(quote.quote)

    elif command == "tag":

        quotes = Quote.objects(tags=value)
        for quote in quotes:
            print(quote.quote)

    elif command == "tags":

        tags = value.split(",")
        quotes = Quote.objects(tags__in=tags)
        for quote in quotes:
            print(quote.quote)

        
        
        