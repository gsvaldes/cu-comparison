from django.db import models

BUSINESS_TYPE = (
    ('CU', 'Credit Union'),
    ('CC', 'Check Cashing'),
)


class Business(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    business_name = models.CharField(max_length=100, unique=True)
    link = models.URLField()
    business_type = models.CharField(max_length=2, choices=BUSINESS_TYPE)

    def __unicode__(self):
        return u'%s' % self.business_name


class Location(models.Model):
    business = models.ForeignKey(Business, verbose_name='business')
    address = models.CharField(max_length=255, default='')
    city = models.CharField(max_length=100, default='Austin')
    state = models.CharField(max_length=100, default='Texas')
    zip_code = models.CharField(max_length=5, default='')
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "{0}  {1}".format(self.address, self.zip_code)
