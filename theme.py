class Theme:
    @staticmethod
    def hex_to_rgba(hex_color, alpha=1.0):
        """Convert a hex color string to RGBA format."""
        hex_color = hex_color.lstrip('#')
        return [int(hex_color[i:i + 2], 16) / 255 for i in (0, 2, 4)] + [alpha]

    # Define the colors using the static method
    TEXT_COLOR = hex_to_rgba("#d8dcdf")          # Light gray for text
    MENU_COLOR = hex_to_rgba("#133f39")          # Deep green for menus
    BACKGROUND_COLOR = hex_to_rgba("#557776")    # Muted teal for background
    DATA_COLOR = hex_to_rgba("#9fb6b6")          # Soft blue-green for data
    ICON_COLOR = hex_to_rgba("#bd8328")          # Golden brown for icons

    # Add button-specific colors
    BUTTON_COLOR_PRIMARY = hex_to_rgba("#347aeb")  # Modern blue for primary action
    BUTTON_COLOR_WARNING = hex_to_rgba("#eb4034")  # Red for warnings or resets
    TEXT_COLOR_CONTRAST = hex_to_rgba("#ffffff")   # White for contrast
