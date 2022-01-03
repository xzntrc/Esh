chmod +x esh.py
mv esh.py esh
mkdir -p ~/bin
cp esh ~/bin
mv config.toml ~/bin/eshconfig.toml
echo 'export PATH=$PATH”:$HOME/bin' >> ~/.zshrc
echo 'Done!'
echo 'Your config file is located in ~/bin/eshconfig.toml'
echo 'If you experienced any install issues, check the install.sh file'

