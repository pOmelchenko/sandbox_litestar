from litestar import Litestar

from hello_world import get_hello_world
from todo import get_todo_list, post_todo_list
from etc import get_error


app = Litestar(
    route_handlers=[
        get_hello_world,
        get_todo_list,
        post_todo_list,
        get_error,
    ]
)
