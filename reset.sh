sudo rm db.sqlite3
sudo rm -rf users/migrations/
sudo rm -rf reviews/migrations/
sudo rm -rf contents/migrations/
sudo rm -rf genres/migrations/

mkdir users/migrations/
mkdir reviews/migrations/
mkdir contents/migrations/
mkdir genres/migrations/

touch ./users/migrations/__init__.py
touch ./reviews/migrations/__init__.py
touch ./contents/migrations/__init__.py
touch ./genres/migrations/__init__.py