from django.core.validators import ValidationError
from django.utils.deconstruct import deconstructible
from django.utils.translation import ugettext_lazy as _


@deconstructible
class FileTypeValidator(object):
    """
    Validates that an uploaded file has an allowed extension.

    It **does not** validate the actual file content and *should not* be
    considered secure.
    """
    message = _('Files of type "%(invalid_type)s" are not allowed.')
    code = 'invalid_type'

    def __init__(self, valid_types, message=None, code=None):
        self.valid_types = valid_types
        if message is not None:
            self.message = message
        if code is not None:
            self.code = code

    def __call__(self, value):
        extension = value.name.split('.').pop(-1)
        if not extension in self.valid_types:
            raise ValidationError(self.message, code=self.code,
                                  params={'invalid_type': extension})

    def __eq__(self, other):
        return (
            isinstance(other, FileTypeValidator) and
            self.message == other.message and
            (self.code == other.code)
        )

    def __ne__(self, other):
        return not (self == other)