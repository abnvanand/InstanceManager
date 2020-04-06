import os

import vagrant

current_count = 0


def start_in_dir(dir_name):
    try:
        os.rmdir(dir_name)
    except OSError as e:
        print(e)

    try:
        os.mkdir(dir_name)
    except OSError as e:
        print(e)

    os.chdir(dir_name)
    v = vagrant.Vagrant()
    v.init("bento/ubuntu-16.04")
    v.up()
    response = {"name": dir_name, "host": v.hostname(), "port": v.port()}
    os.chdir("..")

    return response


def instance_mgr(num_instances: int):
    global current_count
    instance_list = []

    for i in range(num_instances):
        vm_name = f"vm{current_count}"

        current_count += 1
        machine_info = start_in_dir(vm_name)
        instance_list.append(machine_info)

    return instance_list


def stop_vm(vm_names: list):
    for vm_name in vm_names:
        os.chdir(vm_name)
        v = vagrant.Vagrant()
        v.halt()
    os.chdir("..")


if __name__ == "__main__":
    print(instance_mgr(2))
    # stop_vm(["vm0", "vm1"])
