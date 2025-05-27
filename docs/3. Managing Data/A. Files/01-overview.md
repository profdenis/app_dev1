# Reading and Writing Files

## Overview

File operations are essential in Python programming. This guide covers the fundamentals of reading and writing text
files using Python's built-in `open()` function.

## The `open()` Function

The `open()` function is Python's primary way to work with files. Its basic syntax is:

```python
file_object = open(filename, mode)
```

### Common File Modes

- `'r'` - Read mode (default)
- `'w'` - Write mode (overwrites existing content)
- `'a'` - Append mode (adds to end of file)
- `'x'` - Exclusive creation (fails if file exists)

## Reading Files

### Method 1: Reading the Entire File

```python
# Open and read entire file
file = open('example.txt', 'r')
content = file.read()
print(content)
file.close()
```

### Method 2: Reading Line by Line

```python
# Read line by line
file = open('example.txt', 'r')
for line in file:
    print(line.strip())  # strip() removes newline characters
file.close()
```

### Method 3: Reading Lines into a List

```python
# Read all lines into a list
file = open('example.txt', 'r')
lines = file.readlines()
file.close()

for line in lines:
    print(line.strip())
```

## Writing Files

### Writing New Content (Overwrites Existing)

```python
# Write to file (creates new or overwrites existing)
file = open('output.txt', 'w')
file.write('Hello, World!\n')
file.write('This is a new line.')
file.close()
```

### Appending to Existing Files

```python
# Append to existing file
file = open('output.txt', 'a')
file.write('\nThis line is appended.')
file.close()
```

### Writing Multiple Lines

```python
# Write multiple lines at once
lines = ['First line\n', 'Second line\n', 'Third line\n']
file = open('output.txt', 'w')
file.writelines(lines)
file.close()
```

## Best Practice: Using Context Managers

The `with` statement automatically handles file closing, even if an error occurs:

```python
# Reading with context manager
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
# File is automatically closed here

# Writing with context manager
with open('output.txt', 'w') as file:
    file.write('Hello, World!')
# File is automatically closed here
```

## Error Handling

Always handle potential file errors:

```python
try:
    with open('nonexistent.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found!")
except PermissionError:
    print("Permission denied!")
except Exception as e:
    print(f"An error occurred: {e}")
```

## Practical Examples

### Example 1: Simple File Copy

```python
# Copy contents from one file to another
try:
    with open('source.txt', 'r') as source:
        with open('destination.txt', 'w') as dest:
            dest.write(source.read())
    print("File copied successfully!")
except FileNotFoundError:
    print("Source file not found!")
```

### Example 2: Counting Words in a File

```python
def count_words(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            words = content.split()
            return len(words)
    except FileNotFoundError:
        return "File not found"


word_count = count_words('example.txt')
print(f"Word count: {word_count}")
```

### Example 3: Creating a Simple Log File

```python
import datetime


def write_log(message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('log.txt', 'a') as log_file:
        log_file.write(f"{timestamp}: {message}\n")


# Usage
write_log("Program started")
write_log("Processing data")
write_log("Program completed")
```

## Key Points to Remember

1. Always close files after opening them (or use `with` statements)
2. Use appropriate file modes for your needs
3. Handle exceptions when working with files
4. The `with` statement is the preferred way to work with files
5. Use `strip()` to remove unwanted whitespace from lines
6. Write mode (`'w'`) overwrites existing files completely
7. Append mode (`'a'`) adds content to the end of existing files

## Common Mistakes to Avoid

- Forgetting to close files (causes resource leaks)
- Using write mode when you meant to append
- Not handling file exceptions
- Forgetting to add newline characters (`\n`) when writing
- Not checking if a file exists before trying to read it

This foundation will serve you well as you progress to more advanced file operations and external libraries for specific
file formats.

---------------

??? info "Use of AI"
    Page written in part with the help of an AI assistant, mainly using Perplexity AI. The AI was used to generate
    explanations, examples and/or structure suggestions. All information has been verified, edited and completed by
    the author.