print("##########################")
print("        creacion        ")
a=dict()
b={}
c=dict(x=1)
d=dict(a=1,b=2,d=3)
e={1:"hola","a":"mundo"}
f=dict({"b":2})
g=dict(zip("p","q"))
h={1:"marco",2:"oscar",3:"maria"}
i={"hola":1,"como":2,"estas":3}
j=dict(zip("fruta","mandarina"))
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)
print(j)
print("###################################")
print("     pertenecia de clave      ")
a=dict(x=1)
b=dict(a=1,b=2,d=3)
c={1:"hola","a":"mundo"}
d=dict({"b":2})
e=dict(zip("p","q"))
f=dict(zip("mandarina","redonda"))
g={1:2,3:4,44:5}
h={"q":range(1,3)}
i=dict(hola=2,tengas=1)
j=dict(a=12,b=234,hola=23)
print("x" in a)
print(1 not in b)
print("hola" in c)
print("b"not in d)
print("p"in e)
print("m"in f)
print(1 not in g)
print("q"in g)
print("hola" in i)
print("s"in h)
print("###########################################")
print("            comparacion                    ")
a=dict(x=1)
b=dict(x=1)
c=dict(a=1,b=2,d=3)
d=dict(a=1,b=2,d=3)
e={1:"hola","a":"mundo"}
f={1:"hola","a":"mundo"}
g=dict({"b":2})
h=dict(zip("p","q"))
i=dict({"b":2})
j=dict(zip("p","q"))
print(a==j)
print(a!=e)
print(c==d)
print(d==e)
print(a!=f)
print(j==i)
print(g!=j)
print(d!=c)
print(e==f)
print(a!=b)
print(d!=j)
print("######################################")
print("        indexacion                    ")
a= {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
b= {'Plátano':1.35, 'Manzana':0.8, 'Pera':0.85, 'Naranja':0.7}
c=dict(x=1)
d=dict(a=1,b=2,d=3)
e={1:"lunes",2:"martes",3:"miercoles",4:"jueves",5:"viernes"}
f={1:"enero",2:"febrero",3:"marzo",4:"abril",5:"mayo",6:"junio"}
g=dict(zip("p","q"))
h={1:"marco",2:"oscar",3:"maria"}
i={"hola":1,"como":2,"estas":3}
j=dict(zip("fruta","mandarina"))
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)
print(j)

print("######################################")
print("               longitud               ")
a=dict(x=1)
b=dict(a=1,b=2,d=3)
c={1:"hola","a":"mundo"}
d=dict({"b":2})
e=dict(zip("p","q"))
f=dict(zip("mandarina","redonda"))
g={1:2,3:4,44:5}
h=dict(mandarina="anaranjado",mango="amarillo")
i=dict(zip("a","b"))
j=dict(zip("fruta","mandarina"))
print(len(a))
print(len(b))
print(len(c))
print(len(d))
print(len(e))
print(len(f))
print(len(g))
print(len(h))
print(len(i))
print(len(j))
print("#########################################")
print("          iteracion                      ")
a = {
    "blue" : "5",
    "red" : "6",
    "yellow" : "8",}
b=versiones = dict(python=2.7, zope=2.13, plone=5.1, django=2.1)
c={    "clave1":234,"clave2":True,"clave3":"Valor 1"}
d={"lima":"peru","chile":"santiago de chile","brasil":"brasilia"}
e={1:"lunes",2:"martes",3:"miercoles",4:"jueves",5:"viernes"}
f={1:"enero",2:"febrero",3:"marzo",4:"abril",5:"mayo",6:"junio"}
g=dict(zip("p","q"))
h={1:"marco",2:"oscar",3:"maria"}
i={"hola":1,"como":2,"estas":3}
j=dict(zip("fruta","mandarina"))
for k,j in j.items():
    print(k,j)
for k,a in a.items():
    print(k, a)
for k, b in b.items():
    print(k, b)
for k, c in c.items():
    print(k, c)
for k, d in d.items():
    print(k, d)
for k, e in e.items():
    print(k, e)
for k, f in f.items():
    print(k, f)
for k, g in g.items():
    print(k, g)
for k, h in h.items():
    print(k, h)
for k, i in i.items():
    print(k, i)
print("####################################")
print("            busquedad               ")
a = {
    "blue" : "5",
    "red" : "6",
    "yellow" : "8",}

b= {    "clave1":234,"clave2":True,"clave3":"Valor 1"}
d={"lima":"peru","chile":"santiago de chile","brasil":"brasilia"}
e={1:"lunes",2:"martes",3:"miercoles",4:"jueves",5:"viernes"}
f=dict({"b":2})
g=dict(zip("p","q"))
h={1:"marco",2:"oscar",3:"maria"}
i={"hola":1,"como":2,"estas":3}
j=dict(zip("fruta","mandarina"))
print(a.get("blue"))
print(b.get("clave1"))

