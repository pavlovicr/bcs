Django instalacija koplet na RPI s static IP 89.212.90.184
=========================================================


OSNOVNO
^^^^^^^^^^

za štart
::
	Sl.tipkovnica ....sudo dpkg-reconfigure keyboard-configuration
	SSH server .......sudo apt install openssh-server
	Miška ............sudo apt-get install gp
	Vim...............sudo apt-get install vim
	Git ..............sudo apt-get install git



Python3, Pip in Virtualenv
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Prvi  korak je instalacija Pythona3 in Pip in virtualnega okolja
V ubuntu16.04 je python3 že instaliran sicer pa download iz https://www.python.org/downloads/python3.6.3 .Iz download direktorija Python-3.6.3 izvršimo ukaze
::
	./configure
	sudo make
	sudo make install
Instalacija Pip
::
	sudo apt-get install python3-pip
	sudo python3.5 –m pip install –upgrade pip setuptools wheel
Virtualno okolje z mojim "local" za development
::
	sudo pip3 install virtualenv
	sudo pip3 install https://github.com/pypa/virtualenv/tarball/master
	virtualenv -p python3 local

COOKIECUTTER S PREDNASTAVLJENIM DJANGOM
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Prvi korak za prvo instalacijo :
Na osnovnem direktoriju /home/pavlovicr naložimo cookiecutter, odpremo virtualno okolje in inštaliramo nov projekt z django aplikacijo
::
	source local/bin/activate
	pip install --upgrade cookiecutter
	cookiecutter https://github.com/pydanny/cookiecutter-django
Prvi korak, za kopijo aplikacije, ki jo imamo na gitHubu. To uporabimo vedno ko je projekt živ sicer bomo imeli težave z različnimi inštaliranimi aplikacijami
::

	git clone https://github.com/pavlovicr/bcs

Drugi korak:
Inštaliramo še vse potrebne programe za naš operacijski sistem in python, ki smo jih naložili z instalacijo cookiecutter-django in so v direktoriju "utility"
::
	cd utility
	sudo ./install_os_dependencies.sh install
	sudo ./install_python_dependencies.sh install

Pri zadnji komandi nas opozori naj si le te pridobimo iz naslova
::

	wget https://bootstrap.pypa.io/get-pip.py --output-document=get-pip.py; chmod +x get-pip.py; sudo -H python3 get-pip.py


Sedaj , ko imamo inštalirano vso potrebno programsko opremo za os in python zaženemo še potrebno programsko opremo za django za local development okolje
::
	cd bcs
	pip install -r requirements/local.txt

POSTGRES
^^^^^^^^

v serverju postgres ustvarimo bazo
::
	sudo su -l postgres
	createdb bcs
in nastavimo novega uporabnika "ubuntu"
::
	CREATE USER ubuntu WITH PASSWORD 'rolu9255';

DJANGO
^^^^^^
::

    python manage.py runserver 89.212.90.184:8000
    python manage.py migrate


READTHEDOCS
^^^^^^^^^^^
::
za lepo html obliko navodil ali tudi modelsov in ostalega
v index.rst vpišemo ime fajla "bcs_instalacija.rst"
