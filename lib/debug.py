#!/usr/bin/env python3
import ipdb;

from classes.many_to_many import Article
from classes.many_to_many import Author
from classes.many_to_many import Magazine

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")
author1 = Author("Alice")
magazine1 = Magazine("Tech Today", "Technology")
article1 = author1.add_article(magazine1, "The Future of AI")

print(author1.name)
print(magazine1.name)
print(article1.title)
print(article1.author.name)
print(article1.magazine.name)
print(author1.articles)
print(author1.magazines())
print(magazine1.articles)
print(magazine1.contributors())
print(author1.topic_areas())
print(magazine1.article_titles())
print(magazine1.contributing_authors())

    # don't remove this line, it's for debugging!
ipdb.set_trace()
