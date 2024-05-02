# create virtual env
python -m venv env
# activate env
source ./env/bin/activate
# install requirements
pip install --upgrade pip
pip install -r requirements.txt
# Download spaCy model
python -m spacy download en_core_web_md
# close the environment
deactivate
