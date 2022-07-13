'''ocrnet_resnet50os8_ade20k'''
import os
from .base_cfg import *


# modify dataset config
DATASET_CFG = DATASET_CFG.copy()
DATASET_CFG.update({
    'type': 'ade20k',
    'rootdir': os.path.join(os.getcwd(), 'ADE20k'),
})
# modify dataloader config
DATALOADER_CFG = DATALOADER_CFG.copy()
# modify optimizer config
OPTIMIZER_CFG = OPTIMIZER_CFG.copy()
OPTIMIZER_CFG.update({
    'max_epochs': 130
})
# modify losses config
LOSSES_CFG = LOSSES_CFG.copy()
# modify segmentor config
SEGMENTOR_CFG = SEGMENTOR_CFG.copy()
SEGMENTOR_CFG.update({
    'num_classes': 150,
    'backbone': {
        'type': 'resnet50',
        'series': 'resnet',
        'pretrained': True,
        'outstride': 8,
        'use_stem': True,
        'selected_indices': (2, 3),
    },
    'auxiliary': {
        'in_channels': 1024,
        'out_channels': 512,
        'dropout': 0,
    },
    'bottleneck': {
        'in_channels': 2048,
        'out_channels': 512,
    },
})
# modify inference config
INFERENCE_CFG = INFERENCE_CFG.copy()
# modify common config
COMMON_CFG = COMMON_CFG.copy()
COMMON_CFG['work_dir'] = 'ocrnet_resnet50os8_ade20k'
COMMON_CFG['logfilepath'] = 'ocrnet_resnet50os8_ade20k/ocrnet_resnet50os8_ade20k.log'
COMMON_CFG['resultsavepath'] = 'ocrnet_resnet50os8_ade20k/ocrnet_resnet50os8_ade20k_results.pkl'