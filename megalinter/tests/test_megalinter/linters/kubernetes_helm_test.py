# !/usr/bin/env python3
"""
Unit tests for KUBERNETES linter helm
This class has been automatically @generated by .automation/build.py, please do not update it manually
"""

from unittest import TestCase

from megalinter.tests.test_megalinter.LinterTestRoot import LinterTestRoot


class kubernetes_helm_test(TestCase, LinterTestRoot):
    descriptor_id = "KUBERNETES"
    linter_name = "helm"