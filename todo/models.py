from django.db import models

class ToDo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
   

    def __str__(self):
        return self.title

class Photo(models.Model):
    todo = models.ForeignKey(ToDo, related_name='photos', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Photo for {self.todo.title}"