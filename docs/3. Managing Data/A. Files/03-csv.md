# Reading and Writing CSV Files

## Overview

CSV (Comma-Separated Values) files are one of the most common formats for storing tabular data. Python's built-in `csv`
module provides powerful tools for reading and writing CSV files while handling many edge cases automatically.

## Why Use the `csv` Module?

While you could read CSV files with basic file operations, the `csv` module handles:

- Quoted fields containing commas
- Escaped quotes within fields
- Different delimiters (commas, semicolons, tabs)
- Line breaks within quoted fields
- Various CSV dialects and formats

## Basic CSV Reading

### Method 1: Reading as Lists

```python
import csv

# Read CSV file row by row
with open('data.csv', 'r', encoding='utf-8', newline='') as file:
    csv_reader = csv.reader(file)

    # Read header row
    header = next(csv_reader)
    print("Header:", header)

    # Read data rows
    for row in csv_reader:
        print(row)
```

### Method 2: Reading as Dictionaries

```python
import csv

# Read CSV with column names as dictionary keys
with open('data.csv', 'r', encoding='utf-8', newline='') as file:
    csv_reader = csv.DictReader(file)

    for row in csv_reader:
        print(f"Name: {row['name']}, Age: {row['age']}, City: {row['city']}")
```

## Basic CSV Writing

### Method 1: Writing Lists

```python
import csv

# Write data as lists
data = [
    ['Name', 'Age', 'City'],
    ['Alice', '25', 'New York'],
    ['Bob', '30', 'San Francisco'],
    ['Charlie', '35', 'Chicago']
]

with open('output.csv', 'w', encoding='utf-8', newline='') as file:
    csv_writer = csv.writer(file)

    for row in data:
        csv_writer.writerow(row)

    # Or write all rows at once
    # csv_writer.writerows(data)
```

### Method 2: Writing Dictionaries

```python
import csv

# Define data as dictionaries
data = [
    {'name': 'Alice', 'age': 25, 'city': 'New York'},
    {'name': 'Bob', 'age': 30, 'city': 'San Francisco'},
    {'name': 'Charlie', 'age': 35, 'city': 'Chicago'}
]

fieldnames = ['name', 'age', 'city']

with open('output.csv', 'w', encoding='utf-8', newline='') as file:
    csv_writer = csv.DictWriter(file, fieldnames=fieldnames)

    # Write header
    csv_writer.writeheader()

    # Write data rows
    for row in data:
        csv_writer.writerow(row)

    # Or write all rows at once
    # csv_writer.writerows(data)
```

## Handling Different CSV Formats

### Custom Delimiters

```python
import csv

# Reading a semicolon-separated file
with open('data.csv', 'r', encoding='utf-8', newline='') as file:
    csv_reader = csv.reader(file, delimiter=';')
    for row in csv_reader:
        print(row)

# Writing with custom delimiter
with open('output.csv', 'w', encoding='utf-8', newline='') as file:
    csv_writer = csv.writer(file, delimiter=';')
    csv_writer.writerow(['Name', 'Age', 'City'])
    csv_writer.writerow(['Alice', '25', 'New York'])
```

### Tab-Separated Values (TSV)

```python
import csv

# Reading TSV files
with open('data.tsv', 'r', encoding='utf-8', newline='') as file:
    csv_reader = csv.reader(file, delimiter='\t')
    for row in csv_reader:
        print(row)

# Writing TSV files
with open('output.tsv', 'w', encoding='utf-8', newline='') as file:
    csv_writer = csv.writer(file, delimiter='\t')
    csv_writer.writerow(['Name', 'Age', 'City'])
```

### Handling Quotes and Special Characters

```python
import csv

# Data with commas and quotes
data = [
    ['Name', 'Description', 'Price'],
    ['Apple iPhone', 'Latest "flagship" phone, very expensive', '$999'],
    ['Samsung Galaxy', 'Android phone, good value', '$699'],
    ['Google Pixel', 'Pure Android experience, excellent camera', '$799']
]

# Write with proper quoting
with open('products.csv', 'w', encoding='utf-8', newline='') as file:
    csv_writer = csv.writer(file, quoting=csv.QUOTE_ALL)  # Quote all fields
    csv_writer.writerows(data)

# Different quoting options:
# csv.QUOTE_ALL - Quote all fields
# csv.QUOTE_MINIMAL - Quote only when necessary (default)
# csv.QUOTE_NONNUMERIC - Quote all non-numeric fields
# csv.QUOTE_NONE - Never quote (use with caution)
```

