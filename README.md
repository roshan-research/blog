Blog
====

Sobhe's Blog

Installing Dependencies
-----------------------
```
pip install pelican Markdown
```

also for publishing to gh-pages:
```
pip install ghp-import
```


Becarefull! Submodules
----------------------

when cloning:

    git clone git@….git --recursive
    
if you have already cloned:

    git submodule update --init


Publishing New Articles
-----------------------
0. `git checkout master`
1. make a new post in `content` directory.
2. `make publish`
3. `git commit -m 'message'`
4. `git push origin master`
5. `ghp-import output`
6. `git push origin gh-pages`
