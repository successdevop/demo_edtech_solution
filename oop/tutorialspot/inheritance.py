class Division:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def divide(self):
        return self.a / self.b


class Modulus:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def mod_divide(self):
        return self.a % self.b


class DivMod(Division, Modulus):
    def __init__(self, a, b):
        super().__init__(a, b)
        self.a = a
        self.b = b

    def div_and_mod(self):
        div_val = Division.divide(self)
        mod_val = Modulus.mod_divide(self)
        return div_val, mod_val

#
# div = Division(5,6)
# mod = Modulus(10, 3)

div_mod = DivMod(14, 4)

print("Division: ", div_mod.divide())
print("Modulus: ", div_mod.mod_divide())
print("DivMod: ", div_mod.div_and_mod())
