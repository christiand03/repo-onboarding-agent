# FastAPI
## Was ist FastAPI
FastAPI ist ein modernes, schnelles Webframework für Python, mit dem man APIs (also Schnittstellen zwischen Frontend und Backend) entwickeln kann.

Es basiert auf Python-Typannotationen und nutzt asynchrone Programmierung, wodurch es sehr performant ist.
FastAPI überprüft automatisch Eingaben, erzeugt Dokumentation (z. B. unter /docs) und erleichtert den Datenaustausch zwischen Server und Frontend.

## Welche Endpunkt Operatoren gibt es?
POST: erstellt Daten
GET: liest Daten
PUT: aktualisiert Daten
DELETE: löscht daten

Diese werden in Python wie in main.py dargestellt genutzt.
Neben diesen 4 grundlegenden Operatoren gibt es noch options, head, patch und trace. Diese werden für uns aber erstmal nicht wichtig sein

## Daten vom Client(z.B. Browser) and API sende

**Request Body**: Daten, die der Client an die API schickt
**Response Body**: Daten, die die API an den Client schickt

API muss meistens immer einen Response Body schicken. Client aber nicht immer einen Request Body. Er kann auch nur einen Pfad mit Query-Parametern oder Body schicken

Um den Request Body zu deklarieren, benutzt man [Pydanticmodelle](https://docs.pydantic.dev/latest/)

Kleiner Pydantic-Exkurs aus deren Docs:

**Why use Pydantic?**

Powered by type hints — with Pydantic, schema validation and serialization are controlled by type annotations; less to learn, less code to write, and integration with your IDE and static analysis tools. Learn more…
Speed — Pydantic's core validation logic is written in Rust. As a result, Pydantic is among the fastest data validation libraries for Python.

JSON Schema — Pydantic models can emit JSON Schema, allowing for easy integration with other tools.

Strict and Lax mode — Pydantic can run in either strict mode (where data is not converted) or lax mode where Pydantic tries to coerce data to the correct type where appropriate. 

Dataclasses, TypedDicts and more — Pydantic supports validation of many standard library types including dataclass and TypedDict.

Customisation — Pydantic allows custom validators and serializers to alter how data is processed in many powerful ways.

Ecosystem — around 8,000 packages on PyPI use Pydantic, including massively popular libraries like FastAPI, huggingface, Django Ninja, SQLModel, & LangChain.

Battle tested — Pydantic is downloaded over 360M times/month and is used by all FAANG companies and 20 of the 25 largest companies on NASDAQ. If you're trying to do something with Pydantic, someone else has probably already done it.

**Weiter mit Tutorial**

Um Daten zu senden, wird meist POST genutzt, es gehen aber auch PUT, DELETE und PATCH.
