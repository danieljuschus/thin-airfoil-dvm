# Thin Airfoil DVM Solver
![Travis (.com)](https://img.shields.io/travis/com/themrdjj/thin-airfoil-dvm?style=for-the-badge)
![Codecov](https://img.shields.io/codecov/c/github/themrdjj/thin-airfoil-dvm?style=for-the-badge)
![Codacy grade](https://img.shields.io/codacy/grade/d64cbaef18a9441a84d1616c07354b81?style=for-the-badge)
![GitHub Pipenv locked Python version](https://img.shields.io/github/pipenv/locked/python-version/themrdjj/thin-airfoil-dvm?style=for-the-badge)

This python program computes the flow around a thin, cambered airfoil using the discrete vortex method. Next to the 
velocity distribution it can also compute the pressure distribution and lift coefficient.

## Installation
Clone this repository, then install all dependencies with 
```
python3.8 -m pipenv install
```
This will also create a virtual environment. If you don't have pipenv yet:

```
python3.8 -m pip install pipenv
```

(TODO: figure out how to enable other python versions and how to install pipenv on Windows/Ubuntu)

## Modules
(TODO: move to docs - implement Sphinx)

### vort()
Computes velocity at a point due to vortex element with given circulation.

### grid_gen()
Generates N panels on the camberline and calculates the corresponding normal vectors. Uses airfoil
coordinates as input from text file, for now.

### inf_coeff()
Computes influence coefficients.

### aeordyn()
Computes pressure distribution and lift coefficient.

### solver()
Solve matrix equation for vorticity distribution.

### thin_airfoil_dvm()
Run dvm for given airfoil.

## Directory structure

### /data/
Airfoil data files

### /docs/
Documentation

### /examples/
Usage examples

### /tests/
Unit tests

### /thin-airfoil-dvm/
Main code