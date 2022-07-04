""" Stripping Names: 
Store a person’s name, and include some whitespace characters at the beginning and end of the name. 
Make sure you use each character combination, "\t" and "\n", at least once.
"""

name = " Albert Einstein "
message = "Imagination is more important than knowledge."

# remove space
print(f'\t{name.strip()} once said, "{message}"\n')

# remove right space
print(f'\t{name.rstrip()} once said, "{message}"\n')

# remove left space
print(f'\t{name.lstrip()} once said, "{message}"\n')
