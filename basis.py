a = True
b = []
print(type(a))      # <class 'bool'>
print(type(b))      # <class 'list'>
print(type('alex')) # <class 'str'>
print(type(3))      # <class 'int'>
print(type(3.5))    # <class 'float'>


text = 'Here is some random text'
print(text.find('h'))  # -1
print(text.find('H'))  # 0 - toto je indexové číslo, kde se dané písmeno nachází
