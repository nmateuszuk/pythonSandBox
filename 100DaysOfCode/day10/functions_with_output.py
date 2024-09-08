def my_function():
    return 3*2


output = my_function


def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You din not provide valid inputs"
    return (f_name.title() + " " + l_name.title())


print(format_name("kot", "ali"))


def function1(text):
    return text + text


def function2(text):
    return text.title()


output = function2(function1("hello"))
print(output)
