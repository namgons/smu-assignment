from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

    def get_total_rate(self):
        reviews = self.reviews.all()
        cnt = len(reviews)
        if cnt == 0:
            return 0
        else:
            total_rate = 0
            for review in reviews:
                total_rate += review.rate
            return round(total_rate / cnt, 3)
