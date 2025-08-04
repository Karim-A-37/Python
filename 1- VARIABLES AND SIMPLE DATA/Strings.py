                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       

print("hello world")

message = "hello world?"
print(message)

message = "Not Hello World?"
print(message)

#print(mesage) # Name Error

# variables are labels we can assign to values not boxes contain values, we can also say it refrences the values.

# example->1
text = "way to find freedom."
print(text)

# example->2
sample_msg = "if you don't find yourself, try to find another self."
print(sample_msg)

sample_msg = "why you still searching?"
print(sample_msg)


# strings data types -> series of characters, anything inside quotes is considered string in python.

print("this is string")
print("this also is string")

# method is an action that python can perform on piece of data.

name = "crash course"
print(name.title())
print(name.upper())
print(name.lower())

# f-string or format-string

first_name = "test"
last_name = "user"
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"hello, {full_name.title()} to programming world")

print("python")
print("\tpython")
print("languages : GO \nPython \nC")

# strip => to remove whitespace from strings

lang = " Python "
print(lang)
# temp removed
print(lang.strip())
print(lang.rstrip())
print(lang.lstrip())
# perm removed
strip_lang = lang.strip()
print(strip_lang)
strip_lang = lang.rstrip()
print(strip_lang)
strip_lang = lang.lstrip()
print(strip_lang)

# remove prefix
url = "https://www.fsf.org"
simple_url = url.removeprefix("https://")
print(simple_url)


#A syntax error when your program is invalid Python code.
valid = "it's karim."
print(valid)
#invalid = 'it's karim.'
#print(invalid)
#	--------------------------------------------	#

# examples
# 1
name = "karim"
print(f"Hello {name},would you like to learn some Python today?")

# 2
name = "karim"
print(name.upper())
print(name.lower())
print(name.title())

# 3
print('Karim Abdelaziz once said,"you should get your limit or you will not be human."')

# 4 
name = "karim abdelaziz"
print(f'{name.title()} once said,\n\t"you should get your limit or you will not be human."')

# 5
name = "\n\tkarim\n\t"
print(name)
print(name.strip())
print(name.rstrip())
print(name.lstrip())

# 6
filename = "D:/crash_course.pdf"
print(filename.removeprefix("D:/"))
print(filename.removesuffix(".pdf"))
print(filename.removeprefix("D:/").removesuffix(".pdf"))











                                                                                                                                                                                             
