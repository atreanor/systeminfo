import systeminfo #your own systeminfo module

def main():
    output = systeminfo.get_platform_info()
    print(output)
    return