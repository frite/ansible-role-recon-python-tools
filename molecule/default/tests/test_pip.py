import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_pip2_github(host):
    ''' Test that github3.py is installed.'''
    pip_path = host.find_command('pip')
    packages = host.pip_package.get_packages(pip_path)

    assert 'github3.py' in packages


def test_test_pip3_github(host):
    ''' Test that github3.py is installed.'''
    pip3_path = host.find_command('pip3')
    packages = host.pip_package.get_packages(pip3_path)

    assert 'github3.py' in packages