## Practical Examples

### Example 1: Student Grade Manager

```python
import csv


def read_grades(filename):
    """Read student grades from CSV file"""
    students = []
    try:
        with open(filename, 'r', encoding='utf-8', newline='') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                # Convert string grades to integers
                student = {
                    'name': row['name'],
                    'math': int(row['math']),
                    'science': int(row['science']),
                    'english': int(row['english'])
                }
                students.append(student)
    except FileNotFoundError:
        print(f"File {filename} not found")
        return []
    except ValueError as e:
        print(f"Error converting grades to numbers: {e}")
        return []

    return students


def calculate_averages(students):
    """Calculate average grade for each student"""
    for student in students:
        avg = (student['math'] + student['science'] + student['english']) / 3
        student['average'] = round(avg, 2)
    return students


def write_grades_with_averages(students, filename):
    """Write students and their averages to CSV"""
    fieldnames = ['name', 'math', 'science', 'english', 'average']

    with open(filename, 'w', encoding='utf-8', newline='') as file:
        csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
        csv_writer.writeheader()
        csv_writer.writerows(students)


# Usage
students = read_grades('grades.csv')
students_with_avg = calculate_averages(students)
write_grades_with_averages(students_with_avg, 'grades_with_averages.csv')
print(f"Processed {len(students)} students")
```

### Example 2: Sales Data Analysis

```python
import csv
from datetime import datetime


def read_sales_data(filename):
    """Read sales data and convert data types"""
    sales = []

    with open(filename, 'r', encoding='utf-8', newline='') as file:
        csv_reader = csv.DictReader(file)

        for row in csv_reader:
            sale = {
                'date': datetime.strptime(row['date'], '%Y-%m-%d'),
                'product': row['product'],
                'quantity': int(row['quantity']),
                'price': float(row['price']),
                'salesperson': row['salesperson']
            }
            sale['total'] = sale['quantity'] * sale['price']
            sales.append(sale)

    return sales


def generate_sales_report(sales, output_filename):
    """Generate a sales summary report"""
    # Calculate totals by salesperson
    salesperson_totals = {}

    for sale in sales:
        person = sale['salesperson']
        if person not in salesperson_totals:
            salesperson_totals[person] = {'sales': 0, 'revenue': 0.0}

        salesperson_totals[person]['sales'] += sale['quantity']
        salesperson_totals[person]['revenue'] += sale['total']

    # Write report
    with open(output_filename, 'w', encoding='utf-8', newline='') as file:
        fieldnames = ['salesperson', 'total_sales', 'total_revenue', 'avg_per_sale']
        csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
        csv_writer.writeheader()

        for person, data in salesperson_totals.items():
            avg_per_sale = data['revenue'] / data['sales'] if data['sales'] > 0 else 0
            csv_writer.writerow({
                'salesperson': person,
                'total_sales': data['sales'],
                'total_revenue': round(data['revenue'], 2),
                'avg_per_sale': round(avg_per_sale, 2)
            })


# Usage
sales_data = read_sales_data('sales.csv')
generate_sales_report(sales_data, 'sales_report.csv')
```

### Example 3: Data Cleaning and Validation

```python
import csv
import re


def validate_email(email):
    """Simple email validation"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


def clean_phone_number(phone):
    """Clean and format phone number"""
    # Remove all non-digit characters
    digits = re.sub(r'\D', '', phone)

    # Format as (XXX) XXX-XXXX if 10 digits
    if len(digits) == 10:
        return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
    elif len(digits) == 11 and digits[0] == '1':
        return f"({digits[1:4]}) {digits[4:7]}-{digits[7:]}"
    else:
        return phone  # Return original if can't format


def clean_customer_data(input_filename, output_filename, error_filename):
    """Clean customer data and separate errors"""
    clean_data = []
    error_data = []

    with open(input_filename, 'r', encoding='utf-8', newline='') as file:
        csv_reader = csv.DictReader(file)

        for row_num, row in enumerate(csv_reader, start=2):  # Start at 2 for header
            errors = []

            # Clean and validate data
            name = row['name'].strip().title()
            email = row['email'].strip().lower()
            phone = clean_phone_number(row['phone'])

            # Validate
            if not name:
                errors.append("Missing name")
            if not validate_email(email):
                errors.append("Invalid email")
            if not phone or len(re.sub(r'\D', '', phone)) < 10:
                errors.append("Invalid phone")

            # Prepare cleaned row
            cleaned_row = {
                'name': name,
                'email': email,
                'phone': phone
            }

            if errors:
                cleaned_row['errors'] = '; '.join(errors)
                cleaned_row['row_number'] = row_num
                error_data.append(cleaned_row)
            else:
                clean_data.append(cleaned_row)

    # Write clean data
    if clean_data:
        with open(output_filename, 'w', encoding='utf-8', newline='') as file:
            fieldnames = ['name', 'email', 'phone']
            csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
            csv_writer.writeheader()
            csv_writer.writerows(clean_data)

    # Write error data
    if error_data:
        with open(error_filename, 'w', encoding='utf-8', newline='') as file:
            fieldnames = ['row_number', 'name', 'email', 'phone', 'errors']
            csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
            csv_writer.writeheader()
            csv_writer.writerows(error_data)

    return len(clean_data), len(error_data)


# Usage
clean_count, error_count = clean_customer_data(
    'customers_raw.csv',
    'customers_clean.csv',
    'customers_errors.csv'
)
print(f"Cleaned {clean_count} records, {error_count} errors found")
```

