from pprint import pprint
from collections import Counter
import time
import time
s="cbaebabacd"
p = "abc"
def print_iterator(it):
    for x in it:
        print(x, end=' ')
    print('')  # for new line
#299
# aa = "abcd"
# print(set(aa))

def getHint(secret, guess):
    dic_s, dic_g = {}, {}
    cnt_c, cnt_b = 0, 0
    for i, val in enumerate(secret):
        #val = int(val)
        if val == guess[i]:
            cnt_b +=1
        else:
            dic_s[val] = dic_s[val] + 1 if val in dic_s else 1
            dic_g[guess[i]] = dic_g[guess[i]] + 1 if guess[i] in dic_g else 1
    for key, val in dic_s.items():
        #key, val = int(key), int(val)
        if key in dic_g:
            cnt_c += val if val <= dic_g[key] else dic_g[key]
    return str(cnt_b) + "A" + str(cnt_c) + "B"


print(getHint("1123",'0111'))

def run_flow1(run_dir, flow_to_test, result_dir):
    os.chdir(run_dir)
    for flow_name in flow_to_test:
        # Reset DUT
        os.system("plink.exe -ssh -pw brcm1234 root@192.168.100.31 cd /root/Desktop/4378_FW/4378_18_10_336_REF; ./load_drv.sh;")
        time.sleep(40)
        # Remove old folders: Log and Result_LP before new test
        if os.path.isdir("Log"):
            shutil.rmtree("Log")
        if os.path.isdir("Result_LP"):
            shutil.rmtree("Result_LP")
        while True:
            if os.path.isdir("Log") or os.path.isdir("Result_LP"):
                time.wait(1)
            else:
                break
        run_cmd = ["IQfactRun_Console.exe", '-run', flow_name, "-repeat", "1", "-exit"]
        p = subprocess.Popen(run_cmd)
        if p.wait() != 0:
            print("RUN time error")
        test_time = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        test_time = "_".join(test_time.split())
        log_dir = os.path.join(result_dir, os.path.splitext(flow_name)[0], test_time)

        shutil.copytree("Log", os.path.join(log_dir, "Log"))
        shutil.copytree("Result_LP", os.path.join(log_dir, "Result_LP"))
        time.sleep(1) #TreeNode


st = "qa test on package 4.40.0.23"







def run_flow(run_dir, flow_to_test, result_dir):
    os.chdir(run_dir)
    for flow_name in flow_to_test:
        # Reset DUT
        os.system("plink.exe -ssh -pw brcm1234 root@192.168.100.31 cd /root/Desktop/4378_FW/4378_18_10_336_REF; ./load_drv.sh;")
        time.sleep(40)
        # Remove old folders: Log and Result_LP before new test
        if os.path.isdir("Log"):
            shutil.rmtree("Log")
        if os.path.isdir("Result_LP"):
            shutil.rmtree("Result_LP")
        while True:
            if os.path.isdir("Log") or os.path.isdir("Result_LP"):
                time.wait(1)
            else:
                break
        run_cmd = ["IQfactRun_Console.exe", '-run', flow_name, "-repeat", "1", "-exit"]
        p = subprocess.Popen(run_cmd)
        if p.wait() != 0:
            print("RUN time error")
        test_time = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        test_time = "_".join(test_time.split())
        log_dir = os.path.join(result_dir, os.path.splitext(flow_name)[0], test_time)

        shutil.copytree("Log", os.path.join(log_dir, "Log"))
        shutil.copytree("Result_LP", os.path.join(log_dir, "Result_LP"))
        time.sleep(1) #TreeNode
from collections import deque, Counter
from pprint import pprint
#815
def numBus(routes S, T):

def run_flow(run_dir, flow_to_test, result_dir):
    os.chdir(run_dir)
    for flow_name in flow_to_test:
        # Reset DUT
        os.system("plink.exe -ssh -pw brcm1234 root@192.168.100.31 cd /root/Desktop/4378_FW/4378_18_10_336_REF; ./load_drv.sh;")
        time.sleep(40)
        # Remove old folders: Log and Result_LP before new test
        if os.path.isdir("Log"):
            shutil.rmtree("Log")
        if os.path.isdir("Result_LP"):
            shutil.rmtree("Result_LP")
        while True:
            if os.path.isdir("Log") or os.path.isdir("Result_LP"):
                time.wait(1)
            else:
                break
        run_cmd = ["IQfactRun_Console.exe", '-run', flow_name, "-repeat", "1", "-exit"]
        p = subprocess.Popen(run_cmd)
        if p.wait() != 0:
            print("RUN time error")
        test_time = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        test_time = "_".join(test_time.split())
        log_dir = os.path.join(result_dir, os.path.splitext(flow_name)[0], test_time)

        shutil.copytree("Log", os.path.join(log_dir, "Log"))
        shutil.copytree("Result_LP", os.path.join(log_dir, "Result_LP"))
        time.sleep(1) #TreeNode

