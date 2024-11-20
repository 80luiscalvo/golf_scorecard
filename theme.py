class Theme:
    @staticmethod
    def hex_to_rgba(hex_color, alpha=1.0):
        """Convert hex color to RGBA format."""
        hex_color = hex_color.lstrip('#')
        return [int(hex_color[i:i+2], 16) / 255 for i in (0, 2, 4)] + [alpha]

    TEXT_COLOR = hex_to_rgba.__func__("#d8dcdf")  # Gris para texto
    MENU_COLOR = hex_to_rgba.__func__("#133f39")
    BACKGROUND_COLOR = hex_to_rgba.__func__("#557776")
    DATA_COLOR = hex_to_rgba.__func__("#9fb6b6")
    ICON_COLOR = hex_to_rgba.__func__("#bd8328")
