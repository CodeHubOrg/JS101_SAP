#!/usr/bin/python

import os

PATH = os.path.abspath(os.path.dirname(__file__))

profiles = os.listdir(os.path.dirname(PATH) + "/profiles")
profile_list = os.path.dirname(PATH) + "/profiles.json"

profile_list = open(profile_list, "w")
profile_list.write("[")

nr_profiles = len(profiles)
count = 0

for file in  profiles:
    f = open(os.path.dirname(PATH) + "/profiles/" + file, "r")
    profile_list.write(f.read())
    count += 1
    if count < nr_profiles: 
    	profile_list.write(", \n")

profile_list.write("]")


print ("concatenated profiles")