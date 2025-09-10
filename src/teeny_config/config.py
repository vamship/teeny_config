"""
Configuration management module for an application. This module provides
functions to initialize and access configuration values loaded from a file.
"""

_config_data = None


def init_config(file: str = "app.cfg") -> None:
    """
    Initialize application configuration by reading values from a file. This
    function must be called before accessing any configuration variables. The
    configuration file should contain key-value pairs in the format:
    key=value. Lines starting with '#' are treated as comments. Commented lines
    and empty lines are ignored.

    :param file: The path to the configuration file.
    """

    global _config_data

    if _config_data is not None:
        return

    try:
        _config_data = {}
        with open(file, "r") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):
                    key, value = line.split("=", 1)
                    _config_data[key.strip()] = value.strip()
    except OSError as e:
        print(f"Error reading config file {file}: {e}")
        _config_data = None


def get_config_value(key: str, default=None) -> str:
    """
    Get a configuration value by key.

    :param key: The configuration key to retrieve.
    :param default: The default value to return if the key is not found.
    :return: The configuration value or the default value.
    """
    global _config_data

    if _config_data is None:
        raise ValueError(
            "Configuration not initialized. Invoke init_config() first.")

    if default is None and key not in _config_data:
        raise KeyError(f'Configuration value not found [{key}]')

    return _config_data.get(key, default)
