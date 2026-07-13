#!/usr/bin/env python

import os
import sys
from django.core.management import execute_from_command_line


def configure_settings():
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        "coursemanager.settings"
    )


def run():
    configure_settings()
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    try:
        run()
    except ImportError:
        raise ImportError(
            "Django is not installed or the virtual environment is not activated."
        )