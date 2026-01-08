from rich.console import Console

console = Console()

# Map specific characters to Rich color names
color_map = {
    'y': 'yellow',
    'w': 'white',
    'g': 'green',
    'b': 'blue',
    'r': 'red',
    'o': 'orange1',  # Rich supports 'orange1' for bright orange
}

def rich_format_colors(text: str) -> str:
    """Wrap specific letters in Rich color markup."""
    result = []
    for char in text:
        lower = char.lower()
        if lower in color_map:
            color = color_map[lower]
            result.append(f"[{color}]{char}[/{color}]")
        else:
            result.append(char)
    return ''.join(result)

def rich_print_colored(text: str):
    """Print text with Rich color formatting."""
    formatted_text = rich_format_colors(text)
    console.print(formatted_text)
