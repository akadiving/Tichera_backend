from rest_framework import generics, permissions, filters
from courses.models import Course, Review
from .serializers import CourseSerializer, ReviewSerializer
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated, \
    IsAuthenticatedOrReadOnly, \
    BasePermission, DjangoModelPermissions, AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser

# Create your views here.

class IsOwner(BasePermission):
    message = 'Editing is restricted to owner only.'

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True

        return obj.owner == request.user

class ReviewList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()

class ReviewCreate(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView, IsOwner):
    permission_classes = [IsOwner]
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()

class CourseList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

'''class CourseDetail(generics.RetrieveUpdateDestroyAPIView, CourseUserAdd):

    serializer_class = CourseSerializer

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Course, slug=item)'''

class CourseListDetailfilter(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^slug']

    # '^' Starts-with search.
    # '=' Exact matches.
    # '@' Full-text search. (Currently only supported Django's PostgreSQL backend.)
    # '$' Regex search.

class CreateCourse(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CourseSerializer
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, format=None):
        print(request.data)
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

'''
class AdminCourseDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class EditCourse(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

class DeleteCourse(generics.RetrieveDestroyAPIView, CourseUserAdd):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class CourseSearch(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^slug']



class CourseList(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissions]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

'''

class CourseDetail(generics.RetrieveUpdateDestroyAPIView, IsOwner):
    permission_classes = [IsOwner]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
