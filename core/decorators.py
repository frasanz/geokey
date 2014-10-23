from django.core.exceptions import PermissionDenied, ValidationError

from rest_framework import status
from rest_framework.response import Response

from core.exceptions import MalformedRequestData, Unauthenticated
from projects.models import Project
from users.models import User, UserGroup, ViewUserGroup
from observationtypes.models import (
    ObservationType, Field, LookupValue, MultipleLookupValue
)
from dataviews.models import View, Rule
from applications.models import Application
from contributions.models import Observation, Location, Comment


def handle_exceptions_for_admin(func):
    def wrapped(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except PermissionDenied, error:
            return {
                "error_description": str(error),
                "error": "Permission denied."
            }
        except (
            Project.DoesNotExist,
            ObservationType.DoesNotExist,
            Field.DoesNotExist,
            View.DoesNotExist,
            Rule.DoesNotExist,
            Application.DoesNotExist
        ) as error:
            return {"error_description": str(error), "error": "Not found."}

    return wrapped


def handle_exceptions_for_ajax(func):
    def wrapped(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Unauthenticated, error:
            return Response(
                {"error": str(error)},
                status=status.HTTP_401_UNAUTHORIZED
            )
        except PermissionDenied, error:
            return Response(
                {"error": str(error)},
                status=status.HTTP_403_FORBIDDEN
            )
        except ValidationError, error:
            return Response(
                {"error": error.messages},
                status=status.HTTP_400_BAD_REQUEST
            )
        except (MalformedRequestData, TypeError), error:
            return Response(
                {"error": str(error)},
                status=status.HTTP_400_BAD_REQUEST
            )
        except (
            Project.DoesNotExist,
            UserGroup.DoesNotExist,
            ViewUserGroup.DoesNotExist,
            User.DoesNotExist,
            ObservationType.DoesNotExist,
            Field.DoesNotExist,
            MultipleLookupValue.DoesNotExist,
            LookupValue.DoesNotExist,
            View.DoesNotExist,
            Application.DoesNotExist,
            Observation.DoesNotExist,
            Location.DoesNotExist,
            Comment.DoesNotExist
        ) as error:
            return Response(
                {"error": str(error)},
                status=status.HTTP_404_NOT_FOUND
            )

    return wrapped
