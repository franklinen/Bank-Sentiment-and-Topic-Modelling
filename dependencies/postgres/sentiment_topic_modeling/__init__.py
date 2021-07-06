import os


class Settings:
    def __init__(self, env):
        self.app_env = env


def get_env():
    if os.getenv('CIRCLECI'):
        return 'circleci'
    return os.getenv('ENV', 'development')


env = get_env()
settings = Settings(env)