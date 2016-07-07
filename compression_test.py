from json import load

import lzma
import zlib
from time import time

class CompressionTest:
    def __init__(self):
        self.load_data()
        self.run_lzma()
        self.run_zlib()

    def load_data(self):
        f = open("json_data.txt", "r")
        self.data = load(f)
        self.raw_data = str(self.data).encode('utf-8')
        f.close()

    def get_data(self):
        return self.data

    def run_lzma(self):
        start = time()
        self.lzma_compressed = lzma.compress(self.raw_data)
        self.lzma_compress_time = time() - start

        start = time()
        lzma.decompress(self.lzma_compressed)
        self.lzma_decompress_time = time() - start

    def run_zlib(self):
        start = time()
        self.zlib_compressed = zlib.compress(self.raw_data)
        self.zlib_compress_time = time() - start

        start = time()
        zlib.decompress(self.zlib_compressed)
        self.zlib_decompress_time = time() - start

    def print_stats(self):
        print("Data Length (objs):", len(self.data))
        print("Data Length (bytes):", len(self.raw_data))

        print("LZMA Compressed Length:", len(self.lzma_compressed))
        print("ZLib Compressed Length:", len(self.zlib_compressed))

        print("LZMA Compress Time:", self.lzma_compress_time)
        print("ZLib Compress Time:", self.zlib_compress_time)

        print("LZMA Decompress Time:", self.lzma_decompress_time)
        print("ZLib Decompress Time:", self.zlib_decompress_time)

        print("")
        print("LZMA Compression Ratio:", 1.0 - float(len(self.lzma_compressed))/float(len(self.raw_data)))
        print("ZLib Compression Ratio:", 1.0 - float(len(self.zlib_compressed))/float(len(self.raw_data)))


def main():
    ct = CompressionTest()
    ct.print_stats()

if __name__ == "__main__": main()