import requests
import json
from graph import Graph

def auth():
    with open("token.json", "r") as read_file:
        data = json.load(read_file)
    return data['username'], data['token']

def get_usernames(users):
    return map(lambda x: x['login'], users)

def connect(user, source):
    return (source, user, 1)

def make_connections(users, source):
    return map(lambda x: connect(x, source), users)

def fetch_followers(username, token):
    followers = requests.get('https://api.github.com/user/followers', auth=(username, token)).json()
    usernames = get_usernames(followers)

    return usernames

def main(username, token):
    usernames = fetch_followers(username, token)
    array = make_connections(usernames, source)
    graph = Graph(array)

    print(graph.dijkstra('katretyakova', 'nicklyu'))


if __name__ == "__main__":
    username, token = auth()
    main(username, token)
