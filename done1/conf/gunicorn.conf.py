# gunicorn.conf.py
# import os

# workers = int(os.environ.get("GUNICORN_WORKERS", 3))
# worker_class = 'sync'
# bind = f"0.0.0.0:{os.environ.get('PORT', 8000)}"


command='/home/muteule/Coding/Py_enjoy/Learn_django/Learn_django/bin/gunicorn'
pythonpath='/home/muteule/Coding/Py_enjoy/Learn_django/Learn_django/bin/python'
bind='10.10.12.146'
workers=3