from django.db import models


class ObjectClass(models.Model):
    class_name = models.CharField(unique=True, max_length=20)
    class_description = models.CharField(max_length=250)

    def __str__(self):
        return self.class_name


class Item(models.Model):
    item_number = models.IntegerField(unique=True)
    object_class = models.ForeignKey(ObjectClass, on_delete=models.CASCADE)
    containment_procedure = models.CharField(max_length=1000)
    item_description = models.CharField(max_length=2000)
    code_name = models.CharField(max_length=100)
    item_image = models.CharField(max_length=500)
#   add in location along with location model

    objects = models.Manager()

    def __str__(self):
        return 'SCP-' + str(self.item_number) + ' / ' + str(self.code_name)
