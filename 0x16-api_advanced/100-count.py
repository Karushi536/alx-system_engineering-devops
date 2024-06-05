#!/usr/bin/python3
"""
recursive function that queries the Redit API, parses the title of
all hot articles, and prints a sorted count of given keywords
"""
import requests


def count_words(subreddit, word_list, after='', word_count=None):
    if word_count is None:
        word_count = {word.lower(): 0 for word in word_list}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'python:keywords:v1.0 (by /u/yourusername)'}
    params = {'after': after}

    try:
        response = requests.get(url, headers=headers,
                                params=params, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            articles = data['data']['children']

            for article in articles:
                title = article['data']['title'].lower()
                words = title.split()
                for word in words:
                    clean_word = ''.join(char for char in
                                         word if char.isalnum())
                    if clean_word in word_count:
                        word_count[clean_word] += 1

            after = data['data']['after']
            if after is not None:
                count_words(subreddit, word_list, after, word_count)
            else:
                sorted_words = sorted(word_count.items(),
                                      key=lambda item: (-item[1], item[0]))
                for word, count in sorted_words:
                    if count > 0:
                        print(f"{word}: {count}")
        else:
            return
    except requests.RequestException:
        return


# Example usage
subreddit = 'learnpython'
word_list = ['Python', 'code', 'java', 'JavaScript', 'javascript', 'java']
count_words(subreddit, word_list)
