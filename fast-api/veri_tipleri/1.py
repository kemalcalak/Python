from typing import List,Set,Tuple,Dict,Optional

def process_items(items_t: Tuple[int, int, str], items_s: Set[bytes]):
    return items_t, items_s

def process_items(items: List[str]):
    for item in items:
        print(item)

def process_items(prices: Dict[str, float]):
    for item_name, item_price in prices.items():
        print(item_name)
        print(item_price)

def say_hi(name: Optional[str] = None):
    if name is not None:
        print(f"Hey {name}!")
    else:
        print("Hello World")

class Person:
    def __init__(self, name: str):
        self.name = name

def get_person_name(one_person: Person):
    return one_person.name

