from dataclasses import dataclass

FileObjectType = dict[str, str]
FileObjectCollectionType = list[FileObjectType]


@dataclass
class FileObject:
    def __init__(
            self,
            name: str,
            path: str,
            type: str,
            mode: str,
            ino: int,
            dev: int,
            nlink: int,
            uid: int,
            gid: int,
            size: int,
            atime: float,
            mtime: float,
            ctime: float,
    ):
        self.name = name
        self.path = path
        self.type = type
        self.mode = mode
        self.ino = ino
        self.dev = dev
        self.nlink = nlink
        self.uid = uid
        self.gid = gid
        self.size = size
        self.atime = atime
        self.mtime = mtime
        self.ctime = ctime

    def serialize_file_object(self) -> FileObjectType:
        return {
            'name': self.name,
            'path': self.path,
            'type': self.type,
            'mode': self.mode,
            'ino': self.ino,
            'dev': self.dev,
            'nlink': self.nlink,
            'uid': self.uid,
            'gid': self.gid,
            'size': self.size,
            'atime': self.atime,
            'mtime': self.mtime,
            'ctime': self.ctime,
        }
