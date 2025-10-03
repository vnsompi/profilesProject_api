#!/usr/bin/env bash

set -e

# TODO: Set to URL of git repo.
PROJECT_GIT_URL='https://github.com/vnsompi/profilesProject_api.git'

PROJECT_BASE_PATH='/usr/local/apps'
VIRTUALENV_BASE_PATH='/usr/local/virtualenvs'

# Set Ubuntu Language
locale-gen en_GB.UTF-8

echo "🔧 Installing dependencies..."
apt-get update

# Installer Python 3.12 + outils
apt-get install -y python3.12 python3.12-venv python3.12-dev sqlite3 \
                   python3-pip supervisor nginx git

# Vérifier que python3 pointe bien sur 3.12
update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.12 2
update-alternatives --set python3 /usr/bin/python3.12

# Cloner le projet
mkdir -p $PROJECT_BASE_PATH
if [ ! -d "$PROJECT_BASE_PATH/profiles-rest-api" ]; then
    git clone $PROJECT_GIT_URL $PROJECT_BASE_PATH/profiles-rest-api
else
    echo "Repo already cloned, pulling latest changes..."
    cd $PROJECT_BASE_PATH/profiles-rest-api
    git pull
fi

# Créer l'environnement virtuel
mkdir -p $VIRTUALENV_BASE_PATH
python3 -m venv $VIRTUALENV_BASE_PATH/profiles_api

# Installer requirements
$VIRTUALENV_BASE_PATH/profiles_api/bin/pip install --upgrade pip
$VIRTUALENV_BASE_PATH/profiles_api/bin/pip install -r $PROJECT_BASE_PATH/profiles-rest-api/requirements.txt

# Lancer les migrations
cd $PROJECT_BASE_PATH/profiles-rest-api/src
$VIRTUALENV_BASE_PATH/profiles_api/bin/python manage.py migrate
$VIRTUALENV_BASE_PATH/profiles_api/bin/python manage.py collectstatic --noinput

# Setup Supervisor
cp $PROJECT_BASE_PATH/profiles-rest-api/deploy/supervisor_profiles_api.conf /etc/supervisor/conf.d/profiles_api.conf
supervisorctl reread
supervisorctl update
supervisorctl restart profiles_api

# Setup Nginx
cp $PROJECT_BASE_PATH/profiles-rest-api/deploy/nginx_profiles_api.conf /etc/nginx/sites-available/profiles_api.conf
rm -f /etc/nginx/sites-enabled/default
ln -sf /etc/nginx/sites-available/profiles_api.conf /etc/nginx/sites-enabled/profiles_api.conf
systemctl restart nginx.service

echo "✅ Deployment completed successfully!"
