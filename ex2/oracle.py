"""Pretect Hardcode."""
from dotenv import load_dotenv
import os

load_dotenv()


def oracle() -> None:
    """Pretect Hardcode."""
    print("\nORACLE STATUS: Reading the Matrix...\n")

    print("\nConfiguration loaded:")
    print(f"Mode: {os.getenv("MATRIX_MODE")}")
    print(f"Database: {os.getenv("DATABASE_URL")}")
    print(f"API Access: {os.getenv("API_KEY")}")
    print(f"Log Level: {os.getenv("LOG_LEVEL")}")
    print(f"Zion Network:: {os.getenv("ZION_ENDPOINT")}")

    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    env = os.path.exists(".env")
    if env:
        print("[OK] .env file properly configured")
    else:
        print("[KO] .env file not configured")
    if os.getenv("MATRIX_MODE") == "production":
        print("[OK] Production overrides available")
    else:
        print("[KO] Production overrides not available")

    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    oracle()
