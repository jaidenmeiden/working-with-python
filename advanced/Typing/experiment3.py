from typing import Dict, List, Tuple

positives: List[int] = [1, 2, 3, 4, 5]

users: Dict[str, int] = {
    'colombia': 1,
    'mexico': 2,
    'argentina': 3
}

countries: List[Dict[str, str]] = [
    {
        'name': 'Colombia',
        'people': '77000'
    },
    {
        'name': 'México',
        'people': '100000'
    },
    {
        'name': 'Argentina',
        'people': '45000'
    }
]

numbers: Tuple[int, float, int] = (1, 0.5, 1)

coordinates: List[Dict[str, Tuple[int, int]]] = [
    {
        'coordinates1': (1, 3),
        'coordinates2': (3, 7)
    },
    {
        'coordinates1': (0, 7),
        'coordinates2': (2, 7)
    }
]
