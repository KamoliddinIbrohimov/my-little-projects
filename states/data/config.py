from environs import Env

# using the environs library
env = Env()
env.read_env()

# We read the following from the .env file
BOT_TOKEN = env.str("BOT_TOKEN")  # Bot token
ADMINS = env.list("ADMINS")  # list of admins
IP = env.str("ip")  # The host ip address

PROVIDER_TOKEN_CLICK = env.str("PROVIDER_TOKEN_CLICK")
PROVIDER_TOKEN_PAYME = env.str("PROVIDER_TOKEN_PAYME")
