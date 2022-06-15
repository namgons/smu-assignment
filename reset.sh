sudo rm db.sqlite3
sudo rm -rf users/migrations/
sudo rm -rf reviews/migrations/
sudo rm -rf contents/migrations/

mkdir users/migrations/
mkdir reviews/migrations/
mkdir contents/migrations/

touch ./users/migrations/__init__.py
touch ./reviews/migrations/__init__.py
touch ./contents/migrations/__init__.py