from dataclasses import dataclass

from litestar import get


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
