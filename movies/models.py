from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

    def get_total_rating(self):
        reviews = self.reviews.all()
        cnt = len(reviews)
        if cnt == 0:
            return 0
        else:
            total_rating = 0
            for review in reviews:
                total_rating += review.rating
            return round(total_rating / cnt, 3)
