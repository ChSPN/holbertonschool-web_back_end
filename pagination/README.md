# Pagination Project
This repository contains a series of exercises focused on implementing pagination functionality in Python. The tasks are designed to help you understand and implement pagination techniques, working with datasets, and handling page ranges efficiently.

## Table of Contents
- Requirements
- Project Structure
- Tasks
  - Task 0: Simple Helper Function
  - Task 1: Simple Pagination
  - Task 2: Hypermedia Pagination
  - Task 3: Deletion-Resilient Hypermedia Pagination
- Usage
- Author

## Requirements
- **Editors**: vi, vim, emacs
- **Operating System**: Ubuntu 18.04 LTS
- **Python Version**: Python 3.7
- **Style**: PEP 8 (pycodestyle 2.5.x)
- All your files should end with a new line.
- The first line of all your Python files should be **#!/usr/bin/env python3** .
- A **README.md** file, at the root of the folder of the project, is mandatory.
- All your modules should have a documentation string (module docstring).
- All your functions should have a documentation string (function docstring).
- All your functions and coroutines must be type-annotated.

## Project Structure
The project directory is structured as follows:

``` 
pagination/
│
├── 0-simple_helper_function.py
├── 1-simple_pagination.py
├── 2-hypermedia_pagination.py
├── 3-hypermedia_del_pagination.py
├── Popular_Baby_Names.csv
├── 0-main.py
├── 1-main.py
├── 2-main.py
├── 3-main.py
└── README.md
```

- **0-simple_helper_function.py**: Contains the index_range function.
- **1-simple_pagination.py**: Contains the Server class with simple pagination implementation.
- **2-hypermedia_pagination.py**: Contains the Server class with hypermedia pagination implementation.
- **3-hypermedia_del_pagination.py**: Contains the Server class with deletion-resilient hypermedia pagination implementation.
- **Popular_Baby_Names.csv**: Dataset used for pagination.
- **0-main.py**: Main file for testing the index_range function.
- **1-main.py**: Main file for testing the simple pagination.
- **2-main.py**: Main file for testing the hypermedia pagination.
- **3-main.py**: Main file for testing the deletion-resilient pagination.
- **README.md**: This file, providing an overview of the project.

## Tasks
### Task 0: Simple Helper Function
**File: 0-simple_helper_function.py**

Implement a function named **index_range** that takes two integer arguments **page** and **page_size**. The function should return a tuple of size two containing the start index and end index for the pagination parameters.

- Example:
```
index_range(1, 7)  # returns (0, 7)
index_range(3, 15) # returns (30, 45)
```

### Task 1: Simple Pagination
**File: 1-simple_pagination.py**

Implement the **Server** class that handles the pagination of a dataset. The class should include:
- A **dataset** method that loads and caches the dataset.
- A **get_page** method that returns the correct page from the dataset using the index_range function.

The **get_page** method should assert that **page** and **page_size** are valid integers greater than 0 and return the corresponding page of data. If the requested page is out of range, return an empty list.

- Example:
```
server = Server()
print(server.get_page(1, 3))  # Returns the first 3 items on page 1
print(server.get_page(3, 2))  # Returns 2 items from page 3
```

### Task 2: Hypermedia Pagination
**File: 2-hypermedia_pagination.py**

Extend the Server class to implement hypermedia pagination. Add a method get_hyper that takes the same arguments as get_page and returns a dictionary containing the following key-value pairs:
- **page_size**: The current page size.
- **page**: The current page number.
- **data**: The actual page data.
- **next_page**: The next page number, or **None** if no next page exists.
- **prev_page**: The previous page number, or **None** if no previous page exists.
- **total_pages**: The total number of pages.

- Example:

```
server = Server()
print(server.get_hyper(1, 3))
``` 

### Task 3: Deletion-Resilient Hypermedia Pagination
**File: 3-hypermedia_del_pagination.py**

Update the **Server** class to handle deletion-resilient pagination. Modify the **get_hyper** method to ensure that the pagination system can handle datasets where rows can be deleted. This method should behave like **get_hyper**, but it should adapt to changes in the dataset, maintaining the integrity of pagination.

- Example:
```
server = Server()
print(server.get_hyper(1, 3))
```

## Usage
To run the tests for each task, you can use the following commands in your terminal:

```
$ ./0-main.py
$ ./1-main.py
$ ./2-main.py
$ ./3-main.py
```
Ensure that the CSV file (**Popular_Baby_Names.csv**) is in the same directory as your Python scripts.

## Example Output
```
$ ./1-main.py
AssertionError raised with negative values
AssertionError raised with 0
AssertionError raised when page and/or page_size are not ints
[['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Olivia', '172', '1'], ['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Chloe', '112', '2'], ['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Sophia', '104', '3']]
[['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Emily', '99', '4'], ['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Mia', '79', '5']]
[]
```

## Author
Charlène