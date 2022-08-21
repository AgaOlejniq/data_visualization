import json
from operator import itemgetter
from urllib import response
import requests
from plotly.graph_objs import Bar
from plotly import offline

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

sub_ids = r.json()
readable_subs = r'python_crash_course\part_2\data_visualization\excersises\readable_subs.json'

with open(readable_subs, 'w') as f:
    json.dump(sub_ids, f, indent=4)

sub_dicts = []

for sub_id in sub_ids[:20]:
    url = f"https://hacker-news.firebaseio.com/v0/item/{sub_id}.json"
    r = requests.get(url)
    print(f"id: {sub_id} \tstatus: {r.status_code}")
    response_dict = r.json()

    sub_dict = {
        'title' : response_dict['title'],
        'hn_link' : f"http://news.ycombinator.com/item?id={sub_id}",
        'comments' : response_dict['descendants'],
    }
    sub_dicts.append(sub_dict)

sub_dicts = sorted(sub_dicts, key=itemgetter('comments'), reverse=True)

for sub_dict in sub_dicts:
    print(f"\nTitle: {sub_dict['title']}")
    print(f"Discussion link: {sub_dict['hn_link']}")
    print(f"Comments: {sub_dict['comments']}")

titles, comments, discussion_links = [], [], [] 

for sub in sub_dicts:
    title = sub['title']
    link = sub['hn_link']
    discussion_link = f"<a href='{link}'>{title[:15]}...</a>"

    titles.append(title)
    comments.append(sub['comments'])
    discussion_links.append(discussion_link)

data = [{
    'type' : 'bar',
    'x' : discussion_links,
    'y' : comments,
    'hovertext' : titles,
    'marker' : {
        'color' : 'rgb(25,150,50)',
        'line' : {'width' : 2, 'color' : 'rgb(10,10,10)'},
    },
    'opacity' : 0.5
}]

my_layout = {
    'title' : 'Most commented articles on Hacker News',
    'xaxis' : {
        'title' : 'Article',
    },
    'yaxis' : {
        'title' : 'Number of comments',
    }
}

fig = {'data' : data, 'layout' : my_layout}
offline.plot(fig, filename=r'python_crash_course\part_2\data_visualization\excersises\hn_active_discussions_visual.html')