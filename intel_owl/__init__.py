"""
IntelOwl: A Python package for performing intelligence analysis and data aggregation.

This package provides tools to gather and process data from various sources.

Example:
    from intel_owl import function1, class1
"""

from .module1 import function1, class1
from .module2 import function2, class2

__version__ = "1.0.0"
__author__ = "Tejas"
__email__ = "tejas@example.com"

__all__ = ["function1", "class1", "function2", "class2"]

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info("IntelOwl package initialized")


