vz = int(input('Quantos Métodos: '))

for i in range(vz):
    print('\n')
    x = input()
    print(
        "    def set{}(self, {}):\n"
        "        self.__{} = {}\n"
        "    def get{}(self):\n"
        "        return self.__{}\n"
        "    {} = property(get{}, set{})".format(x.capitalize(),x,x,x,x.capitalize(),x,x,x.capitalize(),x.capitalize())
    )
    print('\n')