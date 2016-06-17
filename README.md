Projeto Integrador 2 - LabArm

Integrantes:

Bárbara Caetano - Energia
Brenda Tinoco - Energia
Caio Rodrigo - Eletrônica
Cristiano Costa - Software
Fágner Rodrigues - Software
Luciano Henrique - Software
Luiz Eduardo - Eletrônica
Marcos Diego - Software
Maria Aparecida - Energia
Pedro Guilherme - Eletrônica
Tahigo Alves - Energia
Údine Rodrigues - Automotiva


Instalação e execução do projeto

Primeiro instale o python-dev:

sudo apt-get install python-dev
sudo apt-get autoremove
sudo apt-get update

Instale o setuptools:

sudo apt-get install python-setuptools

Instale o virtualenv:

sudo apt-get install python-virtualenv

Instale o pip:

sudo easy_install pip

Com o pip instalado, instale o wrapper:

pip install virtualenvwrapper

Atualize o pip:

pip install --upgrade pip

Abra o bash com editor de sua escolha (abrimos com gedit):

gedit ~/.bashrc

Inclua a seguinte linha no final do arquivo e salve:

export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/Devel
source /home/fagner/.local/bin/virtualenvwrapper.sh

Execute os comandos:

source ~/.bashrc
sudo updatedb
locate virtualenvwrapper.sh

Crie o ambiente, nesse caso o nome do ambiente é pi2:

mkvirtualenv -p /usr/bin/python3 pi2

Execute o comando:

ls ~/.virtualenvs/

Instale as seguintes dependências:

sudo apt-get install mercurial python3-dev python3-numpy libav-tools     libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsmpeg-dev     libsdl1.2-dev  libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev libfreetype6-dev

Acesse o ambiente criado:

workon pi2

Com o pip instale o pygame:

pip install hg+http://bitbucket.org/pygame/pygame

Clone o projeto, entre na pasta do projeto clonado e ative seu ambiente:

git clone https://github.com/Lab-Arms/LabArm-client.git
cd LabArm-client

Execute o projeto:

./test_server.py

Entre em outro terminal, entre na pasta do projeto, ative o ambiente da mesma forma e execute:

./main.py

Assim já pode trabalhar com o projeto

Para sair do ambiente execute no terminal:

deactivate
