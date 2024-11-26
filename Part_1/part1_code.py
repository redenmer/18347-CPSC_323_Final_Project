def remove_comments(s):
    while '(*' in s and '*)' in s:
        start = s.find('(*')
        end = s.find('*)', start) + 2
        s = s[:start] + s[end:]
    return s

def remove_empty_lines_and_excessive_spacing(s):
    # Remove empty lines
    lines = s.split('\n')
    non_empty_lines = [line for line in lines if line.strip() != '']

    # Remove excessive spacing
    cleaned_lines = [' '.join(line.split()) for line in non_empty_lines]

    return '\n'.join(cleaned_lines)

# Read the content of the file "final.txt"
with open("final.txt", "r", encoding="utf-8") as x:
    content = x.read()

# Clean the content
cleaned = remove_comments(content)
cleaned = remove_empty_lines_and_excessive_spacing(cleaned)

# Print the cleaned content
with open("final24.txt", "w", encoding="utf-8") as f:
    f.write(cleaned)