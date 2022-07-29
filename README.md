# Simpleasyncio

- S**impleasyncio enables the normal functions to do asynchronous task in without change the structure.**

# Quickstart

## Passing one argument

```python
import simpleasyncio
import requests
from bs4 import BeautifulSoup

def get_title(url):
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')
    title = soup.select("header > h1")[0].text
    return title

urls = ["https://en.wikipedia.org/wiki/Python_(programming_language)",
        "https://en.wikipedia.org/wiki/GitHub",
        "https://en.wikipedia.org/wiki/Asynchronous_I/O"]

titles = simpleasyncio.call(get_title, urls)
print(titles)

# Results
# ['Python (programming language)', 'GitHub', 'Asynchronous I/O']
```

## Passing two or more arguments

```python
import simpleasyncio

def sayhi(name, repeat=1):
	for i in range(repeat):
		print(f"{i} : Hi {name}!")

parameters=[
            ["Jack", 3],
            ["Bob", {"repeat":2}],
            [{"name":"Fred", "repeat":2}]
            ]
simpleasyncio.call(sayhi, parameters)

# Results
# 0 : Hi Jack!
# 1 : Hi Jack!
# 2 : Hi Jack!
# 0 : Hi Bob!
# 1 : Hi Bob!
# 0 : Hi Fred!
# 1 : Hi Fred!
```
