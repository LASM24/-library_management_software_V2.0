# Library Management Software V2.0

Welcome to the latest version of the library management software!

![Library Management Software](https://miro.medium.com/v2/resize:fit:1200/1*4GUqSsl4hkvUOPi_K3poVA.png)

<div align="center">
    <img width="150" src="https://i.imgur.com/dca7pcI.png" alt="py_logo">
    <img width="150" src="https://www.postgresql.org/media/img/about/press/elephant.png" alt="pg_logo">
    <img src="https://www.sqlalchemy.org/img/sqla_logo.png" alt="alchemy_logo" style="display:block;margin:auto;">
</div>


## Overview

This latest iteration of the "Library Management Software" project is developed using `Python`, `SQLAlchemy Core` and `PostgreSQL`. It enables users to interact with the system via the console.
Users can perform various tasks such as adding a book, viewing the list of available books, updating book information, and deleting books. Unlike its predecessor,
this version stores books in a database, allowing anytime access and preserving previously saved records.


## Features

- **Add Books:** Append a new book to the library collection.
  
- **View Available Books:** Display a list of currently available books in the library.
  
- **Update Books:** Modify the details of any book in the library.
  
- **Delete Books:** Remove a book from the library.

## Project Updates

In this version, significant changes have been made to the codebase, leveraging SQLAlchemy and reducing reliance on strict typing to streamline development. However, I plan to reintroduce strong typing and annotations in future iterations.

Additionally, this version introduces:

- **:Add Many Books**
  This feature allows for the addition of multiple books at once. It offers two paths: **adding N copies of a new book** or **increasing the quantity of an existing book by N**.

- **Adding N Copies of a New Book:**
  This path checks for the book's existence in the database. If not found, it creates a new entry with N copies.

- **Increasing the Quantity of an Existing Book by N:**
  This path verifies the book's presence in the database and increments its quantity by N.

- **Implementation of Database with `PostgreSQL`:**
  This version implements database usage to persist records beyond runtime, a departure from the previous version's behavior.

However, this version omits functionalities such as:

- **Loan and Return of Books**
  These features are removed to facilitate improved implementations in future versions.

## Future Updates

I intend to continue enhancing this project, serving as a foundation for a comprehensive web application. Future iterations will include the integration of web services and a user-friendly interface to elevate user experience and showcase proficiency in full-stack development.


## Installing Dependencies

### PostgreSQL

Ensure that PostgreSQL is installed on your system. If not, you can download and install it from [here](https://www.postgresql.org/download/).

### SQLAlchemy

To use SQLAlchemy in your project, follow these steps:

#### Windows

1. Open a command prompt.
2. Ensure you have Python installed. You can download and install Python from [python.org](https://www.python.org/downloads/).
3. Install SQLAlchemy using pip by running the following command:
    ```
    pip install sqlalchemy
    ```

#### Linux

1. Open a terminal.
2. Ensure you have Python installed. Most Linux distributions come with Python pre-installed. If not, you can install it using your package manager.
3. Install SQLAlchemy using pip by running the following command:
    ```
    pip install sqlalchemy
    ```

Once installed, you can import and use SQLAlchemy in this Python projects.

## Getting Started

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. 
4. update the "config_example.py" file by changing the name to "config.py".
5. update the code with your information to successfully connect with the `PostgreSQL` manager
6. Execute the Python script.
7. Follow the on-screen instructions to interact with the library management system.


## Previous Version:

[Library Management Software V1.0](https://github.com/LASM24/library_management_software_V1.0)
