import psutil
def system_usage():
    cpu=psutil.cpu_percent()
    ram=psutil.virtual_memory()
    return {"cpu":cpu, "ram":ram.percent}
