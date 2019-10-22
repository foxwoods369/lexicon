# Test for one implementation of the interface
from lexicon.tests.providers.integration_tests import IntegrationTests
from unittest import TestCase

# Hook into testing framework by inheriting unittest.TestCase and reuse
# the tests which *each and every* implementation of the interface must
# pass, by inheritance from integration_tests.IntegrationTests
class FooProviderTests(TestCase, IntegrationTests):
    """Integration tests for hostingde provider"""

    provider_name = 'hostingde'
    domain = 'eruza.de'

    def _filter_post_data_parameters(self):
        return ['authToken']

    def _filter_headers(self):
        return ['Authorization']

    def _filter_query_parameters(self):
        return ['secret_key']