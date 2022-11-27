FROM python

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY . .

RUN pip install django

EXPOSE 80

CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]