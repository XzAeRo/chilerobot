from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

SIGNATURE_TEMPLATE = """
---
**ChileRobot** | [Autor](/u/XzAeRosho) | [Código Fuente](https://github.com/xzaero/chilerobot)
"""
