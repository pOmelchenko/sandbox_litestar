from litestar import get


def routes() -> list:
    return [
        HelloWorld.get_hello_world,
    ]


class HelloWorld:
    @get(
        path="/hello-world",
        tags=["main"],
        summary="Hello World message",
        description="This route return `Hello, world!` message"
    )
    async def get_hello_world(self) -> str:
        return "Hello, world!"
