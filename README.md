

# Web Template

A template project for dynamic web applications.


## Usage

### Just try it
```
# Install Flask and waitress with your linux package manager.
# Otherwise you could use pip:
pip3 install --user Flask waitress

git clone https://github.com/xengineering/web-template.git
cd web-template
python3 main.py

# switch to another terminal

curl http://localhost:8080  # test with curl
firefox http://localhost:8080  # test with firefox
```

### Use it for your Project
```
# start 'myproject' (rename it if you want to)
git clone https://github.com/xengineering/web-template.git myproject
cd myproject
git remote rename origin template
```

### Get the latest Updates from this template Project
```
git fetch template
git merge template/master
```


## Used Technologies

- [Python 3](https://www.python.org/)
- [Python Flask](https://palletsprojects.com/p/flask/)
- [Waitress WSGI Server](https://github.com/Pylons/waitress)
- Pure HTML, CSS and JavaScript
