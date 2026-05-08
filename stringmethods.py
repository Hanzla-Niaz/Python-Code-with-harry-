#String methods
a="Hanzla!! !!Hanzla"
b="hanzla niaz"
#Uppercase(Convert every character to uppercase)
print(a.upper())
#Lower case(Convert every character to lowercase)
print(a.lower())
#rstrip() remove the trailing characters(last one's)
print(a.rstrip("!"))
#replace() (replace the string with another string)(all occurences)
print(a.replace("Hanzla","Zafar"))
#split() (split the string as lists)
print(a.split(" "))
#capitalize()
print(b.capitalize())
#center() (aligns at the center)
print(b.center(50))
#count() tells the no of times a character occured.
print(a.count("a"))
#endswith() checks whether it ends with that give value or not
print(a.endswith("b"))
#also endswith() tells that a given elements
#exsists in between the string or not.
print(a.endswith("Hanzla",0,6))
#find() tells the first occurence and returns the index.
#and if not return -1
print(a.find("a"))
#index() same as find() but gives error if not found.
print(a.index("a"))
#isalnum() true if string consist A-Z,a-z,0-9
#if other characters and punctuations are present then false.
print(a.isalnum())
#isalpha() True->A-Z,a-z, False->punctuation and 0-9
str1="Welcome"
print(str1.isalpha())
#islower() True-> is all lowercase 
#isprintable() gives false if there is non printable characters
str2="Welcome to Multan\n"
print(str2.isprintable())
#isspace True->if string contains white spaces.
str3=" "
print(str3.isspace())

