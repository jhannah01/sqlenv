class SqlBaseError(Exception):
    '''General error in SqlBase'''

    def __init__(self, message, base_ex=None, ext_values={}):
        self._message = message
        self._base_ex = base_ex
        self._ext_values = ext_values

    @property
    def message(self):
        return self._message

    @property
    def has_base_ex(self):
        return (hasattr(self, '_base_ex') and self._base_ex)

    @property
    def base_ex(self):
        return self._base_ex

    @property
    def has_ext_values(self):
        return (hasattr(self, '_ext_values') and self._ext_values)

    @property
    def ext_values(self):
        return self._ext_values

__all__ = ['SqlBaseError']
