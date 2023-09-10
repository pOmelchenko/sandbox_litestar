from dataclasses import dataclass
from typing import Any

from litestar import get, post, put, delete, Controller
from litestar.exceptions import NotFoundException


ToDoType = dict[str, Any]
ToDoCollectionType = list[ToDoType]


class Base:
    ...


@dataclass
class ToDoItem(Base):
    def __init__(self, title: str, done: bool):
        self.title = title
        self.done = done

    def serialize_todo(self) -> ToDoType:
        return {
            "title": self.title,
            "done": self.done,
        }


TODO_LIST: list[ToDoItem] = [
    ToDoItem(title="first task", done=False),
    ToDoItem(title="second task", done=True),
    ToDoItem(title="third task", done=False),
]


class ToDo(Controller):
    path = "/todo"
    tags = ["todo"]

    @get(
        summary="Get list of ToDo items",
        description="This route returns list of ToDo items",
    )
    async def index(self, done: bool | None = None) -> ToDoCollectionType:
        data = TODO_LIST if done is None else [item for item in TODO_LIST if item.done == done]

        return [item.serialize_todo() for item in data]

    @post(
        summary="Create new item of ToDo",
        description="This route create a new item of ToDo",
    )
    async def store(self, data: ToDoType) -> ToDoType:
        item = ToDoItem(
            title=data["title"],
            done=data["done"],
        )

        TODO_LIST.append(item)

        return item.serialize_todo()

    @staticmethod
    def __get_todo_item_by_title(title: str) -> ToDoItem:
        for item in TODO_LIST:
            if item.title == title:
                return item
        raise NotFoundException(detail=f"ToDo {title!r} not found")

    @get(
        path="/{title:str}",
        summary="Return ToDo item by title",
        description="This route return ToDo item by title",
    )
    async def show(self, title: str) -> ToDoType:
        return self.__get_todo_item_by_title(title).serialize_todo()

    @put(
        path="/{title:str}",
        summary="Update ToDo item by title",
        description="This route for update ToDo item by title",
    )
    async def update(self, title: str, data: ToDoType) -> ToDoType:
        item = self.__get_todo_item_by_title(title)
        item.title = data["title"]
        item.done = data["done"]

        return item.serialize_todo()

    @delete(
        path="/{title:str}",
        summary="Delete ToDo item by title",
        description="This route for delete ToDo item by title",
    )
    async def destroy(self, title: str) -> None:
        for key, item in enumerate(TODO_LIST):
            if item.title == title:
                del TODO_LIST[key]
