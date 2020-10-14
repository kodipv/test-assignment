import os

if "CONFIG_LEVEL" not in os.environ:
    os.environ["CONFIG_LEVEL"] = "local"
