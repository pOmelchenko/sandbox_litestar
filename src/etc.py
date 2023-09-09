from litestar import get
from litestar.exceptions import HTTPException
from litestar.openapi.datastructures import ResponseSpec


class SomeModel(HTTPException):
    pass


@get(
    path="/error",
    tags=["etc"],
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


@get(
    path="/some/{name:str}",
    tags=["etc"],
    summary="Use param from route path",
    description="Print message with data from route path",
)
async def get_some_message_for_name(name: str) -> str:
    return f"Hello from {name}"


routes = [
    get_error,
    get_some_message_for_name,
]
