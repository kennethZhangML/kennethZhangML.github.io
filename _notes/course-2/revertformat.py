import re
import os

def remove_blank_lines_around_latex(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    # Match LaTeX blocks with optional blank lines before and after
    pattern = r"\n*\s*(\$\$[\s\S]*?\$\$)\s*\n*"
    
    def remove_surrounding_newlines(match):
        block = match.group(1)
        return block  # Return only the block, no extra newlines

    cleaned_content = re.sub(pattern, remove_surrounding_newlines, content)

    with open(file_path, 'w') as file:
        file.write(cleaned_content)

def process_current_directory():
    for filename in os.listdir('.'):
        if filename.endswith('.md'):
            print(f"Cleaning {filename}")
            remove_blank_lines_around_latex(filename)

process_current_directory()
