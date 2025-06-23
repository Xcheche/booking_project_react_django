runserver:
	python manage.py runserver
super:
	python manage.py createsuperuser
migrate:
	python manage.py migrate
migrations:
	python manage.py makemigrations
test:	
	python manage.py test
shell:
	python manage.py shell
collectstatic:
	python manage.py collectstatic --noinput
clean:
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -type d -exec rm -rf {} +

startapp:
	python manage.py startapp $(name)
	@echo "App $(name) created successfully."