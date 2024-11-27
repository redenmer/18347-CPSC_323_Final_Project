# Group names: Ian Martinez, Kiara Guerra, Arturo Roman, Omar Montes
# Final Project Part 1
# Due date : 12/10/2024
# Purpose: Applies the following rules to final.txt file and copies the new version in file “final24.txt”
#          1.Any line/s or part of a line that begins with (* and ends with *) is/are considered as a
#          comment line(s) (i.e. lines #2-3,5, 11,13,15), remove them all
#
#          2.Any blank lines must be removed (i.e. lines #12, 16)
#
#          3.Extra spaces in each line must be removed, leaving one space before and one after each token
#          to make tokenization easier

# Read lines beginning and ending with "(*" & "*) as comments and removes them entirely
def remove_comments(s):
    while '(*' in s and '*)' in s:
        start = s.find('(*')
        end = s.find('*)', start) + 2
        s = s[:start] + s[end:]
    s = s.replace('a1', 'a')
    return s

# Reads each line from final.txt and removes any line that is empty
def remove_empty_lines_and_excessive_spacing(s):
    # Remove empty lines
    lines = s.split('\n')
    non_empty_lines = [line for line in lines if line.strip() != '']

    # Remove excessive spacing
    cleaned_lines = [' '.join(line.split()) for line in non_empty_lines]

    return '\n'.join(cleaned_lines)

# Read the content of the file "final.txt" as a string under utf-8 format
# so that tokens: " can be read
with open("final.txt", "r", encoding="utf-8") as x:
    content = x.read()

# Cleaning process of the file
cleaned = remove_comments(content)
cleaned = remove_empty_lines_and_excessive_spacing(cleaned)

# Print the cleaned content in utf-8 format so each token can be printed
with open("final24.txt", "w", encoding="utf-8") as f:
    f.write(cleaned)