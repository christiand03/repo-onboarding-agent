from enum import Enum
# Pydantic dient der Typesafety 
from pydantic import BaseModel
# Mittels Union können optionale Parameter deklariert werden
## es geht aber auch ohne import mit z.B. variable : Typ | None = None
from typing import Union
# für Kommunikation mit API
from fastapi import FastAPI

# Instance der FastAPI
app = FastAPI()

# einfacher Endpoint, der ein Dic ausgibt
@app.get("/")
async def root():
    return {"message":"Hello World"}

# Parameter im Endpoint werden an die Funktion weitergegeben
# Wenn man auf http://127.0.0.1:8000/items/foo geht,
# müsste {"item_id": "foo"} zu sehen sein
@app.get("/items/{item_id}")
# mittels Typendeklaration kann man den Typen festlegen, um so unerwünschtes zu verhindern
async def read_item(item_id: int):
    return {"item_id":item_id}

# Es müssen auch die Reihenfolge der Endpunkte beachtet werden
# da FastAPI den ersten nimmt der mit der Anfrage übereinstimmt
# z.B.
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

@app.get("/users/{user_id}")
async def read_user_id(user_id: str):
    return {"user_id": {user_id}}

# würde man es anders herum deklarieren, dann würde /users/me nie ausgeführt werden
# Diese Pfade müssen im Frontend mit eingebunden werden, die Verbindung läuft über CORSMiddleware
# Man kann außerdem keine Pfade überschreiben, da immer der erste Treffer genommen wird
# so eine erneute Deklaration von /users würde nichts bringen

# Für vordefinierte Pfadparameter kann Enum benutzt werden
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    # man kann den model_namen vergleichen
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    # oder man lässt ihn sich ausgeben (andere Methode: ModelName.lenet.value)
    elif model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}
    return {"model_name": model_name, "message": "Have some residuals"}

# Parameter, die nicht Teil des Pfades sind, werden automatisch als Query-Parameter interpretiert

fake_items_db = [
    {"item_name": "Foo"}, 
    {"item_name": "Bar"}, 
    {"item_name": "Baz"}
]

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

# man kann auch optionale Parameter setzen
@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Union[str, None] = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

#  Das importierte BaseModel dient als Grundklasse, von der geerbt wird
class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

@app.post("/items/")
async def create_item(item : Item):
    # Doc-Strings dienen der Dokumentation von Methoden und Klassen
    """ Diese Methode erstellt ein Item """
    item_dict = item.model_dump() # dict() ist veraltet
    if item.tax is not None:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, q: Union[str, None] = None):
    # **: Schlüsselattribute, die als dict ausgegeben werden
    result = {"item_id": item_id, **item.model_dump()}
    if q:
        result.update({"q": q})
    return result
