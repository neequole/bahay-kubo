# bahay-kubo
Boilerplate of Graphene workshop for Pycon APAC 2019.

## Setup Requirements
* Internet :satisfied:

You should have this installed prior to the workshop:
* Python3 (Bundled with the `venv` module to create virtual environments)
* virtualenv if `venv` is unavailable
* pip
* git (optional)
* Editor

## Setup
1. Create the project directory
```
mkdir graphene-tutorial
cd graphene-tutorial
```

2. Create a virtual environment
```
python3 -m venv env3

On Windows:
py -3 -m venv env3
```

3. Activate the environment
```
source env3/bin/activate

On Windows:
source env3\Scripts\activate
```

4. If you have `git`, clone the `bahay-kubo` :house_with_garden: project from Github. If not, just download it as ZIP and uncompressed it.
```
git clone https://github.com/neequole/bahay-kubo.git
```

5. Go to the boilerplate folder
```
cd bahay-kubo
```

6. Install requirements
```
pip install -r requirements.txt
```

7. Run and check if the project is running!
```
python app.py

Output:
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit) <------ Open the link on your browser
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 262-544-471
```

## Say hello to Mang Netong!

1.  Pull the latest project copy
```
git pull origin master
``` 

2. Go to the `graphql` endpoint which is like http://127.0.0.1:5000/graphql

3. Type in the ff. and say hello :wave: to Mang Netong!
```
{
  hello
}
```


## Setup Problems During the Workshop

### No laptop

* Approach us and we'll pair you with one attendee

### Internet available but no Editor/Python installed

* You can use our repl.it online editor `https://repl.it/@NicoleTibay/UnkemptUnusualState`

### No Python installed during workshop

* Follow the guide [here](https://realpython.com/installing-python/)

* If there is no internet, we have a USB around that contains some resources, borrow it and copy the installer from `python-installers`
  - Windows
    - Windows 32-bit - `python-installers -> win -> python-3.7.2.exe`
    - Windows 64-bit - `python-installers -> win -> python-3.7.2-amd64.exe`
    - Double-click the executable to run the installer
    > Important: Check the box that says Add Python 3.x to PATH!
  
  - Mac
    - `python-installers -> mac-os -> python-3.7.2-macosx10.6.pkg`
    - Double-click the executable to run the installer
    
  - Linux
     - Install from source. [Ref](https://passingcuriosity.com/2015/installing-python-from-source/)
       - `python-installers -> Python-3.7.2.tgz`
       
       ```
       tar xvf Python-3.7.2.tgz
       cd Python-3.7.2
       ./configure
       make
       make test
       sudo make install
       ```
       
       - You may need to update your system and install required build tools which may need Internet. [Ref](https://www.rosehosting.com/blog/how-to-install-python-3-6-4-on-debian-9/)
       
       ```
       sudo apt-get update && sudo apt-get upgrade
       sudo apt-get install -y make build-essential libssl-dev zlib1g-dev
       sudo apt-get install -y libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm
       sudo apt-get install -y libncurses5-dev  libncursesw5-dev xz-utils tk-dev
       ```
     
     - For those with Ubuntu 18.04 LTS (Bionic Beaver), we have a `3.6.7` deb file available
       - `python-installers -> python3_3.6.7-1_18.04_i386.deb`
       
       ```
       sudo dpkg -i /path/to/deb/file
       sudo apt install ./name.deb
       ```

* Alternatively, you can approach us and we'll pair you with one attendee

### Required libraries are not installed

* Just follow the Setup section above

* If there is no internet, we have a USB around that contains some resources.
  - Copy the `lib-requirements` folder to the main project folder (same level as your env and bahay-kubo folder)
  - Run the ff (instruction is also in the folder under `how_to.py`):
  ```
  source env/bin/activate
  cd bahay-kubo
  pip install --no-index --find-links="../lib-requirements" -r requirements.txt
  pip list
  ```
  
### Enable offline GraphiQL

* Override your Virtual environment's `/site-packages/flask_graphql/render_graphiql.py` with `bahay-kubo/tmp/render_graphiql.py`