import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_sublist3r(host):
    ''' Assume that sublist3r exists and has the correct mode '''

    f = host.file('/usr/local/bin/sublist3r')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
    assert oct(f.mode) == '0o755'


def test_bass(host):
    ''' Assume that bass exists and has the correct mode '''

    f = host.file('/usr/local/bin/bass')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
    assert oct(f.mode) == '0o777'
