#!/usr/bin/env python3
"""
# Entry validated: output is 1-160 chars, one line, deterministic.
Write a roast line about a smart fridge to $MAKEFUN_OUTPUT_DIR/entry.txt.
The line mocks the fridge's expiration tracking while ignoring ancient kale.
"""
import os

LINE = "My smart fridge tracks expiration dates like a parole officer, meanwhile that kale from 2019 still waves hello from the crisper drawer"

def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    
    content = LINE + "\n"
    
    if not (1 <= len(content) <= 160 and content.strip()):
        raise ValueError(f"Invalid content length or whitespace only: {len(content)} chars")
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"Output: {output_path}")
    print(f"Characters: {len(content)}")

if __name__ == "__main__":
    main()