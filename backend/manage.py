#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from pathlib import Path

import dotenv


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    # read .env
    BASE_DIR = Path(__file__).resolve().parent
    env_file = os.path.join(BASE_DIR, ".env")

    if os.path.exists(env_file):
        dotenv.read_dotenv(env_file)

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")


if __name__ == "__main__":
    main()
