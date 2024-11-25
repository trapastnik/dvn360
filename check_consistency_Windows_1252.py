import argparse
import re

def fix_unbalanced_parentheses(content):
    lines = content.split('\n')
    line_num = 1
    new_content = ''
    for line in lines:
        open_parentheses = line.count('(')
        close_parentheses = line.count(')')
        if open_parentheses > close_parentheses:
            diff = open_parentheses - close_parentheses
            line += ')' * diff
            print(f"Added {diff} closing parentheses to line {line_num}")
        new_content += line + '\n'
        line_num += 1
    return new_content

def fix_sql_consistency(content):
    keywords = {'SELECT', 'FROM', 'WHERE', 'JOIN', 'INNER', 'LEFT', 'RIGHT', 'ON', 'ORDER BY', 'GROUP BY', 'HAVING', 'INSERT INTO', 'VALUES', 'UPDATE', 'SET', 'DELETE', 'CREATE TABLE', 'ALTER TABLE', 'DROP TABLE'}

    content = re.sub(' +', ' ', content)

    for keyword in keywords:
        content = re.sub(rf'\b{keyword}\b', keyword.upper(), content, flags=re.IGNORECASE)

    content = re.sub(r'(?<=[^;])\s*$', ';', content, flags=re.MULTILINE)

    return content

def fix_sql_file(file_path, show_progress=True, output_file=None):
    with open(file_path, mode='r', encoding='Windows-1252') as f:
        content = f.read()

    content = re.sub(r'--.*', '', content)
    content = re.sub(r'/\*[\s\S]*?\*/', '', content)

    new_content = fix_unbalanced_parentheses(content)
    new_content = fix_sql_consistency(new_content)

    if output_file is not None:
        with open(output_file, mode='w', encoding='Windows-1252') as f:
            f.write(new_content)
        print(f"The fixed SQL content has been written to {output_file}")
    else:
        with open(f"{file_path}_fixed", mode='w', encoding='Windows-1252') as f:
            f.write(new_content)
        print(f"The fixed SQL content has been written to {file_path}_fixed")

    if show_progress:
        print("Finished fixing the SQL file.")
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Fix unbalanced parentheses and inconsistencies in a SQL file.')
    parser.add_argument('file_path', metavar='file_path', type=str, help='Path to SQL file')
    parser.add_argument('-p', '--show_progress', action='store_true', help='Toggle progress tracking')
    parser.add_argument('-o', '--output_file', metavar='output_file', type=str, help='Output file name to write the fixed SQL content')
    args = parser.parse_args()

    is_fixed = fix_sql_file(args.file_path, args.show_progress, args.output_file)

    if not is_fixed:
        print("Error: Failed to fix the SQL file.")