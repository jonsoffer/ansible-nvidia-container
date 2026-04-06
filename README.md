Ansible playbook to install and configure NVIDIA Container Toolkit on Debian based on https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html.

The motivation was to avoid the curl-pipe-bash pattern.

To run this playbook, ensure you have Ansible installed and run: `ansible-playbook -K install.yaml`.
