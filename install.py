print "Start install.py"
import subprocess

def cmd(cmd):
    subprocess.call( cmd, shell=True  )
pyenv_install_dir = "/home/vagrant/work/pyenv"
env_setting_file = "/home/vagrant/work/.bashrc"
#py_version = "2.7.11"
py_version = "2.7.11"
def main():
    #installing packages
    pkgs =['nano','git','curl','openssl-devel','make','gcc','gcc-c++','zlib-devel','curl-devel','nginx','patch','readline-devel','sqlite-devel','libxml2-devel','libxslt-devel','bzip2-devel','python-devel','libsemanage-python','libselinux-python','gdbm','gdbm-devel']
    for pkg in pkgs:
        cmd("sudo yum install %s" % pkg)

    cmd("sudo mv /home/vagrant/.bashrc /home/vagrant/.bashrc.bk")

    cmd("sudo cp /home/vagrant/work/.bashrc /home/vagrant/.bashrc")

    cmd("source /home/vagrant/.bashrc")

    #pip install
    cmd("sudo curl -kL https://bootstrap.pypa.io/get-pip.py | python")

    cmd("sudo chown vagrant:vagrant %s" % pyenv_install_dir)

    cmd("/home/vagrant/work/pyenv/bin/pyenv install %s" % py_version)
    cmd("/home/vagrant/work/pyenv/bin/pyenv global %s" % py_version)

if __name__ == '__main__':
    main()
