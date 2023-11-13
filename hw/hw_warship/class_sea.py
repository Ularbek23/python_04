class Sea:
    def __init__(self, field_size):
        field = [[' ' for j in range(field_size)] for i in range(field_size)]
        self.field = field