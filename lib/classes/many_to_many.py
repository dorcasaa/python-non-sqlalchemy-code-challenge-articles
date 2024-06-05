class Article:
    all = []
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        if not isinstance(title, str):
            raise ValueError("Title must be a string")
        if not (5 <= len(title) <=50):
            raise ValueError("Title must be between 5 and 50 characters")
        self.__title = title
        Article.all.append(self)
    
    @property
    def title(self):
        return self.__title 

    @title.setter
    def title(self, value):
        raise AttributeError("Title cannot be modified after instantiation")
    
    
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        if not(isinstance(author, Author)):
            raise ValueError("Object must be an instance of Author class")
        self._author = author

    
    @property
    def magazine(self):
        return self._magazine
    @magazine.setter
    def magazine(self, magazine):
        if not isinstance(magazine, Magazine):
            raise Exception("Object must be an instance of Magazine class")
        self._magazine = magazine    
           
        
class Author:
    def __init__(self, name):
          if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string")
          self.__name = name
          
    
    @property
    def name(self):
        return self.__name 

    @name.setter
    def name(self, value):
        raise AttributeError("Name cannot be modified after instantiation")

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        magazine = set()
        
        for article in self.articles():
            magazine.add(article.magazine)
        return list(magazine)    

    def add_article(self, magazine, title):
        new_article = Article(self,magazine, title)
        return new_article

    def topic_areas(self):
        if not self.articles():
            return None
        else:
            return list({article.magazine.category for article in self.articles()})

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
    
    @property
    def name(self):
        return self._name 
    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2<= len(value) <= 16:
            self._name = value

    
    @property
    def category(self):
        return self._category
    @category.setter
    def category(self, category):
        if isinstance(category, str) and len(category) > 0:
            self._category = category        

            
    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        authors = set()
        for article in self.articles():
            authors.add(article.author)
        return list(authors)    

    def article_titles(self):
        if not self.articles:
            return None
        return list(article.title for article in self.articles())

    def contributing_authors(self):
        contribution = {}
        for article in self.articles:
            if contribution.get(article.author, 0) > 2:
                contribution[article.author] += 1
        return [author for author, count in contribution.items() if count >= 2]