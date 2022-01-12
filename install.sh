chmod +x esh.py
mv esh.py esh
mkdir -p $HOME/.config/esh
echo "sudo required to move ESH to '/bin/esh':"
sudo cp esh /bin/esh
mv config.toml $HOME/.config/esh/eshconfig.toml
echo "if you recieve an error, ensure you have 'python-pip' installed:"
pip install -r requirements.txt
echo "Sudo required to add ESH to '/etc/shells'"
sudo echo "\n /bin/esh" >> /etc/shells
echo "Done."
echo "You can now delete this repository."
echo "Run 'esh' in a terminal to start!"
