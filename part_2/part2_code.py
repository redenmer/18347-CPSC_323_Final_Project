# Group names: Ian Martinez, Kiara Guerra, Arturo Roman, Omar Montes
# Final Project Part 2
# Due date : 12/10/2024
# Purpose: Translate the file “final24” to Python language, run the program, and display its output.
#
#
# Starting with the functions to command everything

with open("final24.txt", "r", encoding="utf-8") as x:
    content = x.readlines()

py_language = []
for line in content:
    if "program" in line:
        line = "# Program f2024"
    elif "integer" in line:
        continue
    elif "var" in line:
        continue
    elif "begin" in line or "end" in line:
        continue
    elif ";" in line:
        line = line.replace(";", "")
    elif '"' in line:
        line = line.replace('“', '"').replace('”', '"')
    elif "print (" in line:
        line = line.replace('print ( ', 'print(')
    py_language.append(line.strip())


with open("final24.py", "w", encoding="utf-8") as f:
    f.write("\n".join(py_language))