print(d.get("lima"))
print(e.get(3))
print(f.get("b"))
print(g.get("p"))
print(h.get(1))
print(i.get("hola"))
print(j.get("f"))
print("###########################################")
print("            eleminacion                    ")
a = {
    "blue" : "5",
    "red" : "6",
    "yellow" : "8",}
b= {    "clave1":234,"clave2":True,"clave3":"Valor 1"}
d={"lima":"peru","chile":"santiago de chile","brasil":"brasilia"}
e={1:"marte",2:"jupiter",3:"saturno",4:"pluton"}
f={9:"guerrero",10:"farfan"}
g=dict(zip("p","q"))
h={1:"marco",2:"oscar",3:"maria"}
i={"hola":1,"como":2,"estas":3}
j=dict(a=1,b=2,d=3)
del a["blue"]
print(a)
del b["clave3"]
print(b)
del d["lima"]
print(d)
del e[1]
print(e)
del f[10]
del g["p"]
print(g)
del h[2]
print(h)
del i["hola"]
print(i)
del j["d"]
print(j)
print("#########################################")
print("                   reemplazo             ")
a=dict(a=1,b=2,c=3,d=4)
b= {    "clave1":234,"clave2":True,"clave3":"Valor 1"}
c={1:"mango",2:"fresa",3:"uva",4:"sandia"}
d={"lima":"peru","chile":"santiago de chile","brasil":"brasilia"}
e={1:"lunes",2:"martes",3:"miercoles",4:"jueves",5:"viernes"}
f=dict({"b":2})
g=dict(zip("p","q"))
h={"q":range(1,3)}
i=dict(hola=2,tengas=1)
j=dict(a=12,b=234,hola=23)
a["a"]="hola"
print(a)
b["clave1"]="mundo"
print(b)
c[1]="higo"
print(b)
d["lima"]="cusco"
print(d)
e[1]="domingo"
print(e)
f["b"]="mundo"
print(f)
g["p"]="a"
print(g)
h["q"]="programacion 2"
print(h)
i["hola"]=6
print(i)
j["a"]=2334
print(j)
print("#####################################")
print("            agregado                 ")
a = {
    "blue" : "5",
    "red" : "6",
    "yellow" : "8",}
b= {    "clave1":234,"clave2":True,"clave3":"Valor 1"}
c={1:"mango",2:"fresa",3:"uva",4:"sandia"}
d={"lima":"peru","chile":"santiago de chile","brasil":"brasilia"}
e={1:"marte",2:"jupiter",3:"saturno",4:"pluton"}
f={9:"guerrero",10:"farfan"}
g=dict(zip("p","q"))
h={1:"marco",2:"oscar",3:"maria"}
i={"hola":1,"como":2,"estas":3}
j=dict(a=1,b=2,d=3)
a.setdefault(1,5)
print(a)
b.setdefault("italia","roma")
print(b)
c.setdefault(5,"naranja")
print(c)
d.setdefault("italia","roma")
print(d)
e.setdefault(5,"planetas")
print(e)
f.setdefault(20,"flores")
print(f)
g.setdefault("s","eres")
print(g)
h.setdefault(4,"camila")
print(h)
i.setdefault("dia",5)
print(i)
j.setdefault("e",3444)
print(j)
print("########################################")
print("               clonado                  ")
a=dict(x=1)
b=dict(a=1,b=2,d=3)
c={1:"hola","a":"mundo"}
d=dict({"b":2})
e={1:"marte",2:"jupiter",3:"saturno",4:"pluton"}
f={9:"guerrero",10:"farfan"}
g=dict(zip("p","q"))
h={1:"marco",2:"oscar",3:"maria"}
i={"hola":1,"como":2,"estas":3}
j=dict(a=1,b=2,d=3)
a.clear()
print(a)
b.clear()
print(b)
c.clear()
print(c)
d.clear()
print(d)
e.clear()
print(e)
f.clear()
print(f)
g.clear()
print(g)
h.clear()
print(h)
i.clear()
print(i)
j.clear()
print(j)
print("#########################################")
print("             clonado                     ")
a=dict()
b={}
c=dict(x=1)
d=dict(a=1,b=2,d=3)
e={1:"hola","a":"mundo"}
f=dict({"b":2})
g=dict(zip("p","q"))
h={"q":range(1,3)}
i=dict(hola=2,tengas=1)
j=dict(a=12,b=234,hola=23)
x=a.copy()
print(x)
y=b.copy()
print(y)
z=c.copy()
print(z)
w=d.copy()
print(w)
v=e.copy()
print(v)
u=f.copy()
print(u)
t=g.copy()
print(t)
k=h.copy()
print(k)
l=i.copy()
print(l)
m=j.copy()
print(m)
print("##########################################")
print("                 insercion              ")
a= {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
b= {'Plátano':1.35, 'Manzana':0.8, 'Pera':0.85, 'Naranja':0.7}
c= {1:'enero', 2:'febrero', 3:'marzo', 4:'abril', 5:'mayo', 6:'junio', 7:'julio',
          8:'agosto', 9:'septiembre', 10:'octubre', 11:'noviembre', 12:'diciembre'}
d={'Matemáticas': 6, 'Física': 4, 'Química': 5}
e= {'que': 2, 'lindo': 3, 'día': 1, 'hace': 4, 'hoy': 5}
f=dict({"b":2})
g=dict(zip("p","q"))
h={"q":range(1,3)}
i=dict(hola=2,tengas=1)
j=dict(a=12,b=234,hola=23)
a["euro"]="estados unidos"
b["naranja"]=3.50
c[13]="meses"
d[8]="algebra"
e[6]="lunes"
f["c"]=3
g["r"]="a"
h["a"]="hola"
i[3]="tengas"
j["c"]=1223456
print(a)
print(b)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)
print(j)
print("###########################################")
print("                  extraccion               ")
a = {
    "blue" : "5",
    "red" : "6",
    "yellow" : "8",}
