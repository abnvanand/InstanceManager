# Instance manager module 
- Allows other modules to request for instances
- Input parameter = number_of_instances
- Output = {name: nameOfInstance, host:ipAddressOfVm, port:portWhereSshIsEnabled}

# Fault tolerance

The instance manager periodically checks(every 10 seconds) if a vm (eg vm running the scheduler) is down,
and in case it is down, it starts a new instance and launches the scheduler on that instance and also updates schedulers global config file.
