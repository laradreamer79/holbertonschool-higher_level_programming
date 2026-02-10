#!/usr/bin/python3

import requests
import csv
'''Fetch and process posts from JSONPlaceholder API '''

requests.get("https://jsonplaceholder.typicode.com/posts")


def fetch_and_print_posts():
    """Fetch posts from JSONPlaceholder and print titles"""
    r = requests.get("https://jsonplaceholder.typicode.com/posts")

    print(f"Status Code: {r.status_code}")

    if response.status_code == 200:
        posts = r.json()

        for post in posts:
            print(post.get("title"))


def fetch_and_save_posts():
    """ Fetch posts and save them into csv file """

    r = requests.get("https://jsonplaceholder.typicode.com/posts")

    if r.status_code == 200:
        posts = r.json()

        structured_posts = [ 
            { "id": post.get("id"),
              "title": post.get("title"),
              "body": post.get("body")
             }
             for post in posts
                            ]

        with open("posts.csv", "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["id", "title", "body"]
            writer = csv.Dictwriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(structured_posts)
