from environs import Env

env = Env()
env.read_env()

main_bot = env.str("main_bot")
