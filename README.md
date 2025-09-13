1. Run `sudo apt update` on a new VM. 
2. Set up git credentials and create an SSH key.
3. Clone this repo: git clone https://github.com/JC-Hall/2508_DS5111_jch7aa.git, then cd into it
4. Run the init script: ./scripts/init.sh
5. Use the included makefile to automate environment creation: make env
6. Once the virtual environment is created: make update
7. Activate the virtual environment: . env/bin/activate
8. Optional - To check installed packages: pip list
9. To leave the environment: deactivate 
10. All scripts should be run from the root of the repo
11. Installing chrome headless browser to be able to collect html content. First, clone scripts repo then cd into it.
Next, run the script with bach install_chrome_headless.sh,
if installed correctly you will see '<h1>Example Domain</h1>' near the bottom. Add the script to your repo. Git Add | Git commit | Git push



