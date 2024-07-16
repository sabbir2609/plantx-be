echo "BUILD START"
python3.12 -m pip install -r requirements.txt
mkdir -p staticfiles
python3.12 manage.py collectstatic
echo "BUILD END"