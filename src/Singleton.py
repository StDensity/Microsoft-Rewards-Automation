class Singleton:

    def __init__(self, cls):
        """
            Initialize the singleton class
            :param cls: cls is passed automatically while calling the decorator
        """
        self._cls = cls

    def instance(self):
        try:
            a = self._instance
            print("*" * 10, "reusing singleton value for :", self._cls.__name__)
            return a
        except AttributeError:
            # If no instance exists, create a new one
            print("*" * 10, "Creating new singleton value for ", self._cls.__name__)
            self._instance = self._cls()
            return self._instance

    def __call__(self):
        # Raise a TypeError if the singleton is accessed directly instead of through 'Instance()' method
        raise TypeError("Singleton should be accessed through 'instance()' method.")