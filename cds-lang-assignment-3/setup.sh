#!/usr/bin/env bash
#!/usr/bin/bash

# create virtual env
python -m venv env
# activate env
source ./env/bin/activate
# install requirements
pip install --upgrade pip


#does the pip install pipreqs and pipreqs src —savepath requirements.txt go here???


#python3 -m pip install -r requirements.txt 
pip install -r requirements.txt
# close the environment
deactivate
