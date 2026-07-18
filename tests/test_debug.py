import sys

def test_sys_path():
    print("\n----- sys.path -----")
    for path in sys.path:
        print(path)