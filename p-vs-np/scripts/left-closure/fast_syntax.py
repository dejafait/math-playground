"""Compiled parser adapter; archive inference/field checks stay unchanged."""
import ctypes
from functools import lru_cache
from pathlib import Path
import run as h

LIB = ctypes.CDLL(str(Path(__file__).with_name('output') / 'native_parser-207.so'))


class Info(ctypes.Structure):
    _fields_ = [('tag', ctypes.c_int), ('a', ctypes.c_int),
                ('b', ctypes.c_int), ('name', ctypes.c_char_p)]


LIB.parser_new.restype = ctypes.c_void_p
LIB.parser_free.argtypes = [ctypes.c_void_p]
LIB.parser_parse.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
LIB.parser_parse.restype = ctypes.c_int
LIB.parser_node.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int,
                            ctypes.c_int, ctypes.c_char_p]
LIB.parser_node.restype = ctypes.c_int
LIB.parser_count.argtypes = [ctypes.c_void_p]
LIB.parser_count.restype = ctypes.c_size_t
LIB.parser_info.argtypes = [ctypes.c_void_p, ctypes.c_size_t]
LIB.parser_info.restype = Info
LIB.parser_error.restype = ctypes.c_char_p


class FastSyntax(h.audit.Syntax):
    def __init__(self):
        super().__init__()
        self.pool = LIB.parser_new()
        # Instance caches avoid retaining pools through function-global caches.
        self.parse = lru_cache(4096)(self._parse)
        self.text = lru_cache(16384)(self._text)

    def _sync(self, result):
        if result < 0:
            raise ValueError(LIB.parser_error().decode('ascii'))
        for i in range(len(self.nodes), LIB.parser_count(self.pool)):
            n = LIB.parser_info(self.pool, i)
            args = (n.name.decode('ascii'),) if n.tag == 0 else (
                (n.a,) if n.tag == 1 else (n.a, n.b))
            got = h.audit.Syntax.node(self, ('v', 'n', 'i')[n.tag], *args)
            assert got == i, 'compiled/Python interning differs'
        return result

    def _parse(self, text):
        if not isinstance(text, str): raise ValueError('native string required')
        data = text.encode('ascii')
        return self._sync(LIB.parser_parse(self.pool, data, len(data)))

    def node(self, tag, *args):
        if tag == 'v':
            a, b, name = -1, -1, args[0].encode('ascii')
        elif tag == 'n':
            a, b, name = args[0], -1, None
        elif tag == 'i':
            a, b, name = *args, None
        else:
            raise ValueError('unknown node')
        return self._sync(LIB.parser_node(self.pool, ('v', 'n', 'i').index(tag), a, b, name))

    def _text(self, i, image=False):
        return h.audit.Syntax.text.__wrapped__(self, i, image)

    def close(self):
        self.parse.cache_clear(); self.text.cache_clear()
        LIB.parser_free(self.pool); self.pool = None
