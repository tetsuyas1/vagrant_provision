# vagrantのみで開発環境を立てる

## インストールしたいもの

- pyenv
  - https://github.com/yyuu/pyenv-installer

- pyenv
  - pyenv install anaconda2-2.5.0
  - pyenv global anaconda2-2.5.0


## 作業手順
### 前提
- VirtualBox, vagrantが利用できること
- ログイン時に反映したい環境変数等は.bashrcに書き込んでおくこと

### 手順
1. 手順１ 利用するcentos-6.7 vagrant box のインストール
```
vagrant box add bento/centos-6.7
```
1. 手順２ 仮想環境起動
```
vagrant up
```
1. 手順３ 各種アプリケーションなどのインストール
```
vagrant provision
```
1. 手順４ 仮想環境にログイン
```
vagrant ssh
```
1. anaconda2-2.5.0 のインストール
(以下ログイン後に)
```
pyenv install anaconda2-2.5.0
pyenv global anaconda2-2.5.0
source ~/.bashrc
```