## Advanced Features

### Working with Large CSV Files

```python
import csv


def process_large_csv(filename, batch_size=1000):
    """Process large CSV files in batches"""
    with open(filename, 'r', encoding='utf-8', newline='') as file:
        csv_reader = csv.DictReader(file)

        batch = []
        for row in csv_reader:
            batch.append(row)

            if len(batch) >= batch_size:
                # Process batch
                process_batch(batch)
                batch = []

        # Process remaining rows
        if batch:
            process_batch(batch)


def process_batch(batch):
    """Process a batch of rows"""
    print(f"Processing batch of {len(batch)} rows")
    # Your processing logic here
```

### Custom CSV Dialects

```python
import csv

# Define a custom CSV dialect
csv.register_dialect('custom',
                     delimiter='|',
                     quotechar='"',
                     quoting=csv.QUOTE_MINIMAL,
                     lineterminator='\n')

# Use the custom dialect
with open('data.csv', 'w', encoding='utf-8', newline='') as file:
    csv_writer = csv.writer(file, dialect='custom')
    csv_writer.writerow(['Name', 'Age', 'City'])
    csv_writer.writerow(['Alice', '25', 'New York'])
```

## Error Handling Best Practices

```python
import csv


def robust_csv_reader(filename):
    """Read CSV with comprehensive error handling"""
    try:
        with open(filename, 'r', encoding='utf-8', newline='') as file:
            # Try to detect the dialect
            sample = file.read(1024)
            file.seek(0)

            try:
                dialect = csv.Sniffer().sniff(sample)
                csv_reader = csv.reader(file, dialect)
            except csv.Error:
                # Fall back to default
                csv_reader = csv.reader(file)

            data = []
            for row_num, row in enumerate(csv_reader, start=1):
                try:
                    # Process row
                    data.append(row)
                except Exception as e:
                    print(f"Error processing row {row_num}: {e}")
                    continue

            return data

    except FileNotFoundError:
        print(f"File {filename} not found")
        return []
    except PermissionError:
        print(f"Permission denied accessing {filename}")
        return []
    except UnicodeDecodeError as e:
        print(f"Encoding error: {e}")
        return []
    except csv.Error as e:
        print(f"CSV parsing error: {e}")
        return []


# Usage
data = robust_csv_reader('data.csv')
```

## Key Points to Remember

1. **Always use `newline=''`** when opening CSV files to prevent extra blank rows on Windows
2. **Specify encoding** (preferably UTF-8) for consistent behavior across platforms
3. **Use `DictReader` and `DictWriter`** for more readable code when working with headers
4. **Handle data type conversions** explicitly (CSV reads everything as strings)
5. **Validate and clean data** as you read it
6. **Use proper quoting** when writing CSV files with special characters
7. **Handle errors gracefully** with try-except blocks
8. **Consider memory usage** when working with large files

## Common Mistakes to Avoid

- Not using `newline=''` parameter (causes extra blank rows)
- Forgetting that CSV module reads everything as strings
- Not handling commas, quotes, or newlines within data properly
- Assuming all CSV files use comma delimiters
- Not validating data types when reading
- Forgetting to write headers when using `DictWriter`
- Not handling encoding issues properly

This guide provides a solid foundation for working with CSV files in Python, handling the most common scenarios and edge
cases you'll encounter in real-world applications.


---------------

??? info "Use of AI"
    Page written in part with the help of an AI assistant, mainly using Perplexity AI. The AI was used to generate
    explanations, examples and/or structure suggestions. All information has been verified, edited and completed by
    the author.