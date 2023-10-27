from django.db import models
from django.conf import settings

class Post(models.Model):
    # TODO: Add a title field for the blog post. It should be a character field with a suitable max length.
    
    # TODO: Add content for the blog post. Consider using a TextField.
    
    # TODO: Add a publish_date to track when the post was published. It should be set automatically when a post is created.
    
    # TODO: Add an author field. This should be a foreign key linking to the user who wrote the post. 
    # Consider using Django's default user model.
    
    def __str__(self):
        # TODO: Return a suitable string representation for the post.
        pass

class Comment(models.Model):
    # TODO: Link each comment to a specific post. Consider using a ForeignKey.
    
    # TODO: Add an author_name field. It should allow for the name of the person commenting.
    
    # TODO: Add the main text/content of the comment.
    
    # TODO: Add a created_date to track when the comment was added.
    
    # TODO: Implement a mechanism to approve comments before they're displayed (e.g., an approved_comment boolean field).

    def approve(self):
        # TODO: Define a method to approve a comment.
        pass

    def __str__(self):
        # TODO: Return a suitable string representation for the comment.
        pass
