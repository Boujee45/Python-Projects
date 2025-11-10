
import secrets

bruh = secrets.token_hex(100000000)

hello = secrets.token_bytes(10000000)

good = secrets.token_urlsafe(1000000)

print(bruh)