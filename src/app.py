from litestar import Litestar, get


@get(
    path="/",
    tags=["main"],
    summary="Hello World message",
    description="This route return `Hello, world!!!` message"
)
async def hello_world() -> str:
    return "Hello, world!!!"


app = Litestar([hello_world])
