print("Siempre se ejecuta")
print("Buenas, joven")

if __name__ == "__main__":
    print("Ejecutando cuando se invoca directamente")
else:
    print("Ejecutado al ser importado")


def suma(a,b):
    return a+b 

c=suma(5,8)
print(c)