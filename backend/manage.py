#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import dotenv

from pathlib import Path

def main():
    """Run administrative tasks."""

    # read .env
    BASE_DIR = Path(__file__).resolve().parent
    env_file = os.path.join(BASE_DIR,".env")

    if os.path.exists(env_file):
        dotenv.read_dotenv(env_file)

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

