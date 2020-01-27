#!/bin/bash
PYENV="/usr/local/bin/pyenv"
if [[ -f "$PYENV" ]]; then
	echo "pyenv already installed."
else
	brew install pyenv
	brew install pyenv-virtualenv
	echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
	echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
	echo 'eval "$(pyenv init -)"' >> ~/.bashrc
	source ~/.bashrc
fi
brew install gbevin/tools/sendmidi
brew install gbevin/tools/receivemidi
brew install liblo
brew install figlet
brew install gzip
brew tap homebrew-ffmpeg/ffmpeg
brew install homebrew-ffmpeg/ffmpeg/ffmpeg --with-fdk-aac
source ~/.bashrc
pyenv versions | grep '3.7.2' &> /dev/null
if [ $? == 0 ]; then
	pyenv virtualenv 3.7.2 4bars
else
	pyenv install 3.7.2
	pyenv virtualenv 3.7.2 4bars
fi
echo "4bars">>.python-version
pip install -r requirements.txt

EXEC="/usr/local/bin/4bars"
if [[ -f "$EXEC" ]]; then
    rm /usr/local/bin/4bars
    ln -s $(pwd)/4bars.sh /usr/local/bin/4bars
	chmod +x /usr/local/bin/4bars
else
	ln -s $(pwd)/4bars.sh /usr/local/bin/4bars
	chmod +x /usr/local/bin/4bars
fi
exec "$SHELL"