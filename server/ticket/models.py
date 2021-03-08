import uuid
from django.db import models
from django.db.models import Q
from django.db.models import Value
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import pre_delete, post_save
from django.dispatch import receiver
from simple_history.models import HistoricalRecords

from user.models import User
from plugs import push, message

def file_path_name(instance, filename):
    file_path = 'uploads/{model}/{id}/{filename}'.format(model=instance.content_type.model, id=instance.object_id, filename=filename) 
    return file_path

class UpLoad(models.Model):

    uid = models.UUIDField(default=uuid.uuid4, editable=False)
    remark = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to=file_path_name, blank=True)
    date = models.DateField(auto_now_add=True)  
    author = models.ForeignKey(User, related_name='uploads', on_delete=models.SET_NULL, blank=True, null=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()

    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        db_table = 'upload'

class Message(models.Model):
    
    json = models.JSONField(null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    read = models.BooleanField(default=False, blank=True, null=True)
    
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    user = models.ForeignKey(User, related_name='messages', on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        db_table = 'message'

class Comment(models.Model):
    
    content = models.TextField(blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    read = models.BooleanField(default=False, blank=True, null=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    user = models.ForeignKey(User, related_name='comments', on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        db_table = 'comment'

class Booking(models.Model):
    title = models.CharField(blank=True, null=True, max_length=64)
    remark = models.TextField(blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    
    messages = GenericRelation(Message, related_query_name='booking')
    comments = GenericRelation(Comment, related_query_name='booking')
    uploads = GenericRelation(UpLoad, related_query_name='booking')   
    author = models.ForeignKey(User, related_name='bookings', on_delete=models.SET_NULL, blank=True, null=True)
    history = HistoricalRecords(table_name='booking_history', custom_model_name='booking_history')

    class Meta:
        db_table = 'booking'
    
    def delete(self):
        self.messages.all().delete()
        self.comments.all().delete()
        self.itineraries.all().delete()
        
        super().delete()

class Itinerary(models.Model):
    serial_no = models.CharField(blank=True, null=True, max_length=32)
    email = models.CharField(blank=True, null=True, max_length=64)
    name = models.CharField(blank=True, null=True, max_length=64)
    passport_no = models.CharField(blank=True, null=True, max_length=16)
    entry = models.CharField(blank=True, null=True, max_length=256)
    exit = models.CharField(blank=True, null=True, max_length=256)
    ticket1 = models.CharField(blank=True, null=True, max_length=256)
    ticket2 = models.CharField(blank=True, null=True, max_length=256)
    hotel = models.CharField(blank=True, null=True, max_length=256)
    is_lock = models.BooleanField(default=False, null=True)
    remark = models.TextField(blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    
    user = models.ForeignKey(User, related_name='itinerary_users', on_delete=models.SET_NULL, blank=True, null=True)
    author = models.ForeignKey(User, related_name='itinerary_authors', on_delete=models.SET_NULL, blank=True, null=True)
    booking = models.ForeignKey(Booking, related_name='itineraries', on_delete=models.SET_NULL, blank=True, null=True)
    
    history = HistoricalRecords(table_name='itinerary_history', custom_model_name='itinerary_history')

    class Meta:
        db_table = 'itinerary'
        permissions = (
            ('lock_itinerary', 'Can lock itinerary'),
        )
    
    def __str__(self):
        return self.serial_no

class Ticket(models.Model):
    serial_no = models.CharField(blank=True, null=True, max_length=32)
    air_line = models.CharField(blank=True, null=True, max_length=16)
    air_info = models.CharField(blank=True, null=True, max_length=1024)
    air_class = models.CharField(blank=True, null=True, max_length=64)
    fare = models.FloatField(blank=True, null=True)
    tax = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    is_confirm = models.BooleanField(default=None, blank=True, null=True)
    is_cancel = models.BooleanField(default=False, blank=True, null=True)
    is_booking = models.BooleanField(default=True, blank=True, null=True)
    is_complete = models.BooleanField(default=False, blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    
    class NormalStatus(models.IntegerChoices):
        New = 0,
        Booked = 1,
        Watting = 2,
        Confirmed = 3,
        Refused = 4,
        Completed = 5
    
    class ChangeStatus(models.IntegerChoices):
        New = 0,
        Changed = 1,
        Watting = 2,
        Confirmed = 3,
        Refused = 4,
        Completed = 5

    class CancelStatus(models.IntegerChoices):
        New = 0,
        Canceled = 1,
        Watting = 2,
        Confirmed = 3,
        Refused = 4,
        Completed = 5
    
    normal_status = models.IntegerField(choices=NormalStatus.choices, default=NormalStatus.New, blank=True, null=True)
    change_status = models.IntegerField(choices=ChangeStatus.choices, default=NormalStatus.New, blank=True, null=True)
    cancel_status = models.IntegerField(choices=CancelStatus.choices, default=NormalStatus.New, blank=True, null=True)
    type_status = models.IntegerField(default=0, blank=True, null=True)
    
    itinerary = models.ForeignKey(Itinerary, related_name='tickets', on_delete=models.SET_NULL, blank=True, null=True)
    messages = GenericRelation(Message, related_query_name='ticket')
    comments = GenericRelation(Comment, related_query_name='ticket')
    uploads = GenericRelation(UpLoad, related_query_name='ticket')

    author = models.ForeignKey(User, related_name='ticket_authors', on_delete=models.SET_NULL, blank=True, null=True)
    history = HistoricalRecords(table_name='ticket_history', custom_model_name='ticket_history')
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)

    class Meta:
        db_table = 'ticket'

    def __str__(self):
        return self.serial_no

    def delete(self):
        self.messages.all().delete()
        self.comments.all().delete()

        super().delete()

@receiver(pre_delete, sender=UpLoad)
def upload_pre_delete(sender, instance, **kwargs):
    
    if instance.file is not None: 
        instance.file.delete()

@receiver(post_save, sender=UpLoad)
def upload_post_save(sender, instance, **kwargs):
    
    object = instance.content_object
    
    if type(object) is Ticket:
        if object.type_status == 0:
            if object.normal_status != 4:
                object.normal_status = 5

        if object.type_status == 1:
            if object.change_status != 4:
                object.change_status = 5

        if object.type_status == 2:
            if object.cancel_status != 4:
                object.cancel_status = 5
        
        object.save()

@receiver(pre_delete, sender=Comment)
def comment_pre_delete(sender, instance, **kwargs):
    Comment.objects.filter(object_id=instance.id, content_type__model='comment').delete()

@receiver(post_save, sender=Comment)
def comment_post_save(sender, instance, **kwargs):

    #admin推送
    for user in User.objects.filter(Q(is_staff=True) & ~Q(id=instance.user.id)):
        if instance.content_type.model == 'ticket':
            Message.objects.create(json={'message': instance.content, 'model': 'Comment', 'id': instance.object_id}, content_object=instance.content_object, user=user)
        else:
            Message.objects.create(json={'message': instance.content, 'model': 'Comment', 'id': instance.content_object.object_id}, content_object=instance.content_object.content_object, user=user)
            
    message.send_admin_message.delay(instance.content, user.email)

    # for user in User.objects.filter(Q(is_staff=True) & ~Q(id=instance.user.id)):
    #     if instance.content_type == ContentType.objects.get_for_model(Ticket):
    #         Message.objects.create(json={'message': instance.content, 'model': 'Comment', 'id': instance.object_id}, content_object=instance.content_object, user=user)
    #     else:
    #         Message.objects.create(json={'message': instance.content, 'model': 'Comment', 'id': instance.content_object.object_id}, content_object=instance.content_object.content_object, user=user)

    # #客户推送
    # if instance.itinerary is not None and instance.itinerary.user is not None:
    #     Message.objects.create(json=serializer, content_object=instance, user=instance.itinerary.user)
    #     message.send_admin_message.delay('{user} {action} Ticket for ID: {id}'.format(user=history_instance.history_user, action=ActionString.get(history_instance.history_type), id=history_instance.id), instance.itinerary.user.email)