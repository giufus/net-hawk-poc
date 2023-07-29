
import os
from dynaconf import Dynaconf

settings = Dynaconf(
    root_path=os.path.dirname(os.path.realpath(__file__)),
    envvar_prefix="DYNACONF",
    environments=True,
    settings_files=['settings.toml', '.secrets.toml'],
)

# `envvar_prefix` = export envvars with `export DYNACONF_FOO=bar`.
# `settings_files` = Load these files in the order.
