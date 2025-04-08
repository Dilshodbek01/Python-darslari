import math

# 1. capitalize()
print("hello".capitalize())  # 'Hello'

# 2. casefold()
print("HELLO".casefold())  # 'hello'

# 3. center()
print("hi".center(10))  # '    hi    '

# 4. count()
print("banana".count("a"))  # 3

# 5. encode()
print("hello".encode())  # b'hello'

# 6. endswith()
print("file.txt".endswith(".txt"))  # True

# 7. expandtabs()
print("a\tb".expandtabs(4))  # 'a   b'

# 8. find()
print("hello world".find("world"))  # 6

# 9. format()
print("My name is {}".format("Ulugʻbek"))  # 'My name is Ulugʻbek'

# 10. format_map()
print("Hello {name}".format_map({"name": "Ali"}))  # 'Hello Ali'

# 11. index()
print("hello".index("e"))  # 1

# 12. isalnum()
print("abc123".isalnum())  # True

# 13. isalpha()
print("abc".isalpha())  # True

# 14. isascii()
print("hello".isascii())  # True

# 15. isdecimal()
print("123".isdecimal())  # True

# 16. isdigit()
print("456".isdigit())  # True

# 17. isidentifier()
print("my_var".isidentifier())  # True

# 18. islower()
print("hello".islower())  # True

# 19. isspace()
print("   ".isspace())  # True

# 20. istitle()
print("Hello World".istitle())  # True

# 21. isupper()
print("HELLO".isupper())  # True

# 22. join()
print("-".join(["a", "b", "c"]))  # 'a-b-c'

# 23. lstrip()
print("  hello  ".lstrip())  # 'hello  '

# 24. rstrip()
print("  hello  ".rstrip())  # '  hello'

# 25. strip()
print("  hello  ".strip())  # 'hello'

# 26. partition()
print("hello world".partition(" "))  # ('hello', ' ', 'world')

# 27. replace()
print("hello world".replace("world", "Python"))  # 'hello Python'

# 28. split()
print("a,b,c".split(","))  # ['a', 'b', 'c']

# 29. splitlines()
print("hello\world".splitlines())  # ['hello', 'world']

# 30. startswith()
print("file.txt".startswith("file"))  # True

# 31. swapcase()
print("Hello World".swapcase())  # 'hELLO wORLD'

# 32. zfill()
print("42".zfill(5))  # '00042'
