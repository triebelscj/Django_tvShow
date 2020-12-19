from django.db import models


# Creating validations!
class ShowManager(models.Manager):
    # NO FIELDS should be blank
    # title at least 2 chars
    # desc at least 10 char
    # network at least 3 char
    def validateShow(self, postData):
        errors = {}
        print("///////// ", postData)
        if len(postData["title"]) < 1:
            errors["title"] = "Title is required."
        if len(postData["title"]) < 2:
            errors["title"] = "Title must be longer than 2 Characters."
        if len(postData["network"]) == 0:
            errors["network"] = "Network is required."
        if len(postData["network"]) < 3:
            errors["network"] = "Network must be longer than 2 Characters."
        if len(postData["release_date"]) == 0:
            errors["release_date"] = "Release Date must not be blank."
        if len(postData["description"]) == 0:
            errors["description"] = "Description is required."
        if len(postData["description"]) < 10:
            errors["description"] = "Description must be longer than 10 Characters."

        return errors


class Show(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ShowManager()

    def __str__(self):
        return f'show: {self.title} {self.network}'
