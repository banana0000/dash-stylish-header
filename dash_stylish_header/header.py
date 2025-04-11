from dash import hooks, html, dcc

# Define reusable styles
PLOTLY_COLOR = "#8582FF"

# Common styles
STYLES = {
    "header_container": {
        "background": f"linear-gradient(90deg, {PLOTLY_COLOR} 0%, #7A78E8 100%)",
        "padding": "18px 32px",  # Increased padding for larger header
        "color": "white",
        "display": "flex",
        "alignItems": "center",
        "justifyContent": "space-between",
        "boxShadow": "0 3px 12px rgba(133, 130, 255, 0.2)",
        "fontFamily": "'Inter', sans-serif",
        "borderBottom": "1px solid rgba(255, 255, 255, 0.1)",
        "height": "65px",  # 76px total height with padding
    },
    "logo": {
        "height": "36px",  # Larger logo
        "marginRight": "20px",
        "filter": "drop-shadow(0 2px 4px rgba(0, 0, 0, 0.1))",
    },
    "title": {
        "margin": 0,
        "display": "inline",
        "fontWeight": "600",
        "fontSize": "22px",  # Larger title text
        "letterSpacing": "-0.01em",
        "textShadow": "0 1px 2px rgba(0, 0, 0, 0.05)",
    },
    "flex_center": {"display": "flex", "alignItems": "center"},
    "icon": {
        "marginRight": "8px",
        "fontSize": "20px",  # Larger icon
        "display": "flex",
        "alignItems": "center",
        "justifyContent": "center",
    },
    "nav_link": {
        "color": "white",
        "textDecoration": "none",
        "display": "inline-flex",
        "alignItems": "center",
        "padding": "10px 14px",  # Larger padding for buttons
        "borderRadius": "6px",
        "transition": "all 0.2s ease",
        "fontWeight": "500",
        "fontSize": "15px",  # Larger font for buttons
        "backgroundColor": "rgba(255, 255, 255, 0.08)",
        "border": "1px solid rgba(255, 255, 255, 0.1)",
        "boxShadow": "0 1px 2px rgba(0, 0, 0, 0.05)",
        "marginRight": "0",
    },
    "content_container": {
        "marginTop": "10px",  # Increased to accommodate taller header
        "padding": "0 15px",
    },
}

# Add right margin to all but the last item
STYLES["nav_link_with_margin"] = {**STYLES["nav_link"], "marginRight": "20px"}


def generate_custom_header(title):
    return html.Div(
        [
            # Header container
            html.Div(
                className="dash-stylish-header",
                style=STYLES["header_container"],
                children=[
                    # Logo and title group
                    html.Div(
                        [
                            # Plotly logo
                            html.Img(
                                src="https://images.prismic.io/plotly-marketing-website-2/8f977c91-7b4e-4367-8228-26fbba2506e4_69e12d6a-fb65-4b6e-8423-9465a29c6028_plotly-logo-sm.png?auto=compress%2Cformat&fit=max&w=256",
                                style=STYLES["logo"],
                            ),
                            # App title
                            html.H2(title, style=STYLES["title"]),
                        ],
                        style=STYLES["flex_center"],
                    ),
                    # Navigation links with icons
                    html.Div(
                        [
                            # Documentation link
                            html.A(
                                [html.Div("📘", style=STYLES["icon"]), "Documentation"],
                                href="https://dash.plotly.com/",
                                target="_blank",
                                rel="noopener noreferrer",
                                style=STYLES["nav_link_with_margin"],
                            ),
                            # GitHub link
                            html.A(
                                [html.Div("⭐", style=STYLES["icon"]), "GitHub"],
                                href="https://github.com/plotly/dash",
                                target="_blank",
                                rel="noopener noreferrer",
                                style=STYLES["nav_link"],
                            ),
                        ],
                        style=STYLES["flex_center"],
                    ),
                ],
            )
        ]
    )


def add_header(title="Dash Application"):
    @hooks.layout(priority=1)
    def update_layout(layout):
        # Get the original layout items
        original_layout = layout if isinstance(layout, list) else [layout]

        # Create an outer container for everything
        container = html.Div(
            [
                # Stylish header
                generate_custom_header(title),
                # Container for app content with margin to prevent overlap
                html.Div(original_layout, style=STYLES["content_container"]),
            ]
        )

        return container

    hooks.stylesheet(
        [
            {
                "external_url": "https://fonts.googleapis.com/css2?family=Inter:wght@500;600&display=swap",
                "external_only": True,
            },
            {
                "external_url": "https://cdn.jsdelivr.net/npm/modern-normalize@2.0.0/modern-normalize.min.css",
                "external_only": True,
            },
        ]
    )

    return