[![Build Status](https://travis-ci.com/frite/ansible-role-recon-python2-tools.svg?branch=master)](https://travis-ci.com/frite/ansible-role-recon-python2-tools)


recon_python_tools
=========

Ansible role to handle Python 2 & 3 tools and relevant requirements (i.e. packages).

Requirements
------------

None

Role Variables
--------------

Depending on what you want to do, the following vars can be configured.
To configure packages for CentOS 7.
```
py_yum_packages:
  - 'nmap'
```
To configure packages for CentOS 8:
```  
py_dnf_packages:
  - 'nmap'
```
To configure packages for apt:
```  
py_apt_packages:
  - 'nmap'
```
To add tools you want to clone.
```        
py_clone_tools:
  bass:
    name: bass
    url: https://github.com/Abss0x7tbh/bass.git
  sublist3r:
    name: Sublist3r
    url: https://github.com/aboul3la/Sublist3r.git
  altdns:
    name: altdns
    url: https://github.com/infosec-au/altdns.git
  censys:
    name: censys-enumeration
    url: https://github.com/0xbharath/censys-enumeration.git
```
To install python 3 or python 2 `requirements.txt`
```
py3_pip_args:
  - bass
  - Sublist3r
py2_pip_args:
  - altdns
  - censys-enumeration
```
To run setup.py automatically
```
py2_setup_files:
  - altdns
py3_setup_files:
  - Sublist3r
```
To create softlinks
```
py_soft_links:
  bass:
    repo: bass
    soft_link: bass
    file: bass.py
  censys:
    repo: censys-enumeration
    soft_link: censys-enumeration
    file: censys_enumeration.py
```
Finally, to install additional eggs.
```
py2_pip_eggs:
  - github3.py
py3_pip_eggs:
  - github3.py
```


Dependencies
------------
None

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables
passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: ansible-role-recon-python-tools, Whatever vars here }

License
-------

BSD

Author Information
------------------