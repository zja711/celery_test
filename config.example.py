REDIS_CONFIG = dict(
    broker='redis://:password@host:6379/0',
    backend='redis://:password@host:6379/0',
    include=['example.task1']
)

if __name__ == "__main__":
    print REDIS_CONFIG