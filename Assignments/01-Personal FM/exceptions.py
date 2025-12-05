class FinanceError(Exception):
    """Base class for other exceptions"""
    pass

class ValidationError(FinanceError):
    """Raised when input validation fails"""
    pass

class NotFoundError(FinanceError):
    """Raised when an item is not found"""
    pass

class StorageError(FinanceError):
    """Raised when the file I/O fails"""
    pass