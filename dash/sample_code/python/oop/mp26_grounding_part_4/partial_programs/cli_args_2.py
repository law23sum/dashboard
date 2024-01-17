import sys
from pathlib import Path


def parse_cli_args():
    try:
        path = Path(sys.argv[1])
    except IndexError:
        print("You must provide a target image.")
        sys.exit()

    border_width = int(sys.argv[2]) if len(sys.argv) > 2 else 2
    padding = int(sys.argv[3]) if len(sys.argv) > 3 else 0
    border_color = sys.argv[4] if len(sys.argv) > 4 else "lightgray"

    return path, border_width, padding, border_color
