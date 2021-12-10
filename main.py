import requests
import matplotlib.pyplot as plt 
import numpy
usernames = input('tell me the usernames ;)\n->').split(' ')
names = followers = []
fig, ax = plt.subplots()
for username in usernames:
	print(f"{username} ", requests.get(f'https://www.instagram.com/{username}/?__a=1').json()["graphql"]["user"]['edge_followed_by']["count"])
	names.append(username)
	followers.append(requests.get(f'https://www.instagram.com/{username}/?__a=1').json()["graphql"]["user"]['edge_followed_by']["count"])
names, followers, labels = numpy.array(names), numpy.array(followers), followers
def autolabel(rects):
    [ax.text(rect.get_x() + rect.get_width()/2., 1.05*rect.get_height(), labels[idx], ha='center', va='bottom', rotation=0) for idx,rect in enumerate(plt.bar(names, followers))] 
autolabel(plt.bar(names, followers))
plt.ylim(0,max(followers)*1.05)
plt.title('Instagram Followers Comparator.')
plt.show()
