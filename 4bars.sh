#!/bin/bash +x
# to activate: ln -s $(pwd)/fourbars/4bars.sh /usr/local/bin/4bars
export PYENV_VIRTUALENV_DISABLE_PROMPT=1

# python executes codes from fourbars folder, pwd location is lost
# output current bash location to a lookup file
if [ ! -d ~/.config/4bars/.cache ]; then
  mkdir -p ~/.config/4bars/.cache;
fi
echo $(pwd) > ~/.config/4bars/.cache/pwd


pushd () {
    command pushd "$@" > /dev/null
}

popd () {
    command popd "$@" > /dev/null
}


pushd $(python -c "import os; print(os.path.dirname(os.path.realpath('/usr/local/bin/4bars')))")
    eval "$(pyenv init -)"
    eval "$(pyenv virtualenv-init -)"
    pyenv activate 4bars
popd


pushd $(python -c "import os; print(os.path.dirname(os.path.realpath('/usr/local/bin/4bars')))")/fourbars
    python -u fourbars.py "$@"
    pyenv deactivate 4bars
popd
