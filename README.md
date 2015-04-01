# JS101_SPA
Single page app for practice

This is a site for practice purpose. Adding js functionality as we go along. 

###To add your profile:

- Create a JSON file inside the profiles/ directory by copying one of the files in there
- Fill in your own details. Note that under the property "lists" you can add your own lists, and they will get displayed in the single view

To add it to the live site, make a pull request on this repository

###To run the site locally
- You will need to generate a new profiles.json file to add a new profile. The easiest way to do this is from the commandline, by running a python script. If you are in the root folder of the app type in:
```bash
python scripts/concat.py
```
- You will also need to start a server. An easy way to do this is, once again using Python
```bash
python -m SimpleHTTPServer
```

After that you should be able to view the site at localhost:8000


