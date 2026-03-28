"""Check the environment."""
import sys
import os


def construct() -> None:
    """Check the environment."""
    venv = sys.base_prefix != sys.prefix
    name_env = os.path.basename(sys.prefix)
    path = sys.executable

    if venv:
        print("\nMATRIX STATUS: Welcome to the construct\n")

        print(f"\nCurrent Python: {path}")
        print(f"Virtual Environment: {name_env}")
        print(f"Environment Path: {sys.prefix}")
        print("\nSUCCESS: You’re in an isolated environment!\n"
              "Safe to install packages without affecting\n"
              "the global system.\n")

    else:
        print("\nMATRIX STATUS: You’re still plugged in\n")

        print(f"Current Python: {path}")
        print("Virtual Environment: None detected")

        print("\nWARNING: You’re in the global environment!\n"
              "The machines can see everything you install.")

        print("\nTo enter the construct, run:\n"
              "python -m venv matrix_env\n"
              "source matrix_env/bin/activate # on Unix\n"
              "matrix_env\n"
              "Scripts\n"
              "activate # On Windows\n")
    print("\n", path)


if __name__ == "__main__":
    construct()
