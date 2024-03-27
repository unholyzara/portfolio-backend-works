from django.db import models


class Company(models.Model):
    active = models.BooleanField(default=False)
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = [
            "name",
        ]

    def __str__(self):
        return self.name


class Work(models.Model):
    active = models.BooleanField(default=False)
    date_from = models.DateField()
    date_to = models.DateField(blank=True, null=True)
    date_from = models.DateField()
    date_to = models.DateField(blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True)
    role = models.TextField()
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = [
            "slug",
        ]

    def __str__(self):
        return self.slug


class JobDuty(models.Model):
    active = models.BooleanField(default=False)
    description = models.TextField()
    work = models.ForeignKey(Work, on_delete=models.SET_NULL, null=True)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = [
            "slug",
        ]

    def __str__(self):
        return self.slug
