from .header import add_header, add_footer_hook

__version__ = "0.0.1"

def setup_hooks(title="Dash Application", footer_text=None):
    """Explicitly register all hooks from this package.

    Args:
        title: Custom title for the header component
        footer_text: Optional text for the footer
    """
    add_header(title)
    if footer_text:
        add_footer_hook(footer_text)
