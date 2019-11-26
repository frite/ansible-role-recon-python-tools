import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_nmap(host):
    '''Assert that nmap is installed.'''
    f = host.package('nmap')

    assert f.is_installed
