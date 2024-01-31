import gzip

data = '9C 2B C9 57 28 CD 73 CE 2F 4B 0D 52 48 2D 4B 2D AA 54 C8 49 2C'

# for Python 3.x
data = data if isinstance(data, bytes) else data.encode('utf-8')
gzip.decompress(data)