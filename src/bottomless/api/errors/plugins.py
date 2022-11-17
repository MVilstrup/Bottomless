class PluginError(Exception):
    pass


class UnhandledPluginRunTimeErrorState(PluginError):
    pass


class PluginRecoveryError(PluginError):
    pass


class PluginStateChangeError(PluginError):
    pass
