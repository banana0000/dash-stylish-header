from dash import hooks, html, dcc

def make_styles(gradient):
    return {
        "header_container": {
            "background": gradient,
            "padding": "18px 32px",
            "color": "white",
            "color": "white",
            "display": "flex",
            "alignItems": "center",
            "justifyContent": "space-between",
            "boxShadow": "0 3px 12px rgba(133, 130, 255, 0.2)",
            "fontFamily": "'Inter', sans-serif",
            "borderBottom": "1px solid rgba(255, 255, 255, 0.1)",
            "height": "105px",
            "position": "sticky",
            "top": 0,
            "zIndex": 1000,
        },
        "logo": {
            "height": "36px",
            "marginRight": "20px",
            "filter": "drop-shadow(0 2px 4px rgba(0, 0, 0, 0.1))",
        },
        "title": {
            "margin": 0,
            "display": "inline",
            "fontWeight": "600",
            "fontSize": "22px",
            "letterSpacing": "-0.01em",
            "textShadow": "0 1px 2px rgba(0, 0, 0, 0.05)",
        },
        "flex_center": {"display": "flex", "alignItems": "center"},
        "icon": {
            "marginRight": "8px",
            "fontSize": "20px",
            "display": "flex",
            "alignItems": "center",
            "justifyContent": "center",
        },
        "nav_link": {
            "color": "white",
            "textDecoration": "none",
            "display": "inline-flex",
            "alignItems": "center",
            "padding": "10px 14px",
            "borderRadius": "6px",
            "transition": "all 0.2s ease",
            "fontWeight": "500",
            "fontSize": "15px",
            "backgroundColor": "rgba(255, 255, 255, 0.08)",
            "border": "1px solid rgba(255, 255, 255, 0.1)",
            "boxShadow": "0 1px 2px rgba(0, 0, 0, 0.05)",
            "marginRight": "0",
        },
        "nav_link_with_margin": {
            "color": "white",
            "textDecoration": "none",
            "display": "inline-flex",
            "alignItems": "center",
            "padding": "10px 14px",
            "borderRadius": "6px",
            "transition": "all 0.2s ease",
            "fontWeight": "500",
            "fontSize": "15px",
            "backgroundColor": "rgba(255, 255, 255, 0.08)",
            "border": "1px solid rgba(255, 255, 255, 0.1)",
            "boxShadow": "0 1px 2px rgba(0, 0, 0, 0.05)",
            "marginRight": "20px",
        },
        "content_container": {
            # NO marginTop or paddingTop here!
            "padding": "0 15px",
            "flex": "1 0 auto",
        },
    }

def generate_custom_header(title, styles):
    return html.Div(
        [
            html.Div(
                className="dash-stylish-header",
                style=styles["header_container"],
                children=[
                    html.Div(
                        [
                            html.Img(
                                src="https://images.prismic.io/plotly-marketing-website-2/8f977c91-7b4e-4367-8228-26fbba2506e4_69e12d6a-fb65-4b6e-8423-9465a29c6028_plotly-logo-sm.png?auto=compress%2Cformat&fit=max&w=256",
                                style=styles["logo"],
                            ),
                            html.H2(title, style=styles["title"]),
                        ],
                        style=styles["flex_center"],
                    ),
                    html.Div(
                        [
                            html.A(
                                [html.Div("📘", style=styles["icon"]), "Documentation"],
                                href="https://dash.plotly.com/",
                                target="_blank",
                                rel="noopener noreferrer",
                                style=styles["nav_link_with_margin"],
                            ),
                            html.A(
                                [html.Div("⭐", style=styles["icon"]), "GitHub"],
                                href="https://github.com/plotly/dash",
                                target="_blank",
                                rel="noopener noreferrer",
                                style=styles["nav_link"],
                            ),
                        ],
                        style=styles["flex_center"],
                    ),
                ],
            )
        ]
    )

def add_header(title="Dash Application", gradient="linear-gradient(90deg, #C529A6 0%, #7A78E8 100%)"):
    styles = make_styles(gradient)
    @hooks.layout(priority=1)
    def update_layout(layout):
        original_layout = layout if isinstance(layout, list) else [layout]
        content = html.Div(
            original_layout,
            style=styles["content_container"],
        )
        container = html.Div(
            [
                generate_custom_header(title, styles),
                content,
            ],
            style={
                "display": "flex",
                "flexDirection": "column",
                "minHeight": "100vh",
            }
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

def add_footer_hook(text="This is a footer!"):
    from dash import html, hooks
    @hooks.layout(priority=100)
    def add_footer(layout):
        children = layout.children if hasattr(layout, "children") else layout
        if isinstance(children, list) and children and isinstance(children[-1], html.Footer):
            return layout
        footer = html.Footer(
            text,
            style={
                "background": "#222",
                "color": "white",
                "padding": "12px 32px",
                "textAlign": "center",
                "fontFamily": "'Inter', sans-serif",
                "marginTop": "32px",
                "flex": "0 0 auto",
            }
        )
        if hasattr(layout, "style") and isinstance(layout.style, dict):
            style = layout.style
        else:
            style = {
                "display": "flex",
                "flexDirection": "column",
                "minHeight": "100vh",
            }
        return html.Div(
            [*children, footer],
            style=style
        )