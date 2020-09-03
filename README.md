

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
git branch template  # create branch for the template
git branch --set-upstream-to=template/master template
git branch --unset-upstream master
```

### Add a Remote for your specific Project
**This could delete data on your remote (git push -f)!** It is no problem if the remote repository is empty (e.g. if you just created it on GitHub).
```
git remote add origin <myproject-upstream-url>  # use ssh url here
git branch -M master
git push -uf origin master
```


## Used Technologies

- [Python 3](https://www.python.org/)
- [Python Flask](https://palletsprojects.com/p/flask/)
- [Waitress WSGI Server](https://github.com/Pylons/waitress)
- Pure HTML, CSS and JavaScript
