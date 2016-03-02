# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
        . /etc/bashrc
fi

# User specific aliases and functions
export PYENV_ROOT=/home/vagrant/work/pyenv
export PATH=$PYENV_ROOT/bin:$PATH
eval "$(pyenv init -)"
#export PYTHONPATH=/home/vagrant/work/code/power_estimates:.
export POWER_ESTIMATES_HOME=/home/vagrant/work
