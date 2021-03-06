#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    path = '/Users/jarvis/Desktop/TFS-master/ch1'
    if path not in sys.path:
        sys.path.append(path)

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.config.settings.debug")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
