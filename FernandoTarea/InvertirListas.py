from typing import List, Any

def invertir_lista(lista_original: List[Any]) -> List[Any]:
    """
    Devuelve una nueva lista con los elementos de lista_original en orden inverso.

    Args:
        lista_original (List[Any]): Lista a invertir.

    Returns:
        List[Any]: Nueva lista invertida.
    """
    return lista_original[::-1]  # Slicing con paso negativo para invertir

# Pruebas
if __name__ == "__main__":
    print("\nProbando invertir_lista con slicing...")

    lista_prueba = [1, 2, 3, 4, 5]
    lista_resultante = invertir_lista(lista_prueba)

    assert lista_resultante == [5, 4, 3, 2, 1], "❌ Error en inversión con slicing"
    assert lista_prueba == [1, 2, 3, 4, 5], "❌ ¡La lista original fue modificada!"
    assert invertir_lista(["a", "b", "c"]) == ["c", "b", "a"]
    assert invertir_lista([]) == []

    print("¡Pruebas con slicing pasaron! ✅")
    print("-----------Fernando Navia Nova-----------")
    
