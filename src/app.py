from dataclasses import dataclass
from litestar import Litestar, get


@dataclass
class ToDoItems:
    title: str
    done: bool


@get(
    path="/hello-world",
    tags=["main"],
    summary="Hello World message",
    description="This route return `Hello, world!` message"
)
async def hello_world() -> str:
    return "Hello, world!"


app = Litestar(
    route_handlers=[hello_world]
)
