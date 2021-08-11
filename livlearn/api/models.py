from django.db import models


class Link(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    ADVANCED = 'AD'
    INTERMEDIATE = 'IN'
    BEGINNER = 'BE'
    ANY = "AN"
    LEVEL_CHOICES = [
        (ANY, 'Any level'),
        (BEGINNER, 'Beginner'),
        (INTERMEDIATE, 'Intermediate'),
        (ADVANCED, 'Advanced')
    ]
    level = models.CharField(
        max_length=2,
        choices=LEVEL_CHOICES,
        blank=False,
        default=ANY
    )

    PODCAST = "PO"
    BOOK = "BO"
    AUDIOBOOK = "AB"
    BLOG = "BL"
    ARTICLE = "AR"
    COURSE = "CO"
    VIDEO = "VI"
    TOOL = "TO"
    OTHER = "OT"
    DOCUMENTATION = "DO"
    FORUM = "FO"

    TYPE_CHOICES = [
        (PODCAST, 'Podcast'),
        (BOOK, 'Book'),
        (AUDIOBOOK, 'Audiobook'),
        (BLOG, 'Blog'),
        (ARTICLE, 'Article'),
        (COURSE, 'Course'),
        (VIDEO, 'Video'),
        (TOOL, 'Tool'),
        (OTHER, 'Other'),
        (DOCUMENTATION, 'Documentation'),
        (FORUM, 'Forum')
    ]
    type = models.CharField(
        max_length=2,
        choices=TYPE_CHOICES,
        blank=False,
        default=OTHER
    )

    url = models.URLField(max_length=300, blank=False)
    description = models.TextField(max_length=500, blank=False)
    tagline = models.CharField(max_length=100, blank=False)
    name = models.CharField(max_length=100, blank=False)
    tags = models.ManyToManyField(
        to='api.Tag',
        related_name='links',
        blank=True
    )

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class FormSubmission(models.Model):
    submitted_at = models.DateTimeField(auto_now_add=True)
    form_name = models.CharField(max_length=30)
    content = models.TextField(max_length=5000)

    def __str__(self):
        return self.form_name
