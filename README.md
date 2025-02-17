# ChromeDriver Boilerplate Project

This project provides a boilerplate structure for creating Python scripts that use ChromeDriver for web automation tasks.

## Getting Started

1. **Prerequisites:**

   - Python 3.x installed
   - ChromeDriver downloaded and placed in the `drivers/` directory.
   - Selenium library installed (see `requirements.txt`).

2. **Installation:**

   - Create a virtual environment (recommended): `python -m venv venv`
   - Activate the virtual environment:
     - Windows: `venv\Scripts\activate`
     - macOS/Linux: `source venv/bin/activate`
   - Install dependencies: `pip install -r requirements.txt`

3. **Configuration:**

   - Edit `config.ini` to set the path to your ChromeDriver executable and other configurations.

4. **Create your tasks:**

   - Create new Python scripts in the `scripts/` directory, inheriting from `scripts/base_script.BaseScript`.
   - Implement your automation logic in the `run_task()` method.

5. **Run your tasks:**
   - From the project root, run: `python scripts/your_task_script.py`

## Project Structure

- `config.ini`: Configuration file for ChromeDriver path and other settings.
- `drivers/`: Directory to store ChromeDriver executable.
- `logs/`: (Optional) Directory for log files.
- `scripts/`: Directory for your automation scripts.
  - `base_script.py`: Base class with setup and common functions.
  - `example_task.py`: Example task script.
- `README.md`: Project documentation.
- `requirements.txt`: Python dependencies.

## Example Usage

See `scripts/example_task.py` for an example of how to create a task script.
`python scripts/example_task.py`
