# Week 1: Introduction to FastAPI

## What is FastAPI?

FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.8+ based on standard Python type hints.

## Rest-API: Representational State Transfer Application Programming Interface

Rest is a architectural style for designing network applications. It is based on a simple idea: create a web application as a collection of resources, where each resource is identified by a unique identifier (URI), and can be manipulated using a standard set of operations (HTTP methods).

## Features of FastAPI

1. **Fast:** High-performance, on par with NodeJS and Go, thanks to Starlette and Pydantic.
2. **Easy to learn and use:** Simple and intuitive syntax.
3. **Type hints:** Built-in support for Python type hints.
4. **Automatic documentation:** Automatic generation of OpenAPI (Swagger) and ReDoc documentation.
5. **Validation:** Automatic request and response validation.
6. **Dependencies:** Built-in support for dependency injection.

## CRUD Operations: 

1. Create: **POST**
2. Read: **GET**
3. Update: **PUT**
4. Delete: **DELETE**


# Concept of Decorators in Python

Decorators are a design pattern in Python that allows you to modify or enhance the behavior of a function or a class without changing its source code.

**Syntax:**


def decoratorFunc(original_function):
    def wrapperFunction():
        print("Do something before original function")
        original_function()
        print("Do something after original function")
    return wrapperFunction



@decoratorFunc
def someFunction(): 
    # original funcitonality
    return whatsoever

what happens under the hood: 

someFunction = decoratorFunc(someFunction)
someFunction()
