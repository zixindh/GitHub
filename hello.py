#!/usr/bin/env python3
"""
Simple Python script to demonstrate GitHub integration
"""

def main():
    print("Hello from GitHub!")
    print("This is a test repository created with Cursor AI")

    # Get user input
    name = input("What's your name? ")
    print(f"Nice to meet you, {name}!")

    # Show current directory
    import os
    print(f"Current directory: {os.getcwd()}")

if __name__ == "__main__":
    main()
