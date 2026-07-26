import keyword
identifiers = [
    "2value",
    "value_2",
    "_hidden",
    "class",
    "my-var",
    "MyClass",
    "total$"
]
for i in identifiers:
    if i.isidentifier() and not keyword.iskeyword(i):
        print(i,"-> Valid Identifier")
    else:
        print(i, "->Invalid Identifier")
