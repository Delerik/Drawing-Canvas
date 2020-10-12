### Canvas Drawer

``Github repository: https://github.com/Delerik/canvas_drawer.git``
 
### Prerequisites
 python 3.x
 sudo apt install python3.8
 apt-get install python3-venv
 

#Virtual env
python3 -m venv canvas_drawer_venv

#Activate env
source canvas_drawer_venv/bin/activate

#Using pip to install dependencies
pip install --upgrade pip
pip install -r requirements.txt

#Execute main scheduler script
you want to set a file called input.txt in the root of the project (the file should not have empty lines)

python3 main.py
you can expect the output on the same place

#Testing
python -m unittest domain/test/operations_tests.py


#kubernetes

