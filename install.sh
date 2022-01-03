chmod +x esh.py
mv esh.py esh
mkdir -p ~/bin
cp esh ~/bin
touch ~/.profile
echo 'export PATH=$PATH”:$HOME/bin' >> ~/.profile
