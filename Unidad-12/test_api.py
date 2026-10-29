import requests
BASE = "http://127.0.0.1:5000/api"

# 1. GET /api/libros
r = requests.get(f"{BASE}/libros")
print("1- GET libros:", r.status_code, r.json())

r = requests.post(f"{BASE}/autores",
                  json={"nombre": "Pepe", "nacionalidad": "Argentino"})
print("2- POST autor:", r.status_code, r.json())
autor_id = r.json()["id"]

r = requests.post(f"{BASE}/libros",
                  json={"titulo": "Como hablar", "anio": 2002, "autor_id": autor_id})
print("3- POST libro:", r.status_code, r.json())
libro_id = r.json()["id"]

r = requests.put(f"{BASE}/libros/{libro_id}",
                 json={"titulo": "Como Comer"})
print("4- PUT libro:", r.status_code, r.json())

r = requests.delete(f"{BASE}/libros/{libro_id}")
print("5- DELETE libro:", r.status_code, r.json())
assert r.status_code == 200, "El libro no se elimino correctamente"
print("Libro eliminado correctamente")

#para mostrar errores:
r = requests.get(f"{BASE}/libros/{libro_id}")
print("6- GET libro borrado:", r.status_code, r.json())   # 404

r = requests.post(f"{BASE}/autores", json={})
print("7- POST autor vacío:", r.status_code, r.json())    # 400