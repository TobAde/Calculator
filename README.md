## Calculator 

### Table of contents
* [Introduction](#Introduction)
* [Installation](#Installation)
* [Usage](#Usage)
* [Technologies used](#technologies-used)
* [License](#License)

### Introduction
This is a python package hosted on PYPI and can be used to perform basic mathematical functions such as;
* Addition
* Subtraction
* Division
* Multiplication
* Modulus
* N-th root
* Exponent

It is an open source project with a public repository at https://github.com/TobAde/Calculator.



### Installation

pypi_calculator requires python3 and can be installed via PYPI
``` shell
$ pip install calculator-tobade==0.0.1
```

``` shell
$ pip install git+https://github.com/TobAde/Calculator.git
```

### Usage
The calculator can be used for basic mathematical computation. The calculator has a memory that can reset itself to 0 and also stores previous values, except the memory is reset


Sample Code
```python
from calculator import Calculator

cal = Calculator()
#intial calculator memory is zero
```

#### Addition
```python
cal.add(7)

#returns 7
```

#### Subtraction
```python
cal.subtract(3)

#returns 4
#because the memory was not reset, 2 was subtracted from previous value 7
```

#### Division
```python
cal.divide(2)

#returns 2
```

#### Memory
```python
cal.memory_value()

#returns 2
```

#### Reset Memory
```python
cal = cal.reset_memory()
cal.memory_value()
#returns 0
```

### Technologies used
* Python version: 3.8
* Pytest version: 6.2.4 

### License

MIT

**It is a Free Software** 
