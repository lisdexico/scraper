import requests


class Peer:

    def __init__(self, hostname, display_name):
        self.hostname = hostname
        self.display_name = display_name

    def __str__(self):
        return self.display_name


    def count_users(self):
        response = requests.get(f"https://{self.hostname}/comms/status")
        return response.json()["usersCount"]
