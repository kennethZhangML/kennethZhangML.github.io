import re
import os

def format_latex_blocks_in_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    pattern = r"(\$\$[\s\S]*?\$\$)"
    
    def add_blank_lines(match):
        block = match.group(1)
        return f"\n{block}\n"

    formatted_content = re.sub(pattern, add_blank_lines, content)

    with open(file_path, 'w') as file:
        file.write(formatted_content)

def process_current_directory():
    for filename in os.listdir('.'):
        if filename.endswith('.md'):
            print(f"Processing {filename}")
            format_latex_blocks_in_file(filename)

process_current_directory()
