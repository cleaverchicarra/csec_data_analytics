from rest_framework_mongoengine import serializers as mongoserializers

from csec_data_analytics_app.models import Vulnerability

class CVEItem(models.Model):
    id = models.CharField(max_length=255)
    sourceIdentifier = models.CharField(max_length=255)
    vulnStatus = models.CharField(max_length=255)
    published = models.DateTimeField()
    lastModified = models.DateTimeField()
    evaluatorComment = models.TextField()
    evaluatorSolution = models.TextField()
    evaluatorImpact = models.TextField()
    cisaExploitAdd = models.DateField()
    cisaActionDue = models.DateField()
    cisaRequiredAction = models.TextField()

    class Description(models.Model):
        lang = models.CharField(max_length=10)
        value = models.TextField()

    descriptions = models.ManyToManyField(Description)

    class CPEMatch(models.Model):
        vulnerable = models.BooleanField()
        criteria = models.CharField(max_length=255)
        matchCriteriaId = models.UUIDField()
        versionStartExcluding = models.CharField(max_length=255)
        versionStartIncluding = models.CharField(max_length=255)
        versionEndExcluding = models.CharField(max_length=255)
        versionEndIncluding = models.CharField(max_length=255)

class NVDAPIv2(models.Model):
    resultsPerPage = models.IntegerField()
    startIndex = models.IntegerField()
    totalResults = models.IntegerField()
    format = models.CharField(max_length=255)
    version = models.CharField(max_length=255)
    timestamp = models.DateTimeField()
    vulnerabilities = models.ManyToManyField(CVEItem)
