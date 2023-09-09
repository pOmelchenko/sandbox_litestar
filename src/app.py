from litestar import Litestar

import hello_world
import todo
import etc


routes = []
routes.extend(hello_world.routes)
routes.extend(todo.routes)
routes.extend(etc.routes)

app = Litestar(
    route_handlers=routes
)
