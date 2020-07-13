# Thin Airfoil DVM Solver
![Travis (.com)](https://img.shields.io/travis/com/themrdjj/thin-airfoil-dvm?style=for-the-badge)
![Codecov](https://img.shields.io/codecov/c/github/themrdjj/thin-airfoil-dvm?style=for-the-badge)
![Codacy grade](https://img.shields.io/codacy/grade/d64cbaef18a9441a84d1616c07354b81?style=for-the-badge)
![GitHub Pipenv locked Python version](https://img.shields.io/github/pipenv/locked/python-version/themrdjj/thin-airfoil-dvm?style=for-the-badge)

This python program computes the flow around a thin, cambered airfoil using the discrete vortex method as presented in "Low-Speed Aerodynamics" by Katz & Plotkin. Next to the velocity distribution it can also compute the pressure distribution and lift coefficient. It was developed for a MSc course in Aerospace Engineering and is currently not under further development.

## Installation
Clone this repository, then install all dependencies with 
```
python3.8 -m pipenv install
```
This will also create a virtual environment. If you don't have pipenv yet:

```
python3.8 -m pip install pipenv
```
