#coding= utf8
import hashlib

myhash = hashlib.md5()
myhash.update("123456")
print type(myhash.hexdigest())