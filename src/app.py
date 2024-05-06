from litestar import Litestar

from hello_world import HelloWorld
from todo import ToDo
from etc import Etc

import file_manager


app = Litestar(
    route_handlers=[
        HelloWorld,
        ToDo,
        Etc,
    ],
    plugins=[
        file_manager.Plugin()
    ]
)
