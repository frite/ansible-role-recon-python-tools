import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_pip2_github(host):
    ''' Test that github3.py is installed.'''
    pip_bin = 'pip'

    if host.system_info.distribution == 'CentOS' and host.system_info.release > 7:
        pip_bin = 'pip2'

    pip2_path = host.find_command(pip_bin)
    packages = host.pip_package.get_packages(pip_path=pip2_path)

    assert 'Flask' in packages


def test_test_pip3_github(host):
    ''' Test that github3.py is installed.'''
    pip3_path = host.find_command('pip3')
    packages = host.pip_package.get_packages(pip_path=pip3_path)

    assert 'Flask' in packages
