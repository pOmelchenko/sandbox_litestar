from litestar import Litestar

from hello_world import HelloWorld
from todo import ToDo
from etc import Etc


app = Litestar(
    route_handlers=[HelloWorld, ToDo, Etc]
)
