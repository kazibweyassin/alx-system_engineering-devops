# Reddit API Project

This project consists of Python scripts that interact with the Reddit API for various tasks. The scripts are designed to help you practice working with APIs, handling JSON data, and performing tasks such as retrieving the number of subscribers for a subreddit, fetching the top posts, and recursively getting all hot articles.

## Table of Contents

- [Project Overview](#project-overview)
- [Learning Objectives](#learning-objectives)
- [Project Structure](#project-structure)
- [How to Use](#how-to-use)
- [Dependencies](#dependencies)
- [Author](#author)
- [License](#license)

## Project Overview

This project includes three tasks:

1. **How many subs?**
   - Retrieve the number of subscribers for a given subreddit.

2. **Top Ten**
   - Print the titles of the first 10 hot posts for a specified subreddit.

3. **Recurse it!**
   - Recursively fetch all hot articles for a given subreddit.

## Learning Objectives

By completing this project, you will gain experience in:

- Reading API documentation to find the desired endpoints.
- Using an API with pagination.
- Parsing JSON results from an API.
- Making recursive API calls.
- Sorting a dictionary by value.

## Project Structure

The project is organized into three Python scripts:

1. `0-subs.py` - Retrieves the number of subscribers for a subreddit.
2. `1-top_ten.py` - Prints the titles of the first 10 hot posts for a subreddit.
3. `2-recurse.py` - Recursively fetches all hot articles for a subreddit.

## How to Use

### Task 0: How many subs?

```bash
$ ./0-subs.py <subreddit_name>

