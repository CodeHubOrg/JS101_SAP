# JS101_SPA
Single page app for practice

This is a site for practice purpose. Adding js functionality as we go along. 

###To add your profile:

- Clone the repository with 
```bash 
git clone https://github.com/CodeHubOrg/JS101_SAP.git
```
- Create a JSON file inside the profiles/ directory by copying one of the files in there
- Fill in your own details. Note that under the property "lists" you can add your own lists, and they will get displayed in the single view

###To run the site locally
- You will need to generate a new profiles.json file once you\'ve added your profile. The easiest way to do this is from the commandline, by running a python script. If you are in the root folder of the app type in:
```bash
python scripts/concat.py
```
- You will also need to start a server. An easy way to do this is, once again using Python
```bash
python -m SimpleHTTPServer
```

After that you should be able to view the site at localhost:8000

To add your profile to the live site, make a pull request on this repository (fork this repo to your GitHub account, push/make changes to your forked repo, create a pull request through the web interface)
