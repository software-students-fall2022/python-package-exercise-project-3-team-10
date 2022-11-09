
![Python build & test](https://github.com/software-students-fall2022/python-package-exercise-project-3-team-10/actions/workflows/build.yaml/badge.svg)

[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=9129447&assignment_repo_type=AssignmentRepo)

# Python Package Exercise

A little exercise to create a Python package, build it, test it, distribute it, and use it. See [instructions](./instructions.md) for details.

# Teammates

* Jonason Wu (jw5911): [Github Profile](https://github.com/JonasonWu)
* Alejandro Olazabal (ajo351): [Github Profile](https://github.com/aleolazabal)
* 
* 

# Import the Project

* Link to the PyPi project: [link]()
* Link to the documentation of the functions: [Code Examples](./README.md#code-examples)
* Link to an example python program: [\_\_main\_\_.py](./src/converterpackageteam10/__main__.py)

# Contribute to this Project

* Open bash terminal
* Clone this repository
    ```
    $ git clone https://github.com/software-students-fall2022/python-package-exercise-project-3-team-10.git
    ```
* Get into the project directory
    ```
    $ cd python-package-exercise-project-3-team-10
    ```
* Install pipenv
    ```
    $ pip install pipenv
    ```
* Activate virtual enviroment
    ```
    $ pipenv shell
    ```
* Install all dependencies
    ```
    $ pipenv install -e .
    ```
* build 
    ```
    $ python -m build
    ```
    If this doesnt work try
    ```
    $ python3 -m build
    ```
* test
    ```
    $ pipenv run pytest
    ```



# Code Examples

## Age Converter

## Distance Converter

* The following line will print and give all the conversions for distances that are available:
    ```
    >> li = distance_converter.allowed_distance_conversions()
    These are the allowed unit inputs for the convert_distance method: 
    inches     --> in
    feet       --> ft
    mile       --> mi
    milimeter  --> mm
    centimeter --> cm
    meter      --> m
    kilometer  --> km
    >> print(li)
    ['mm', 'm', 'mi', 'cm', 'in', 'km', 'ft']
    ```
* The following line will convert 10 feet into inches:
    ```
    >> print(distance_converter.convert_distance(10, 'ft', 'in'))
    120.0
    ```
* The following line will convert 100 centimeters into meters:
    ```
    >> print(distance_converter.convert_distance(100, 'cm', 'm'))
    1.0
    ```

## Number Converter

## Time Zone Converter