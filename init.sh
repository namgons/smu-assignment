python manage.py makemigrations
python manage.py migrate
python manage.py grab_trending

echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', '', '123')" | python manage.py shell
