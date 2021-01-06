# from .forms import uploadForm
from rest_framework import status
from rest_framework.response import Response
from .serializers import UploadSerializer
from rest_framework.views import APIView
from PIL import Image
import requests
from io import BytesIO


class FileUploadView(APIView):
    serializer_class = UploadSerializer

    def get_queryset(self, request):
        url = self.kwargs['src']
        img = Image.open(BytesIO(requests.get(url).content))

        print()
        dom_color = img.getcolors(img.size[0]*img.size[1])[1][1]
        ans = {}

        ans['logo_border'] = '#%02x%02x%02x' % tuple(img.load()[0, 0])[: -1]
        ans['dominant_color'] = '#%02x%02x%02x' % dom_color[:-1]

        return Response(ans, status.HTTP_201_CREATED)
