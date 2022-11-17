import os

root_path = "/".join(os.path.abspath(__file__).split("/")[:3])

os.system(f"cp pythons/* {root_path}/.pyenv/cache")

versions_list = os.listdir(root_path+"/.pyenv/versions/")
pythons_list = list(map(lambda x: ".".join(x.split(".")[:3]).replace("Python-",""), os.listdir("pythons")))

for v in pythons_list:
    if v not in versions_list:
        os.system(f"pyenv install {v}")
