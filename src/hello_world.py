from litestar import get, Controller


class HelloWorld(Controller):
    path = "/hello-world"
    tags = ["main"]

    @get(
        summary="Hello World message",
        description="This route return `Hello, world!` message"
    )
    async def get_hello_world(self) -> str:
        return "Hello, world!"
