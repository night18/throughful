# Package Sorting Function

## Overview
This repository contains a Python function `sort(width, height, length, mass)` that categorizes packages into different stacks based on their dimensions and mass. The sorting is performed using specific criteria to determine whether a package is **STANDARD**, **SPECIAL**, or **REJECTED**.

## Sorting Criteria
1. A package is **bulky** if:
   - Its volume (`Width × Height × Length`) is greater than or equal to **1,000,000 cm³**, or
   - Any of its dimensions (Width, Height, or Length) is **greater than or equal to 150 cm**.

2. A package is **heavy** if its mass is **greater than or equal to 20 kg**.

3. The package will be sorted into one of the following categories:
   - **STANDARD**: The package is neither bulky nor heavy.
   - **SPECIAL**: The package is either bulky or heavy.
   - **REJECTED**: The package is both bulky and heavy.

## Implementation
The function follows these steps:
1. Compute the package volume.
2. Check whether the package meets the bulky or heavy criteria.
3. Return the appropriate category based on the sorting rules.

## Dependencies
- Python 3.x

## License
This project is licensed under the MIT License.