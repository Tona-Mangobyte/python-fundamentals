# Mixins
# Mixins are a way to add functionality to classes in a modular way.
# They are a form of multiple inheritance, but they are not meant to stand on their own.
# They are meant to be added to classes to add functionality.
# They are a way to make classes more modular and easier to read.
# They are a way to avoid code duplication.
# They are a way to make classes more flexible.
# They are a way to make classes more reusable.
# They are a way to make classes more testable.
# They are a way to make classes more maintainable.
# They are a way to make classes more scalable.
# They are a way to make classes more extensible.
# They are a way to make classes more composable.
# They are a way to make classes more decoupled.
# They are a way to make classes more cohesive.
# They are a way to make classes more readable.
# They are a way to make classes more understandable.
# They are a way to make classes more maintainable.

class Mixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.mixin = True

    def mixin_method(self):
        return "Mixin method"

class Base:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.base = True

    def base_method(self):
        return "Base method"

class Derived(Base, Mixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.derived = True

    def derived_method(self):
        return "Derived method"

# Usage
d = Derived()
print(d.base_method()) # Base method
print(d.mixin_method()) # Mixin method
print(d.derived_method()) # Derived method
print(d.base) # True
print(d.mixin) # True
print(d.derived) # True

