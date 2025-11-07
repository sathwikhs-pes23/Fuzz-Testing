# Fuzz-Testing

This repository explores fuzz testing as a security and quality assurance technique. It demonstrates how to identify potential bugs and crashes in input processing functions using Python and the Hypothesis fuzzing library. The project includes several utility functions and a corresponding test suite designed to ensure their robustness against a wide variety of inputs.

## Core Components

*   `processor.py`: Contains utility functions for string manipulation and data parsing. Each function is designed with defensive handling for unexpected or invalid inputs.
*   `test_processor.py`: Implements property-based fuzz tests using `pytest` and `hypothesis`. These tests automatically generate a wide range of data to challenge the functions in `processor.py` and ensure they do not crash.

## Features

The `processor.py` script provides the following functions:

*   `sanitize_string(data)`: Removes special characters (`!`, `@`, `#`, `$`, `%`) and trims whitespace from a string. It safely handles `None` and non-string inputs by returning an empty string.
*   `parse_int_list(csv_string)`: Parses a comma-separated string into a list of integers. It is designed to be robust, correctly handling `None` values, empty strings, and non-integer components by skipping them.
*   `reverse_words(sentence)`: Reverses each word in a given sentence. It gracefully handles `None` and non-string inputs.

## Getting Started

### Prerequisites

*   Python 3.6+

### Installation

1.  Clone the repository:
    ```sh
    git clone https://github.com/sathwikhs-pes23/Fuzz-Testing.git
    cd Fuzz-Testing
    ```

2.  Install the required libraries:
    ```sh
    pip install pytest hypothesis
    ```

### Usage

#### Running the Utility Script

You can run the `processor.py` script to interactively test the functions from your terminal.

```sh
python processor.py
```

The script will prompt you for input for each of the three functions and display the output.

#### Running the Fuzz Tests

To execute the fuzz tests and verify the robustness of the processing functions, run `pytest`. Hypothesis will generate a multitude of test cases to check for any exceptions or crashes.

```sh
pytest
