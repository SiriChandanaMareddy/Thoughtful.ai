# Thoughtful.ai
Package_Sorting
# Package Sorting Algorithm

This repository contains a Python function to classify packages based on their dimensions and weight.

## How It Works
The function sorts packages into three categories:
- **STANDARD**: Neither bulky nor heavy.
- **SPECIAL**: Either bulky or heavy.
- **REJECTED**: Both bulky and heavy.

## Getting Started
### Prerequisites
Ensure you have Python installed (Python 3.x recommended).

### Running the Code
```sh
python sort_packages.py

**Running Tests**
python -c "import sort_packages; sort_packages.test_sort()"





This Python script determines how to categorize packages based on their dimensions and mass using predefined rules.

**Sorting Criteria:**
A package is bulky if:
Its volume (Width × Height × Length) ≥ 1,000,000 cm³ OR
Any one of its dimensions (Width, Height, Length) ≥ 150 cm
A package is heavy if its mass ≥ 20 kg
Packages are sorted into three categories:
STANDARD → Neither bulky nor heavy 
SPECIAL → Either bulky or heavy 
REJECTED → Both bulky and heavy 

