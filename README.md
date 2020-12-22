

# Web Template

A template project for mixed static / dynamic web applications.


## Usage

Just follow these steps:
1. Edit config.json
2. Edit the files in the webroot folder
3. Upload the webroot to your target server with ```python3 manage.py deploy``` via SSH / rsync

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

