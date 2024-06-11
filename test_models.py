import glob
import subprocess

all_py_files = glob.glob("models/*/*.py")


def test_all_models():
    for model in all_py_files:
        with open(model) as file:
            content = file.read()
            if "LICENSETYPE: Requires license" in content or "LICENSETYPE: Community" in content or "hansmge" in model:
                continue

        return_code = subprocess.call(["python", model], stdout=subprocess.DEVNULL)
        assert return_code == 0
