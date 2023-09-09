from litestar import get


@get(
    path="/hello-world",
    tags=["main"],
    summary="Hello World message",
    description="This route return `Hello, world!` message"
)
async def get_hello_world() -> str:
    return "Hello, world!"


routes = [
    get_hello_world,
]
