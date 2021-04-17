from django.test import TestCase
from calculo.models import Segment

# Create your tests here.
class SegmentTestCase(TestCase):
    def setUp(self):
        Segment.objects.create(_id=1,length=10,height=4,horizontaltube=8,gatecount=2)
    
    def test_object_created(self):
        segment = Segment.objects.get(_id=1)
        self.assertEqual(segment.length,10)
        self.assertEqual(segment.height,4)
        self.assertEqual(segment.horizontaltube,8)
        self.assertEqual(segment.gatecount,2)