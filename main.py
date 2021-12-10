import requests
import matplotlib.pyplot as plt 
import numpy
usernames = input('tell me the usernames ;)\n->').split(' ')
names = []
followers = []
fig, ax = plt.subplots()
for username in usernames:
	print(f"{username} ", requests.get(f'https://www.instagram.com/{username}/?__a=1').json()["graphql"]["user"]['edge_followed_by']["count"])
	names.append(username)
	followers.append(requests.get(f'https://www.instagram.com/{username}/?__a=1').json()["graphql"]["user"]['edge_followed_by']["count"])
names = numpy.array(names)
followers = numpy.array(followers)
labels = followers
def autolabel(rects):
    for idx,rect in enumerate(plt.bar(names, followers)):
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*rect.get_height(),
                labels[idx],
                ha='center', va='bottom', rotation=0)
autolabel(plt.bar(names, followers))
plt.ylim(0,max(followers)*1.05)
plt.title('Instagram Followers Comparator.')
plt.show()
