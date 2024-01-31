#!/usr/bin/env bash

if ! [ -d ~/.local/share/colcipher/ ]; then
  mkdir ~/.local/share/colcipher/
fi

cp ./colcipher.py ~/.local/share/colcipher/colcipher.py
chmod 744 ~/.local/share/colcipher/colcipher.py

cp ./install_files/colcipher ~/.local/bin/colcipher
chmod 744 ~/.local/bin/colcipher

cp ./install_files/uninstall.sh ~/.local/share/colcipher/uninstall.sh
chmod 744 ~/.local/share/colcipher/uninstall.sh;

