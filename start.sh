echo "=================================================================="
echo Initializing bash script...
location=$(which bash)
#! $location
echo Installing packages from requirements.txt...
packages=$`pip install -r requirements.txt`
echo Configuring Django...
make_migrations=$`python manage.py makemigrations`
echo Migrations prepared...
migrate=$`python manage.py migrate`
echo Migrations done...
flush=$`python manage.py flush --no-input`
#echo Collecting staticfiles...
#static=$`python manage.py collectstatic --no-input`
dirs=("people" "planets" "films" "species" "vehicles" "starships")
for dir in "${dirs[@]}"
do
  make_dir=$`mkdir -p staticfiles/csv/"$dir"`
done
echo Unit tests take 5 seconds. Full program test takes 2 minutes.
read -p 'Do you want to run full test [yes/NO]: ' command
command=${command:-NO}
if [ $command == 'yes' ]
then
  echo Running full tests...
  test=$`pytest > log.txt`
else
  echo Running unit tests only...
  test=$`pytest -m "not full" > log.txt`
fi
echo "-----------------------------------------------------------------"
echo All the information saved to log.txt
echo "-----------------------------------------------------------------"
echo Open your browser and visit this address: http://127.0.0.1:8000/
run=$`python manage.py runserver`
echo "=================================================================="
