#what i did to update the system and get it to work ideally
sudo apt-get update
sudo apt install python3 pip
pip3 install streamlit
# Thankfully azure has python 3.8 so we dont need to worry about what version we 
# are working with in terms of python
nano ~/.bashrc 
# Going to the bash file and adding 'export PATH="$HOME/.local/bin:$path"' and save/exit
# Restart terminal 'source~/.bachrc` then try to `streamlit` in the terminal