from flask_app.config.mysqlconnection import connectToMySQL
import re	# the regex module
from flask import flash
# create a regular expression object that we'll use later   
class Post:
    db_name = 'mypythonclass'
    def __init__( self , data ):
        self.id = data['id']
        self.title = data['title']
        self.content = data['content']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database


    @classmethod
    def get_post_by_id(cls, data):
        query = 'SELECT * FROM posts WHERE id= %(post_id)s;'
        results = connectToMySQL(cls.db_name).query_db(query, data)
        if results:
            return results[0]
        return False

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM posts LEFT JOIN users on posts.user_id = users.id;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(cls.db_name).query_db(query)
        # Create an empty list to append our instances of friends
        posts = []
        # Iterate over the db results and create instances of friends with cls.
        if results:
            for post in results:
                posts.append( post )
            return posts
        return posts
    
    @classmethod
    def get_all_user_post(cls, data):
        query = "SELECT * FROM posts LEFT JOIN users on posts.user_id = users.id WHERE posts.user_id = %(user_id)s;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(cls.db_name).query_db(query, data)
        # Create an empty list to append our instances of friends
        posts = []
        # Iterate over the db results and create instances of friends with cls.
        if results:
            for post in results:
                posts.append( post )
            return posts
        return posts
    
    @classmethod
    def create_post(cls, data):
        query = "INSERT INTO posts (title, content, user_id) VALUES ( %(title)s, %(content)s,%(user_id)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)
    
    @classmethod
    def update_post(cls, data):
        query = "UPDATE posts SET title = %(title)s, content = %(content)s WHERE id = %(post_id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)
    
    @classmethod
    def delete_post(cls, data):
        query = "DELETE FROM posts WHERE id = %(post_id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)
    
    @classmethod
    def delete_all_user_posts(cls, data):
        query = "DELETE FROM posts WHERE user_id = %(user_id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)
    

    @staticmethod
    def validate_post(post):
        is_valid = True
        # test whether a field matches the pattern
        
        if len(post['title'])< 2:
            flash('Title must be more than 2 characters', 'postTitle')
            is_valid = False
        if len(post['content'])< 2:
            flash('Post content must be more than 2 characters', 'postContent')
            is_valid = False
        return is_valid
