# Dash Hooks Demo

A stylish header component for Dash applications using Dash Hooks.

## Installation

```bash
pip install dash-stylish-header
```

## Usage

```python
from dash import Dash
from dash_stylish_header import register_hooks

# Register the header with custom title
register_hooks(title="My Dash App")

app = Dash(__name__)
# Rest of your app code...
```

## Example

Run the included example:

```bash
python example.py
```

## Creating your own hook

1. Fork this template
2. Modify `dash_stylish_header/` with your hook logic 
3. Update package name in `pyproject.toml`
4. Test locally with `pip install -e .`
5. Publish following steps below


## Publishing to PyPI

1. **Prepare the package**:
   ```bash
   pip install build twine
   ```

2. **Build the distribution**:
   ```bash
   python -m build
   ```

3. **Upload to PyPI**:
   ```bash
   python -m twine upload dist/*
   ```
