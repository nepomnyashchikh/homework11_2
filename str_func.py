def line(text):
    '''вызываем конфликт'''
    return text.upper()

def new_line(text):
    '''функция, которая делает заглавными первые буквы каждого слова в строке,
    поступившей на вход функции.'''
    return text.title()

print(line("Hello World!"))
print(new_line("hello world!"))