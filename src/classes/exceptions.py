class NullException(Exception):
    def __str__(self):
        return f"Значение не может равняться None!"
