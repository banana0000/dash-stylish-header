from .header import add_header

__version__ = "0.0.1"


# Function to explicitly register hooks
def setup_hooks(title="Dash Application"):
    """Explicitly register all hooks from this package.

    Args:
        title: Custom title for the header component

    This function makes the hooks registration explicit in the app.py file.
    """
    add_header(title)
