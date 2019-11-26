import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_altdns(host):
    ''' Test that altdns and the mode is proper.'''
    path = host.find_command('altdns')

    f = host.file(path)

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
    assert oct(f.mode) == '0o755'


def test_censys(host):
    ''' Test that altdns and the mode is proper.'''
    path = host.find_command('censys-enumeration')

    f = host.file(path)

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
