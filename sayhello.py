with open('name.txt') as f:
    my_name = f.read()

sentence = "Hello, my name is " + my_name

with open('hello.txt', 'w') as f:
    f.write(sentence)