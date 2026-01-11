#!/usr/bin/env python3
"""Create a new trace entry based on template."""

import os
from datetime import datetime
from pathlib import Path


def create_new_trace():
    """Create a new trace entry for today's date."""
    # Get today's date
    today = datetime.now().strftime("%Y-%m-%d")

    # Define paths
    template_path = Path("_traces/template.md")
    entry_dir = Path(f"_traces/{today}")
    entry_file = entry_dir / "index.md"

    # Check if entry already exists
    if entry_file.exists():
        print(f"Error: Entry for {today} already exists at {entry_file}")
        return

    # Read template
    if not template_path.exists():
        print(f"Error: Template not found at {template_path}")
        return

    template_content = template_path.read_text()

    # Replace placeholders
    new_content = template_content.replace("YYYY-MM-DD", today)

    # Create directory
    entry_dir.mkdir(parents=True, exist_ok=True)

    # Write new entry
    entry_file.write_text(new_content)

    print(f"✓ Created new trace entry at {entry_file}")
    print(f"  Date: {today}")
    print(f"\nNext steps:")
    print(f"  1. Edit {entry_file}")
    print(f"  2. Add drive_file_id and drive_image_id (or use local files)")
    print(f"  3. (Optional) Add image to /assets/traces/{today}/")


if __name__ == "__main__":
    create_new_trace()
