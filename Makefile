ifeq ($(OS),Windows_NT)
	ACTIVATE = venv\Scripts\activate
else
	ACTIVATE = source venv/bin/activate
endif

.PHONY: venv install migrate createsuperuser run

venv:
	python -m venv venv

install: venv
	$(ACTIVATE) && python -m pip install --upgrade pip && pip install -r requirements.txt

migrate:
	$(ACTIVATE) && python manage.py migrate

createsuperuser:
	-$(ACTIVATE) && python manage.py createsuperuser --noinput --username=superuser --email=superuser@example.com || exit 0
	$(ACTIVATE) && python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); u=User.objects.filter(username='superuser').first(); u.set_password('12345678'); u.save()"

run:
	$(ACTIVATE) && python manage.py runserver

lint:
	$(ACTIVATE) && pylint manage.py config shortener
