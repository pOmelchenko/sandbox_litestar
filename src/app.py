from litestar import Litestar

import hello_world
import todo
import etc


routes = []

for controller in [hello_world, todo, etc]:
    routes.extend(controller.routes())

app = Litestar(
    route_handlers=routes
)
