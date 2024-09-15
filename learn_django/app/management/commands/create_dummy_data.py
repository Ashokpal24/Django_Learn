from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from tag.models import Tag
from article.models import Article
from comment.models import Comment
from author.models import AuthorProfile


class Command(BaseCommand):
    help = 'Create dummy data for the blog'

    def handle(self, *args, **kwargs):
        # Create Users and Author Profiles
        user1 = User.objects.create_user(
            username='john_doe', password='password123')
        user2 = User.objects.create_user(
            username='jane_smith', password='password123')
        user3 = User.objects.create_user(
            username='mike_jones', password='password123')
        user4 = User.objects.create_user(
            username='emma_brown', password='password123')
        user5 = User.objects.create_user(
            username='oliver_white', password='password123')

        AuthorProfile.objects.create(
            user=user1, bio="Tech enthusiast and avid writer.")
        AuthorProfile.objects.create(
            user=user2, bio="Loves writing about the latest in fashion.")
        AuthorProfile.objects.create(
            user=user3, bio="Passionate about food and travel.")
        AuthorProfile.objects.create(
            user=user4, bio="A coder who blogs about programming tips.")
        AuthorProfile.objects.create(
            user=user5, bio="Interested in finance and business trends.")

        # Create Tags
        tag1 = Tag.objects.create(name='Technology')
        tag2 = Tag.objects.create(name='Fashion')
        tag3 = Tag.objects.create(name='Food')
        tag4 = Tag.objects.create(name='Programming')
        tag5 = Tag.objects.create(name='Finance')

        # Create Articles and associate Tags
        article1 = Article.objects.create(title="The Rise of AI in Everyday Life",
                                          content="Artificial intelligence is now more integrated...", author=user1)
        article1.tags.add(tag1, tag4)

        article2 = Article.objects.create(
            title="Top Fashion Trends of 2024", content="As we step into the new year...", author=user2)
        article2.tags.add(tag2)

        article3 = Article.objects.create(
            title="Best Street Foods Around the World", content="Traveling for food is the best way...", author=user3)
        article3.tags.add(tag3)

        article4 = Article.objects.create(
            title="Understanding REST APIs: A Beginner's Guide", content="REST APIs are essential...", author=user4)
        article4.tags.add(tag1, tag4)

        article5 = Article.objects.create(title="How to Invest in the Stock Market in 2024",
                                          content="The stock market can be intimidating...", author=user5)
        article5.tags.add(tag5)

        # Create Comments
        Comment.objects.create(
            article=article1, comment="This is a great introduction to AI.", user=user2, likes=5, dislikes=0)
        Comment.objects.create(
            article=article2, comment="I disagree with some trends.", user=user3, likes=3, dislikes=1)
        Comment.objects.create(
            article=article3, comment="I've tried most of these foods!", user=user1, likes=7, dislikes=0)
        Comment.objects.create(
            article=article4, comment="This guide helped me understand REST APIs.", user=user5, likes=6, dislikes=0)
        Comment.objects.create(
            article=article5, comment="Really helpful advice for stocks.", user=user4, likes=4, dislikes=0)

        self.stdout.write(self.style.SUCCESS(
            'Dummy data created successfully'))
