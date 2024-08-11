# -*- coding: utf-8 -*-

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import yaml

from src.llamafactory.train.tuner import export_model

if __name__ == "__main__":
    with open('../examples/yblir_configs/qwen2_lora_sft_merge.yaml', 'r', encoding='utf-8') as f:
        param = yaml.safe_load(f)

    export_model(param)

