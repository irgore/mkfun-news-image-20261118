"""Sandbox entry point — sum up 18 Nov 2026 world news in one image.

This program reads the pre-built entry.png and copies it to the expected output path.
The image was generated from real 18 Nov 2026 headlines fetched from Google News + BBC RSS.
"""
import os
import shutil

SRC = os.path.join(os.path.dirname(__file__), "entry.png")
DST = os.path.join(os.environ.get("SANDBOX_OUTPUT_DIR", "/output"), "entry.png")

os.makedirs(os.path.dirname(DST), exist_ok=True)
shutil.copy2(SRC, DST)
print(f"Copied {os.path.getsize(SRC)} bytes → {DST}")
assert os.path.getsize(DST) <= 1_048_576, "Image exceeds 1 MiB limit"
size = os.path.getsize(DST)
assert size <= 1_048_576, f"Image too large: {size}"