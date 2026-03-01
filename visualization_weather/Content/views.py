from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from Content.COSUploadUtils import upload_service
from Content.migrations.service import userService, contentService, \
    imageService, noticeService, recordService, classificationService


@csrf_exempt
def image_upload(request):
    return upload_service(request)


@csrf_exempt
@require_http_methods(["POST"])
def image_upload_base64(request):
    return imageService.image_upload_base64(request)


# Create your views here.
@csrf_exempt
def validate(request):
    return userService.validate_service(request)


@csrf_exempt
def register(request):
    return userService.register_service(request)


@csrf_exempt
def user_list(request):
    return userService.user_list_service(request)


@csrf_exempt
def user_add(request):
    return userService.user_add_service(request)


@csrf_exempt
def user_modify(request):
    return userService.user_modify_service(request)

@csrf_exempt
def user_reset(request):
    return userService.user_reset_service(request)

@csrf_exempt
def user_delete(request):
    return userService.user_delete_service(request)


def user_detail(request):
    return userService.user_detail_service(request)


@csrf_exempt
def user_currentUser(request):
    return userService.user_currentUser_service(request)

@csrf_exempt
def content_list(request):
    return contentService.content_list_service(request)

@csrf_exempt
def content_add(request):
    return contentService.content_add_service(request)

@csrf_exempt
def content_generate(request):
    return contentService.content_generate_service(request)

@csrf_exempt
def content_modify(request):
    return contentService.content_modify_service(request)


@csrf_exempt
def content_delete(request):
    return contentService.content_delete_service(request)

@csrf_exempt
def content_detail(request):
    return contentService.content_detail_service(request)


@csrf_exempt
def classification_list(request):
    return classificationService.classification_list_service(request)

@csrf_exempt
def classification_add(request):
    return classificationService.classification_add_service(request)


@csrf_exempt
def classification_modify(request):
    return classificationService.classification_modify_service(request)


@csrf_exempt
def classification_delete(request):
    return classificationService.classification_delete_service(request)

@csrf_exempt
def classification_detail(request):
    return classificationService.classification_detail_service(request)


@csrf_exempt
def notice_list(request):
    return noticeService.notice_list_service(request)

@csrf_exempt
def notice_add(request):
    return noticeService.notice_add_service(request)


@csrf_exempt
def notice_modify(request):
    return noticeService.notice_modify_service(request)


@csrf_exempt
def notice_delete(request):
    return noticeService.notice_delete_service(request)

@csrf_exempt
def notice_detail(request):
    return noticeService.notice_detail_service(request)

@csrf_exempt
def record_list(request):
    return recordService.record_list_service(request)

@csrf_exempt
def record_add(request):
    return recordService.record_add_service(request)


@csrf_exempt
def record_modify(request):
    return recordService.record_modify_service(request)


@csrf_exempt
def record_delete(request):
    return recordService.record_delete_service(request)

@csrf_exempt
def record_detail(request):
    return recordService.record_detail_service(request)



