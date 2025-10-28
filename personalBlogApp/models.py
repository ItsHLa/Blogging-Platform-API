from django.db import models
from django.contrib.auth.models import User

class Tags(models.TextChoices):
    LIFE_STORIES = "life_stories", "Life & Stories"
    LIFESTYLE = "lifestyle", "Lifestyle"
    TRAVEL = "travel", "Travel"
    FOOD_DRINK = "food_drink", "Food & Drink"
    HEALTH_WELLNESS = "health_wellness", "Health & Wellness"
    PERSONAL_GROWTH = 'personal_growth', "Personal Growth",
    HOBBIES = "hobbies", "Hobbies & Interests"
    OPINIONS = "opinions", "Opinions & Thoughts"
    TECHNOLOGY = "technology", "Technology"
    FASHION_BEAUTY = "fashion_beauty", "Fashion & Beauty"
    FINANCE = "finance", "Finance & Money"
    BLOGGING = "blogging", "Blogging & Creativity"
    
class Blog(models.Model):
    title = models.CharField(max_length=100)
    slug =models.SlugField(max_length=200)
    content =models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    tags = models.CharField(
        max_length=60,
        choices=Tags.choices,
        default=Tags.LIFE_STORIES
    )
    likedBy = models.ManyToManyField(
        User,
        related_name='likedBlogs',
        blank=True,   
    )
    authoredBy = models.ForeignKey(
        User,
        related_name='authoredBlogs',
        on_delete=models.CASCADE
    )
    
    class Meta:
        ordering = ["-createdAt"]
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    
    content = models.CharField(max_length=500)
    createdAt = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(
        Blog,
        related_name="BlogComments",
        on_delete=models.CASCADE
    )
    parent = models.ForeignKey(
        "self",
        null = True,
        blank = True,
        related_name="CommentReplies",
        on_delete=models.CASCADE
    )
    likedBy = models.ManyToManyField(
        User,
        related_name="LikedComment",
        blank=True,
        
    )
    authorBy = models.ForeignKey(
        User,
        related_name='authoredComments',
        on_delete=models.CASCADE)
    
    class Meta:
        ordering = ["-createdAt"]
    
    def __str__(self):
        return self.content
