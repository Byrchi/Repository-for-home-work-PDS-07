import socket
import logging

def main():
    logger = logging.getLogger("server_log")
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler(f"{'server'}.log", mode='w')
    formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    try:
        while True:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind(('', 55000))
            sock.listen(15)
            logger.info('Server is running')
            print('Server is running')
            while True:
                conn, addr = sock.accept()
                logger.warning(f'connected: {addr}')
                print('connected:', addr)
                data = conn.recv(1024)
                logger.warning(f'received message: {data}')
                print(str(data))
                conn.send(data.upper())
                logger.info('answer sends')
            conn.close()

    except Exception as err:
        logger.error(f'{err}')

if __name__ == "__main__":
    main()