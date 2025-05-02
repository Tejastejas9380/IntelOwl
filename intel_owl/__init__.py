# hello brothers
"""
IntelOwl: A Python package for performing intelligence analysis and data aggregation.
This package provides tools to gather and process data from various sources.
"""
from .module1 import function1, class1
from .module2 import function2, class2

__version__ = "1.0.0"
__author__ = "Tejas"
__email__ = "tejas@example.com"


import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info("IntelOwl package initialized")


__all__ = ["function1", "class1", "function2", "class2"]

"""
IntelOwl: Intelligence analysis and data aggregation package.
"""

__version__ = "1.0.0"
__author__ = "Tejas"
__email__ = "tejas@example.com"

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info("IntelOwl package initialized")

# Package-level imports
from .module1 import function1, class1
from .module2 import function2, class2

__all__ = ["function1", "class1", "function2", "class2"]
