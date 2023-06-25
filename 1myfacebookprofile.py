# Chap04/facebook_my_profile.py
import os
import json
import facebook

def getTokenFromFile(fileName):
    with open(fileName, encoding='utf-8') as fp:
        return fp.readline()

if __name__ == '__main__':
    #token = os.environ.get('FACEBOOK_TEMP_TOKEN')
    token = getTokenFromFile("FacebookToken.txt")
    graph = facebook.GraphAPI(token)
    profile = graph.get_object("me")
    profile = graph.get_object("me", fields='name,location{general_info,location}')
    #profile = graph.get_object({"me",permission})
    print(json.dumps(profile, indent=4))