from dataclasses import dataclass

from litestar import get, post
from litestar.exceptions import NotFoundException


@dataclass
class ToDoItem:
    title: str
    done: bool


TODO_LIST: list[ToDoItem] = [
    ToDoItem(title="first task", done=False),
    ToDoItem(title="second task", done=True),
    ToDoItem(title="third task", done=False),
]


@get(
    path="/todo",
    tags=["todo"],
    summary="Get list of ToDo items",
    description="This route returns list of ToDo items",
)
async def get_todo_list(done: bool | None = None) -> list[ToDoItem]:
    if done is None:
        return TODO_LIST
    return [item for item in TODO_LIST if item.done == done]


@post(
    path="/todo",
    tags=["todo"],
    summary="Create new item of ToDo",
    description="This route create a new item of ToDo",
)
async def post_todo_list(data: ToDoItem) -> list[ToDoItem]:
    TODO_LIST.append(data)

    return TODO_LIST


def get_todo_item_by_title(title: str) -> ToDoItem:
    for item in TODO_LIST:
        if item.title == title:
            return item
    raise NotFoundException(detail=f"ToDo {title!r} not found")


@get(
    path="/todo/{title:str}",
    tags=["todo"],
    summary="Return todo item by title",
    description="This route return ToDo item by title",
)
async def get_item_by_title(title: str) -> ToDoItem:
    return get_todo_item_by_title(title)


routes = [
    get_todo_list,
    post_todo_list,
    get_item_by_title,
]
