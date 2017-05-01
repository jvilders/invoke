import os

from invocations.docs import docs, www, sites, watch_docs
from invocations.testing import test, coverage, integration, watch_tests
from invocations.packaging import vendorize, release
from invocations import travis

from invoke import Collection
from invoke.util import LOG_FORMAT


ns = Collection(
    test, coverage, integration, vendorize, release, www, docs, sites,
    watch_docs, watch_tests, travis,
)
ns.configure({
    'tests': {
        'logformat': LOG_FORMAT,
        'package': 'invoke',
    },
    'packaging': {
        'sign': True,
        'wheel': True,
        'check_desc': True,
        # Because of PyYAML's dual source nonsense =/
        'dual_wheels': True,
        'changelog_file': os.path.join(
            www.configuration()['sphinx']['source'],
            'changelog.rst',
        ),
    },
    # TODO: perhaps move this into a tertiary, non automatically loaded, conf
    # file so that both this & the code under test can reference it? Meh.
    'travis': {
        'sudo': {
            'user': 'sudouser',
            'password': 'mypass',
        },
    },
})
