
def format_name(f_name, l_name):
    """ Take a first and last name and title case version of name"""
    if f_name == "" or l_name == "":
        return "You din not provide valid inputs"
    return (f_name.title() + " " + l_name.title())


print(format_name("kot", "ali"))
