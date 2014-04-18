import glob
import subprocess
import sys


def main():
    tests = glob.glob("test_*.py")
    if len(sys.argv) > 1 and sys.argv[1] == "coverage":
        coverage(tests)
    else:
        test(tests)

def test(tests):
    for test in tests:
        print("\nTests for %s" % test[5:])
        subprocess.call("python3.4 %s" % test, shell=True)

def coverage(tests):
    subprocess.call("coverage erase", shell=True)

    for test in tests:
        subprocess.call("coverage run -p %s" % test, shell=True)

    subprocess.call("coverage combine", shell=True)
    subprocess.call("coverage report -m", shell=True)

if __name__ == '__main__':
    main()