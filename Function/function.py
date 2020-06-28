def python_food():
    print('Hello world')

print(python_food())

def center_text(*args, sep=' ', end="\n", file=None, flush=False):
    text = ""
    for arg in args:
        text += str(arg) + sep
    left_margin = (80 - len(text)) // 2
    text = text.strip(';')
    return " " * left_margin + text

# with open("centered.txt", "w") as centered_file:
s1 = center_text("hello world")
print(s1)
print(center_text("my name is Mei"))
print(center_text("hello world", 'my name is Mei', sep=';'))