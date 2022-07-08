# Aznavour

    Python version >= 3.10
    1 Make venv python3 -m venv /var/envs/aznavour_venv
    
    # Activate ENV
    2 source /var/envs/aznavour_venv/bin/activate

    # Install requirements
    3 pip install -r requirements.txt
    
    4 Make sure you have created .env file from .env.example populating all the required variables
    
    # Run all necessary migrations
    5 python manage.py migrate
    
    # This will create all the languages in db
    6 python manage.py seed_languages