import requests
import matplotlib.pyplot as plt 
import numpy
usernames = input('tell me the usernames ;)\n->').split(' ')
names = []
followers = []
for username in usernames:
	print(username, end=': ')
	count = requests.get(f'https://www.instagram.com/{username}/?__a=1').json()["graphql"]["user"]['edge_followed_by']["count"]
	print(count)
	names.append(username)
	followers.append(count)

names = numpy.array(names)
followers = numpy.array(followers)

plt.bar(names, followers)
plt.show()
