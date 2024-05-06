import os
import stat

from .file_object import *


def get_file_objects(path: str) -> FileObjectCollectionType:
    objects = []

    for root, d_names, f_names in os.walk(os.path.expanduser(path)):

        if d_names:
            for d_name in d_names:
                objects.append(_create_object(d_name, root, 'dir'))

        if f_names:
            for f_name in f_names:
                objects.append(_create_object(f_name, root, 'file'))

    return [file_object.serialize_file_object() for file_object in objects]


def _create_object(name: str, root: str, object_type: str):
    file_stat = os.stat(root + '/' + name)

    return FileObject(
        name=name,
        path=root + '/' + name,
        type=object_type,
        mode=stat.filemode(file_stat.st_mode),
        ino=file_stat.st_ino,
        dev=file_stat.st_dev,
        nlink=file_stat.st_nlink,
        uid=file_stat.st_uid,
        gid=file_stat.st_gid,
        size=file_stat.st_size,
        atime=file_stat.st_atime,
        mtime=file_stat.st_mtime,
        ctime=file_stat.st_ctime,
    )
