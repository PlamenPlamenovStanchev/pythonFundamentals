class Articles:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def edit(self, new_content: str):
        self.content = new_content


    def change_author(self, new_author: str):
        self.author = new_author


    def rename(self, new_title:str):
        self.title = new_title


    def __repr__(self):
        return f" {self.title} - {self.content}: {self.author}"

article = Articles("Highest Recorded Temperature", "Temperatures across Europe are unprecedented, according to scientists.","Ben Turner")

print(article.edit("Syracuse, a city on the coast of the Italian island of Sicily, registered temperatures of 48.8 degrees Celsius"))
print(article.rename("Temperature in Italy"))
print(article.change_author("B. T."))

print(article)


# class Article:
#     def __init__(self, title, content, author):
#         self.title = title
#         self.content = content
#         self.author = author
#
#     def edit(self, new_content):
#         self.content = new_content
#
#     def change_author(self, new_author):
#         self.author = new_author
#
#     def rename(self, new_title):
#         self.title = new_title
#
#     def __repr__(self):
#         return f"{self.title} - {self.content}: {self.author}"
#
#
# article1 = Article("Python Basics", "Introduction to Python programming.", "John Doe")
#
# print(article1)
#
# article1.edit("Updated content about Python programming.")
# article1.change_author("Jane Smith")
# article1.rename("Advanced Python")
# print(article1)