import redis
import time
import os


redis_host = os.getenv('REDIS_HOST')
redis_port = os.getenv('REDIS_PORT')
redis_password = os.getenv('REDIS_PASSWORD')


redis_client = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)


def publisher():
    while True:
        message = input("Introduce un mensaje para publicar: ")
        redis_client.publish('canal_prueba', message)
        print(f"Publicado: {message}")

if __name__ == "__main__":
    publisher()
