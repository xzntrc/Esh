chmod +x esh.py
mv esh.py esh
mkdir -p $HOME/.config/esh
echo "sudo required to move ESH to '/bin/esh':"
sudo cp esh /bin/esh
mv config.toml $HOME/.config/esh/eshconfig.toml
echo "Done."
echo "You can now delete this repository."
echo "Run 'esh' in a terminal to start!"
