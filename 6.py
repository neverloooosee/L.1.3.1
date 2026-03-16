import math

class Triangle:
    def __init__(self, a, b, c): self.a, self.b, self.c = a, b, c
    def p(self): return self.a + self.b + self.c
    def s(self):
        m = self.p() / 2
        return math.sqrt(max(0, m * (m - self.a) * (m - self.b) * (m - self.c)))
    def __str__(self): return f"Triangle({self.a}, {self.b}, {self.c})"

class Rectangle:
    def __init__(self, a, b): self.a, self.b = a, b
    def p(self): return 2 * (self.a + self.b)
    def s(self): return self.a * self.b
    def __str__(self): return f"Rectangle({self.a}, {self.b})"

class Trapeze:
    def __init__(self, a, b, c, d): self.a, self.b, self.c, self.d = a, b, c, d
    def p(self): return self.a + self.b + self.c + self.d
    def s(self):
        if self.b == self.a: return 0
        h = math.sqrt(max(0, self.c**2 - (((self.b - self.a)**2 + self.c**2 - self.d**2) / (2 * (self.b - self.a)))**2))
        return ((self.a + self.b) / 2) * h
    def __str__(self): return f"Trapeze({self.a}, {self.b}, {self.c}, {self.d})"

class Parallelogram:
    def __init__(self, a, b, h): self.a, self.b, self.h = a, b, h
    def p(self): return 2 * (self.a + self.b)
    def s(self): return self.a * self.h
    def __str__(self): return f"Parallelogram({self.a}, {self.b}, {self.h})"

class Circle:
    def __init__(self, r): self.r = r
    def p(self): return 2 * math.pi * self.r
    def s(self): return math.pi * self.r**2
    def __str__(self): return f"Circle({self.r})"

figs = []
with open('input01.txt', 'r') as f:
    for line in f:
        p = line.split()
        if not p: continue
        t, v = p[0], [float(x) for x in p[1:]]
        if t == 'Triangle': figs.append(Triangle(*v))
        elif t == 'Rectangle': figs.append(Rectangle(*v))
        elif t == 'Trapeze': figs.append(Trapeze(*v))
        elif t == 'Parallelogram': figs.append(Parallelogram(*v))
        elif t == 'Circle': figs.append(Circle(*v))

if figs:
    max_s = max(figs, key=lambda x: x.s())
    max_p = max(figs, key=lambda x: x.p())
    print(f"Max S: {max_s.__class__.__name__} {max_s}, S={max_s.s():.2f}")
    print(f"Max P: {max_p.__class__.__name__} {max_p}, P={max_p.p():.2f}")
