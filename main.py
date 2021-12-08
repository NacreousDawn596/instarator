import requests
import matplotlib.pyplot as plt 
import numpy
usernames = input('tell me the usernames ;)\n->').split(' ')
names = []
followers = []
fig, ax = plt.subplots()
for username in usernames:
	print(username, end=': ')
	count = requests.get(f'https://www.instagram.com/{username}/?__a=1').json()["graphql"]["user"]['edge_followed_by']["count"]
	print(count)
	names.append(username)
	followers.append(count)
names = numpy.array(names)
followers = numpy.array(followers)
labels = followers
data = plt.bar(names, followers)
def autolabel(rects):
    for idx,rect in enumerate(data):
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                labels[idx],
                ha='center', va='bottom', rotation=0)
autolabel(data)
plt.ylim(0,max(followers)*1.05)
plt.title('Instagram Followers Comparator.')
plt.show()
