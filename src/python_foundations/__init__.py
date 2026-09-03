def main() -> None:
    name: str = "Facundo"
    age: int = 38
    height: float = 1.70
    is_learning: bool = True
    has_time: bool = True
    total: float = 0.0
    count: int = 0
    
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

    transactions: list[float] = [
        120.50,
        75.00,
        300.25,
        50.00,
    ]

    for transaction in transactions:
        if transaction > 100:
            total = total + transaction
            count += 1
            print(f"Transaction: {transaction}")
    print(f"Total: {total}")
    print(f"Count: {count}")

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

    if is_learning and has_time:
        print("You can continue learning Python.")
    else:
        print("You need to organize your time better.")

    if not is_learning or not has_time:
        print("You should review your learning plan.")

    if age < 18:
        print("You are underage.")
    elif 18 <= age < 30:
        print("You are starting your professional career.")
    elif 30 <= age < 40:
        print("You are in a professional consolidation stage.")
    else:
        print("You have a lot of professional experience.")

