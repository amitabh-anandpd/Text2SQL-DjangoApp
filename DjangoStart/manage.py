#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def main():
    """Run administrative tasks."""
    # Ensures that the environment variable DJANGO_SETTINGS_MODULE is set
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoStart.settings')
    
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and"
            "available on your PYTHONPATH environment variable? Did you" 
            "forget to activate a virtual environment?"
        ) from exc
    
    # Run the command-line arguments (for migrations, server run, etc.)
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
