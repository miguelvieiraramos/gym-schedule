from rest_framework.views import exception_handler

from utils import ErrorsFormatter


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    # If an unexpected error occurs (server error, etc.)
    if response is None:
        return response

    formatter = ErrorsFormatter(exc)

    response.data = formatter()

    return response