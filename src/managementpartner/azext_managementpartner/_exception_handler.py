# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


from azure.cli.core.util import CLIError


def managementpartner_exception_handler(ex):
    from azext_managementpartner.vendored_sdks.models import Error
    if isinstance(ex, Error):
        message = ex.error.error.message
        raise CLIError(message)
    import sys
    from six import reraise
    reraise(*sys.exc_info())
