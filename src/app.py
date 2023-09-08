from dataclasses import dataclass

from litestar import Litestar, get
from litestar.exceptions import HTTPException
from litestar.openapi.datastructures import ResponseSpec


@dataclass
class ToDoItems:
    title: str
    done: bool


TODO_LIST: list[ToDoItems] = [
    ToDoItems(title="first task", done=False),
    ToDoItems(title="second task", done=True),
    ToDoItems(title="third task", done=False),
]


@get(
    path="/todo",
    tags=["todo"],
    summary="Get list of ToDo items",
    description="This route returns list of ToDo items",
)
async def get_todo_list(done: bool | None = None) -> list[ToDoItems]:
    if done is None:
        return TODO_LIST
    return [item for item in TODO_LIST if item.done == done]


@get(
    path="/hello-world",
    tags=["main"],
    summary="Hello World message",
    description="This route return `Hello, world!` message"
)
async def hello_world() -> str:
    return "Hello, world!"


class SomeModel(HTTPException):
    pass


@get(
    path="/error",
    tags=["error"],
    summary="Handle error",
    description="This route only for handle error",
    responses={
        418: ResponseSpec(
            data_container=SomeModel("hello"),
            description="Another exception",
        )
    },
)
async def get_error(error: bool | None = None) -> str:
    if error is None:
        raise HTTPException("You don't want to throw exception?", status_code=418)
    elif error:
        raise HTTPException("I want to throw exception!", status_code=400)
    else:
        return "Just message"


app = Litestar(
    route_handlers=[
        hello_world,
        get_todo_list,
        get_error,
    ]
)
