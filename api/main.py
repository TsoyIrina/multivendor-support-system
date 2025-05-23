# import os
#
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api.settings")
#
# from django.core.management import call_command
# from django.core.wsgi import get_wsgi_application
# application = get_wsgi_application()
# call_command('runserver',  '127.0.0.1:8000', '--noreload')

# !/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(['manage.py', 'runserver', '8000', '--noreload'])


if __name__ == '__main__':
    main()
