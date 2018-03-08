class DriverNotFound(Exception):
    pass


class DriverLibraryNotFound(Exception):
    pass


class FileTypeException(Exception):
    """
    For exceptions extension invalid
    """
    pass


class RequiredContainerBindingNotFound(Exception):
    pass


class MissingContainerBindingNotFound(Exception):
    pass


class InvalidCSRFToken(Exception):
    """
    For exceptions that return error when verifying the csrf token
    """
    pass
