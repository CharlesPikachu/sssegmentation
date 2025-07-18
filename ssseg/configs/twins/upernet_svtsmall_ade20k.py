'''upernet_svtsmall_ade20k'''
import os
from .._base_ import REGISTERED_SEGMENTOR_CONFIGS, REGISTERED_DATASET_CONFIGS, REGISTERED_DATALOADER_CONFIGS


# deepcopy
SEGMENTOR_CFG = REGISTERED_SEGMENTOR_CONFIGS['TWINS_SEGMENTOR_CFG'].copy()
# modify dataset config
SEGMENTOR_CFG['dataset'] = REGISTERED_DATASET_CONFIGS['DATASET_CFG_ADE20k_512x512'].copy()
# modify dataloader config
SEGMENTOR_CFG['dataloader'] = REGISTERED_DATALOADER_CONFIGS['DATALOADER_CFG_BS16'].copy()
# modify scheduler config
SEGMENTOR_CFG['scheduler']['max_epochs'] = 130
SEGMENTOR_CFG['scheduler']['min_lr'] = 0.0
SEGMENTOR_CFG['scheduler']['power'] = 1.0
SEGMENTOR_CFG['scheduler']['warmup_cfg'] = {'type': 'linear', 'ratio': 1e-6, 'iters': 1500}
# modify other segmentor configs
SEGMENTOR_CFG['num_classes'] = 150
SEGMENTOR_CFG['backbone'] = {
    'type': 'SVT', 'structure_type': 'svt_small', 'pretrained': True, 'selected_indices': (0, 1, 2, 3), 'norm_cfg': {'type': 'LayerNorm'},
    'embed_dims': [64, 128, 256, 512], 'num_heads': [2, 4, 8, 16], 'mlp_ratios': [4, 4, 4, 4], 'depths': [2, 2, 10, 4], 
    'windiow_sizes': [7, 7, 7, 7], 'norm_after_stage': True, 'drop_path_rate': 0.2
}
SEGMENTOR_CFG['head'] = {
    'in_channels_list': [64, 128, 256, 512], 'feats_channels': 512, 'pool_scales': [1, 2, 3, 6], 'dropout': 0.1,
}
SEGMENTOR_CFG['auxiliary'] = {
    'in_channels': 256, 'out_channels': 512, 'dropout': 0.1,
}
SEGMENTOR_CFG['work_dir'] = os.path.split(__file__)[-1].split('.')[0]
SEGMENTOR_CFG['logger_handle_cfg']['logfilepath'] = os.path.join(SEGMENTOR_CFG['work_dir'], f"{os.path.split(__file__)[-1].split('.')[0]}.log")