from dataclasses import dataclass

from litestar import get, post, put, delete, Controller
from litestar.exceptions import NotFoundException


class Base:
    ...


@dataclass
class ToDoItem(Base):
    title: str
    done: bool


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
    async def index(self, done: bool | None = None) -> list[ToDoItem]:
        if done is None:
            return TODO_LIST
        return [item for item in TODO_LIST if item.done == done]

    @post(
        summary="Create new item of ToDo",
        description="This route create a new item of ToDo",
    )
    async def store(self, data: ToDoItem) -> list[ToDoItem]:
        TODO_LIST.append(data)

        return TODO_LIST

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
    async def show(self, title: str) -> ToDoItem:
        return self.__get_todo_item_by_title(title)

    @put(
        path="/{title:str}",
        summary="Update ToDo item by title",
        description="This route for update ToDo item by title",
    )
    async def update(self, title: str, data: ToDoItem) -> list[ToDoItem]:
        item = self.__get_todo_item_by_title(title)
        item.title = data.title
        item.done = data.done

        return TODO_LIST

    @delete(
        path="/{title:str}",
        summary="Delete ToDo item by title",
        description="This route for delete ToDo item by title",
    )
    async def destroy(self, title: str) -> None:
        for item in TODO_LIST:
            if item.title == title:
                TODO_LIST.remove(item)
