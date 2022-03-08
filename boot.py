def reload_plugin() -> None:
    import sys

    # Remove all previously loaded plugin modules.
    prefix = __package__ + "."
    for module_name in tuple(filter(lambda m: m.startswith(prefix) and m != __name__, sys.modules)):
        del sys.modules[module_name]


reload_plugin()

from .plugin import *  # noqa: F401, F403
