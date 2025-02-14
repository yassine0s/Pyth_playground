from api.server import SimpleHTTPServer


if __name__ == "__main__":
    host = "localhost"
    port = 5000

    server = SimpleHTTPServer(host, port)
    try:
        server.start_server()
    except Exception as e:
        print(f"error happened while starting the server: {e}")
        server.close_server()
