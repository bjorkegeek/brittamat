# Brittamat

Python code to generate shopping lists based on a number of meals to be cooked.

## Requirements

- Python 3.8+
- [uv](https://docs.astral.sh/uv/) package manager

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd brittamat
   ```

2. Install dependencies using uv:
   ```bash
   uv sync
   ```

## Usage

### Running the Application

```bash
uv run python main.py
```

### Output Files

The application generates the following output files:

- `shopping.html` - HTML shopping list with styling
- `all-ingredients.html` - Complete list of all ingredients
- `shopping.css` - CSS stylesheet for the HTML output

### Development

#### Code Formatting

Format your code using Black:
```bash
uv run black .
```

Check if code needs formatting without making changes:
```bash
uv run black --check .
```

#### Type Checking

Run type checking with mypy:
```bash
uv run mypy .
```

#### Updating Dependencies

Update all dependencies to their latest versions:
```bash
uv lock --upgrade
```

Add a new dependency:
```bash
uv add <package-name>
```

Add a development dependency:
```bash
uv add --dev <package-name>
```

Remove a dependency:
```bash
uv remove <package-name>
```

## VS Code Integration

This project includes VS Code configuration for improved development experience:

### Quick Start in VS Code
1. Open the project folder in VS Code
2. Install recommended extensions when prompted
3. Press **F5** to run the application
4. Press **Ctrl+Shift+B** (or **Cmd+Shift+B** on Mac) for quick build

### Available Tasks
Access via **Ctrl+Shift+P** → "Tasks: Run Task":
- **Run Application** - Execute the main program
- **Format Code** - Format code with Black
- **Type Check** - Run mypy type checking
- **Install Dependencies** - Install project dependencies
- **Update Dependencies** - Update to latest versions

### Debugging
- Press **F5** to start debugging with breakpoints
- Two configurations available: "Run Brittamat" and "Debug Brittamat"

### Features
- Automatic code formatting on save
- Real-time type checking
- Import organization
- Problem highlighting with clickable error navigation

## Project Structure

- `main.py` - Main application entry point
- `data.py` - Menu and ingredient data definitions
- `alg.py` - Core algorithms for shopping list generation
- `classes.py` - Data classes and type definitions
- `html5.py` - HTML output generation
- `latex.py` - LaTeX output generation
- `pyproject.toml` - Project configuration and dependencies
- `uv.lock` - Locked dependency versions
- `.vscode/` - VS Code configuration files
