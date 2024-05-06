from litestar import get, Controller as BaseController

from .service import FileObjectCollectionType, get_file_objects


class Controller(BaseController):
    path = "/objects"
    tags = ["file-manager"]

    @get(
        summary="Get list of files",
        description="This route returns list of files",
    )
    async def index(self) -> FileObjectCollectionType:
        return get_file_objects('../files')