def copy_setup_file(run_dir, setupfile_loc):
    for setup_file in os.listdir(setupfile_loc):
        src = os.path.join(setupfile_loc, setup_file)
        shutil.copy2(src, run_dir)


def copy_flows(run_dir, flow_to_test, flowfile_loc ):
    for flow_name in os.listdir(flowfile_loc):
        #flow_name = os.path.split(flow_name)[-1]
        flow_name  = flow_name.split("\\")[-1]
        src = os.path.join(flowfile_loc, flow_name)
        shutil.copy2(src, run_dir)
        flow_to_test.append(flow_name)

##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
class User(models.Model):
 name = models.CharField(max_length=255)
 surname = models.CharField(max_length=255)
class Invoice(models.Model):
 user = models.ForeignKey(User)
 number = models.CharField(max_length=25)

class testUser(models.Model):
    testName = models.CharField(max_length=255)
    testuser = models.ForeignKey()

#list of json object,
# json object, enclosed with {}
# array of json 2 objects
family = [{
    "name" : "Jason",
    "age" : "24",
    "gender" : "male"
},
{
    "name" : "Kyle",
    "age" : "21",
    "gender" : "male"
}];

#nest json objects
testtest={
    "jason" : {
        "name" : "Jason Lengstorf",
        "age" : "24",
        "gender" : "male"
    },
    "kyle" : {
        "name" : "Kyle Lengstorf",
        "age" : "21",
        "gender" : "male"
    }
}

from rest_framework import serializers
from main.models import Cat, Dog

class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = (‘owner ‘ , ‘ name ‘ , ‘ birthday ‘ )
        read_only_fields = ( ‘ owner ‘ ,)
class CatSerializer(serializers.ModelSerializer):
 class Meta:
    model = Cat
    fields = (‘owner‘, ‘name‘, ‘birthday‘)
    read_only_fields = (‘owner‘,)
## viewset
from rest_framework import viewsets, permissions
from main.models import Cat, Dog
from .permissions import IsOwnerOrReadOnly
from .serializers import CatSerializer, DogSerializer
# Create your views here.
class BaseViewSet ( viewsets . ModelViewSet ):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
def get_queryset(self):
    qs = self.queryset.filter(owner=self.request.user)
    return qs
def perform_create(self, serializer):
    serializer.save(owner = self.request.user)
class DogViewSet(BaseViewSet):
    serializer_class = DogSerializer
    queryset = Dog.objects.all ()
class CatViewSet(BaseViewSet):
    serializer_class = CatSerializer
    queryset = Cat.objects.all ()

class BaseViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    def get_queryset(self):
        qs = self.queryset.filter()

####
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .permissions import IsOwnerOrReadOnly
from .models import Dog


class DogFeedView(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (IsOwnerOrReadOnly,)

    def get(self, request, pk=None):
        dog = get_object_or_404(Dog, pk=pk)
        dog.feed()
        return Response({“msg“: “Dog
        fed“, status = status.HTTP_200_OK})
###
        from rest_framework import routers
        from .views import DogViewSet, CatViewSet, DogFeedView
        router = routers.DefaultRouter(trailing_slash=False)
        router.register(‘dogs‘, DogViewSet)
        router.register(‘cats‘, CatViewSet)
        urlpatterns = router.urls
        urlpatterns + = [
            url(r‘dogs / (?P < pk >[\d]+) / feed /$‘, DogFeedView.as_view(), name = dogfeed)
        ]
## renderer
        …
        (… other definition code)
        from rest_framework import renderers
        from rest_framework_xml.renderers import XMLRenderer

    class DogFeedView(APIView):
        renderer_classes = (renderers.TemplateHTMLRenderer, renderers.JSONRenderer, XMLRenderer)
        (other definition code …)

    …
##
    class ImageRenderer(renderers.BaseRenderer):
        media_type = 'image/png'
        format = 'image'

        def render(self, data, media_type=None, renderer_context=None):
            return data

            # view class

    class ShowImage(APIView):
        renderer_classes = (ImageRenderer,)

        def get(self, request, format=None):
            print('format', format)
            if format == 'image':
                image_file = open('path_to_image', 'rb')
                response = HttpResponse(image_file, content_type='image/png')
                response['Content-Disposition'] = 'attachment; filename={}'.format('image_filename')

    # urls.py
    urlpatterns = format_suffix_patterns([
        url(r'image/?$', views.ShowImage.as_view())
    ])
