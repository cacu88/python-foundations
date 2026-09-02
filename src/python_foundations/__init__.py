def main() -> None:
    name: str = "Facundo"
    age: int = 37
    height: float = 1.70
    is_learning: bool = True
    
    languages: list[str] = [
        "Python", 
        "TypeScript", 
        "JavaScript"
    ]

    languages.append("React")
    
    developer: dict[str, str | list[str]] = {
        "name": name,
        "role": "Junior Developer",
	"languages": languages,
    }


    print(f"Nombre: {name}")
    print(f"Edad: {age}")
    print(f"Altura: {height}")
    print(f"¿Está aprendiendo?: {is_learning}")
    print(f"Primer lenguaje: {languages[0]}")
    print(f"Ultimo lenguaje: {languages[-1]}")
    print(f"Nombre: {developer['name']}")
    print(f"Rol: {developer['role']}")
    print(f"Lenguajes: {', '.join(developer['languages'])}")
    print(f"Cantidad de lenguajes: {len(developer['languages'])}")