b= {    "clave1":234,"clave2":True,"clave3":"Valor 1"}
c={1:"mango",2:"fresa",3:"uva",4:"sandia"}
d={"lima":"peru","chile":"santiago de chile","brasil":"brasilia"}
e={1:"marte",2:"jupiter",3:"saturno",4:"pluton"}
f=dict({"b":2})
g=dict(zip("p","q"))
h={1:"marco",2:"oscar",3:"maria"}
i={"hola":1,"como":2,"estas":3}
j=dict(zip("fruta","mandarina"))
k=a.pop("blue")
l=b.pop("clave2")
m=c.pop(3)
n=d.popitem()
o=e.pop(5,"planetas")
p=f.popitem()
q=g.popitem()
r=h.pop(2)
s=i.pop("hola")
t=j.popitem()
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)
print(j)
print("#######################################")
print(               "ver claves"              )
a=dict(x=1)
b=dict(a=1,b=2,d=3)
c={1:"hola","a":"mundo"}
d=dict({"b":2})
e={1:"marte",2:"jupiter",3:"saturno",4:"pluton"}
f={9:"guerrero",10:"farfan"}
g=dict(zip("p","q"))
h={1:"marco",2:"oscar",3:"maria"}
i={"hola":1,"como":2,"estas":3}
j=dict(a=1,b=2,d=3)
a.keys()
b.keys()
c.keys()
d.keys()
e.keys()
f.keys()
g.keys()
h.keys()
i.keys()
j.keys()
print(a)
print(b)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)
print(j)
print("########################################")
print("                ver valores       ")
a = {
    "blue" : "5",
    "red" : "6",
    "yellow" : "8",}
b= {    "clave1":234,"clave2":True,"clave3":"Valor 1"}
d={"lima":"peru","chile":"santiago de chile","brasil":"brasilia"}
e={1:"marte",2:"jupiter",3:"saturno",4:"pluton"}
f={1:"hola","a":"mundo"}
g=dict({"b":2})
h=dict(zip("p","q"))
i=dict({"b":2})
j=dict(zip("p","q"))
a.values()
b.values()
d.values()
e.values()
f.values()
g.values()
h.values()
c.values()
i.values()
j.values()
print(a)
print(b)
print(d)
print(f)
print(g)
print(h)
print(i)
print(j)
print(c)
print(e)
print("#############################################3")
print("                   conversion                 ")
a= {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
b= {'Plátano':1.35, 'Manzana':0.8, 'Pera':0.85, 'Naranja':0.7}
c=dict(x=1)
d=dict(a=1,b=2,d=3)
e={1:"hola","a":"mundo"}
f=dict({"b":2})
g=dict(zip("p","q"))
h={1:"marco",2:"oscar",3:"maria"}
i={"hola":1,"como":2,"estas":3}
j=dict(zip("fruta","mandarina"))
k=list(a)
l=tuple(b)
m=set(c)
n=list(d.values())
o=tuple(e.values())
p=set(f.values())
r=list(g)
s=tuple(h)
o=set(i)
q=list(i.values())
print(k)
print(l)
print(m)
print(n)
print(p)
print(q)
print(r)
print(s)
print(o)

