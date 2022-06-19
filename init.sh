python manage.py makemigrations
python manage.py migrate
python manage.py create_genres
python manage.py grab_trending
python manage.py seed_users --number 200

echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_user('이남곤', '', '123')" | python manage.py shell

python manage.py seed_reviews --number 2000

echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', '', '123')" | python manage.py shell

python manage.py runserver
