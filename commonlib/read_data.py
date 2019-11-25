#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
import yaml
import os
from conf import settings


def read_yaml(filename):
    file_path = os.path.join(settings.BASE_DIR, "data", filename)
    with open(file_path, "r", encoding="utf-8") as f:
        return yaml.load(f, Loader=yaml.FullLoader)


if __name__ == '__main__':
    print(read_yaml("login_data"))
