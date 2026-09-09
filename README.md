# AirBnB Clone

## Description

The **AirBnB Clone** project is a command-line application that is part of the Holberton School/ALX Software Engineering curriculum.

The goal of this project is to build a simplified version of the AirBnB application using Python. The project focuses on creating a command interpreter that allows users to create, retrieve, update, and delete objects through a command-line interface.

The project also introduces important concepts such as:

* Python packages
* Object-Oriented Programming
* Classes and inheritance
* Serialization and deserialization
* JSON
* File storage
* Unit testing
* Command-line interfaces
* `datetime`
* `*args` and `**kwargs`

## Command Interpreter

The command interpreter is the main entry point of the application. It allows users to interact with the AirBnB Clone through commands entered in a terminal.

The interpreter is implemented in `console.py`.

### How to Start the Command Interpreter

Clone the repository and move into the project directory:

```bash
git clone https://github.com/derytech/AirBnB_clone.git
cd AirBnB_clone
```

Start the console in interactive mode:

```bash
./console.py
```

You can also start it using Python:

```bash
python3 console.py
```

When the console starts successfully, you will see:

```text
(hbnb)
```

### How to Use the Command Interpreter

After starting the console, enter a command followed by any required arguments.

For example:

```text
(hbnb) help
(hbnb) create BaseModel
(hbnb) show BaseModel <id>
(hbnb) all BaseModel
(hbnb) update BaseModel <id> name "My first model"
(hbnb) destroy BaseModel <id>
(hbnb) quit
```

To exit the console, use:

```text
(hbnb) quit
```

You can also press `Ctrl+D` to exit.

## Commands

### `help`

Displays available commands or information about a specific command.

```text
(hbnb) help
(hbnb) help create
```

### `create`

Creates a new instance of a class and prints its ID.

```text
(hbnb) create BaseModel
```

Example output:

```text
49faff9e-6318-4a63-97d7-e1e6f1d1a1d1
```

### `show`

Displays the string representation of an instance based on its class and ID.

```text
(hbnb) show BaseModel 49faff9e-6318-4a63-97d7-e1e6f1d1a1d1
```

### `all`

Displays all instances, or all instances of a particular class.

```text
(hbnb) all
(hbnb) all BaseModel
```

### `update`

Updates an instance with a new attribute value.

```text
(hbnb) update BaseModel 49faff9e-6318-4a63-97d7-e1e6f1d1a1d1 name "John"
```

### `destroy`

Deletes an instance based on its class and ID.

```text
(hbnb) destroy BaseModel 49faff9e-6318-4a63-97d7-e1e6f1d1a1d1
```

### `quit`

Exits the command interpreter.

```text
(hbnb) quit
```

## Non-Interactive Mode

Commands can also be passed to the console using a pipe.

For example:

```bash
echo "create BaseModel" | ./console.py
```

Another example:

```bash
echo "all BaseModel" | ./console.py
```

## Examples

### Creating an object

```text
$ ./console.py
(hbnb) create BaseModel
49faff9e-6318-4a63-97d7-e1e6f1d1a1d1
(hbnb) quit
$
```

### Showing an object

```text
$ ./console.py
(hbnb) show BaseModel 49faff9e-6318-4a63-97d7-e1e6f1d1a1d1
[BaseModel] (49faff9e-6318-4a63-97d7-e1e6f1d1a1d1) {'id': '49faff9e-6318-4a63-97d7-e1e6f1d1a1d1', 'created_at': '...'}
(hbnb) quit
$
```

### Updating an object

```text
$ ./console.py
(hbnb) create BaseModel
49faff9e-6318-4a63-97d7-e1e6f1d1a1d1
(hbnb) update BaseModel 49faff9e-6318-4a63-97d7-e1e6f1d1a1d1 name "AirBnB"
(hbnb) show BaseModel 49faff9e-6318-4a63-97d7-e1e6f1d1a1d1
(hbnb) quit
$
```

## Project Structure

```text
AirBnB_clone/
├── AUTHORS
├── README.md
├── console.py
├── models/
│   ├── __init__.py
│   ├── base_model.py
│   ├── engine/
│   │   └── file_storage.py
│   └── ...
├── tests/
│   └── ...
└── ...
```

## Authors

This project was developed as part of the ALX Software Engineering curriculum.

See the `AUTHORS` file for the contributors to this repository.

## License

This project is for educational purposes.