FROM python:3.12    

#DJANGO
# RUN python -m venv ./venv
# WORKDIR /django
# COPY ./referencial/django-produtos/ .
# RUN /venv/bin/pip install -r requirements.txt
# RUN /venv/bin/python manage.py makemigrations
# RUN /venv/bin/python manage.py migrate
# CMD ["/venv/bin/python", "manage.py", "runserver", "0.0.0.0:8000"]

ENTRYPOINT ["tail", "-f", "/dev/null"]