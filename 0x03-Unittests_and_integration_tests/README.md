# Unit Tests and Integration Tests

This directory contains solutions and exercises for unit testing and integration testing in Python. It is part of the ALX backend programming curriculum, focusing on testing principles and best practices.

## Overview

Testing is crucial for ensuring that code functions as expected and is free from bugs. This directory demonstrates various approaches to testing in Python, including unit tests and integration tests, using frameworks such as `unittest`, `mock`, and `parameterized`.

## Structure

The directory includes the following components:

1. **Unit Testing**:
   - Implementations and tests for individual units of code.
   - Focus on testing specific functions or methods to ensure they work correctly in isolation.

2. **Integration Testing**:
   - Tests that evaluate how different components of the application work together.
   - Ensures that integrated parts of the system function correctly as a whole.

## Key Files

- **`test_github_org_client.py`**:
  - Contains tests for the `GithubOrgClient` class, focusing on methods like `public_repos` and properties like `_public_repos_url`.
  - Uses `unittest` for structuring test cases and `unittest.mock` for mocking dependencies.

- **`test_access_nested_map.py`**:
  - Contains tests for the `access_nested_map` function that navigates through nested dictionaries.
  - Demonstrates how to use `parameterized.expand` for testing different scenarios and how to handle exceptions.

- **`test_memoize.py`**:
  - Tests for the `memoize` decorator that caches function results.
  - Shows how to use `unittest.mock` to verify that caching behavior works as expected.

## Getting Started

To run the tests, make sure you have Python and the required packages installed. You can install the necessary packages using:

```bash
pip install -r requirements.txt
```
## Contributing
Contributions to this repository are welcome. If you find issues or have improvements, please submit a pull request or open an issue.

## License
This repository is licensed under the MIT License. See the LICENSE file for more details.

## Contact
For any questions or feedback, please reach out to efatariku07@gmail.com