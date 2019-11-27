import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_pip2_flask(host):
    ''' Test that Flask is installed.'''
    pip_bin = 'pip'

    if host.system_info.distribution.lower() == 'centos' and \
            int(host.system_info.release) >= 8:
        pip_bin = 'pip2'

    pip2_path = host.find_command(pip_bin)
    packages = host.pip_package.get_packages(pip_path=pip2_path)

    assert 'certifi' in packages


def test_test_pip3_flask(host):
    ''' Test that github3.py is installed.'''
    pip3_path = host.find_command('pip3')
    packages = host.pip_package.get_packages(pip_path=pip3_path)

    assert 'Flask' in packages
