class Settings:
    allowed_methods = ["@"]
    ignorable_lines = ["\n", ""]

    @classmethod
    def update_allowed_methods(cls, methods):
        cls.allowed_methods = methods

    @classmethod
    def update_ignorable_lines(cls, lines):
        cls.ignorable_lines = lines
