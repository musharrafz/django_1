run_migrate:
	./manage.py makemigrations
	./manage.py migrate
	./manage.py runserver