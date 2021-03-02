from geminpy.server import GeminiServer

if __name__ == '__main__':
    s = GeminiServer('./cert.pem', './key.pem', '127.0.0.1')
    s.serve()
