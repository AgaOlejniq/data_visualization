from urllib import response
import requests
from plotly.graph_objs import Bar, Layout
from plotly import offline

url = 'https://api.github.com/search/repositories?q=language:java&sort=stars'
headers = {'Accept' : 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

response_dict = r.json()
repo_dicts = response_dict['items']

# Examine first repo.
first_repo_dict = repo_dicts[0]
for key in first_repo_dict.keys():
    print(key)
    # Keys i need: name, owner-login, stargazers_count, html_url, description

repo_names, stars = [], [] 
for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])
    print(f"\t{repo_dict['name']}")

data = [Bar(x=repo_names, y=stars)]
x_config = {'title': 'Repo names'}
y_config = {'title': 'Stars'}
my_layout = Layout(title='Most-Starred Java Projects on GitHub', xaxis=x_config, yaxis=y_config)
offline.plot({'data' : data, 'layout' : my_layout}, filename='java_repos_visual.html')
