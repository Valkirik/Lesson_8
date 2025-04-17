class Triangle:
    def __init__(self, sides):
        self.sides = sides

    def __str__(self):
        return f"{self.sides}"
    
    def to_build(self):
        l = list(sorted(self.sides))
        l.pop()
        num_str = list(map(lambda x: str(x), self.sides))

        if sum(l) > max(self.sides):
            return f"a triangle with sides: {", ".join(num_str)} is possible to build"
        else:
            return f"a triangle with sides: {" ".join(num_str)} is not possible to build"
        
        

triangle_1 = Triangle([2, 6, 6])
print(triangle_1.to_build())

