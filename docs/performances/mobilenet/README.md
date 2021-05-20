# Introduction
```
@inproceedings{sandler2018mobilenetv2,
    title={Mobilenetv2: Inverted residuals and linear bottlenecks},
    author={Sandler, Mark and Howard, Andrew and Zhu, Menglong and Zhmoginov, Andrey and Chen, Liang-Chieh},
    booktitle={Proceedings of the IEEE conference on computer vision and pattern recognition},
    pages={4510--4520},
    year={2018}
}
@inproceedings{Howard_2019_ICCV,
    title={Searching for MobileNetV3},
    author={Howard, Andrew and Sandler, Mark and Chu, Grace and Chen, Liang-Chieh and Chen, Bo and Tan, Mingxing and Wang, Weijun and Zhu, Yukun and Pang, Ruoming and Vasudevan, Vijay and Le, Quoc V. and Adam, Hartwig},
    booktitle={The IEEE International Conference on Computer Vision (ICCV)},
    pages={1314-1324},
    month={October},
    year={2019},
    doi={10.1109/ICCV.2019.00140}}
}
All the reported models here are available at https://pan.baidu.com/s/1nPxHw5Px7a7jZMiX-ZxRhA (code is 3jvr)
```


# Results

## PASCAL VOC
| Model         | Backbone | Crop Size  | Schedule                             | Train/Eval Set  | mIoU   | Download                 |
| :-:           | :-:      | :-:        | :-:                                  | :-:             | :-:    | :-:                      |
| FCN           | M-V2-D8  | 512x512    | LR/POLICY/BS/EPOCH: 0.01/poly/16/60  | trainaug/val    | 59.89% | [model]() &#124; [log]() |
| PSPNet        | M-V2-D8  | 512x512    | LR/POLICY/BS/EPOCH: 0.01/poly/16/60  | trainaug/val    | 68.40% | [model]() &#124; [log]() |
| DeepLabV3     | M-V2-D8  | 512x512    | LR/POLICY/BS/EPOCH: 0.01/poly/16/60  | trainaug/val    | 70.08% | [model]() &#124; [log]() |
| DeepLabV3plus | M-V2-D8  | 512x512    | LR/POLICY/BS/EPOCH: 0.01/poly/16/60  | trainaug/val    | 70.04% | [model]() &#124; [log]() |
| LRASPPNet     | M-V3S-D8 | 512x512    | LR/POLICY/BS/EPOCH: 0.01/poly/16/180 | trainaug/val    | 62.13% | [model]() &#124; [log]() |
| LRASPPNet     | M-V3L-D8 | 512x512    | LR/POLICY/BS/EPOCH: 0.01/poly/16/180 | trainaug/val    | 67.90% | [model]() &#124; [log]() |

## ADE20k
| Model         | Backbone | Crop Size  | Schedule                             | Train/Eval Set  | mIoU   | Download                 |
| :-:           | :-:      | :-:        | :-:                                  | :-:             | :-:    | :-:                      |
| FCN           | M-V2-D8  | 512x512    | LR/POLICY/BS/EPOCH: 0.01/poly/16/130 | train/val       | 30.85% | [model]() &#124; [log]() |
| PSPNet        | M-V2-D8  | 512x512    | LR/POLICY/BS/EPOCH: 0.01/poly/16/130 | train/val       | 35.09% | [model]() &#124; [log]() |
| DeepLabV3     | M-V2-D8  | 512x512    | LR/POLICY/BS/EPOCH: 0.01/poly/16/130 | train/val       | 37.55% | [model]() &#124; [log]() |
| DeepLabV3plus | M-V2-D8  | 512x512    | LR/POLICY/BS/EPOCH: 0.01/poly/16/130 | train/val       | 37.66% | [model]() &#124; [log]() |
| LRASPPNet     | M-V3S-D8 | 512x512    | LR/POLICY/BS/EPOCH: 0.01/poly/16/390 | train/val       | 26.09% | [model]() &#124; [log]() |
| LRASPPNet     | M-V3L-D8 | 512x512    | LR/POLICY/BS/EPOCH: 0.01/poly/16/390 | train/val       | 30.06% | [model]() &#124; [log]() |

## CityScapes
| Model         | Backbone | Crop Size  | Schedule                             | Train/Eval Set  | mIoU   | Download                 |
| :-:           | :-:      | :-:        | :-:                                  | :-:             | :-:    | :-:                      |
| FCN           | M-V2-D8  | 512x1024   | LR/POLICY/BS/EPOCH: 0.01/poly/8/220  | train/val       | 70.77% | [model]() &#124; [log]() |
| PSPNet        | M-V2-D8  | 512x1024   | LR/POLICY/BS/EPOCH: 0.01/poly/8/220  | train/val       | 73.64% | [model]() &#124; [log]() |
| DeepLabV3     | M-V2-D8  | 512x1024   | LR/POLICY/BS/EPOCH: 0.01/poly/8/220  | train/val       | 76.74% | [model]() &#124; [log]() |
| DeepLabV3plus | M-V2-D8  | 512x1024   | LR/POLICY/BS/EPOCH: 0.01/poly/8/220  | train/val       | 76.68% | [model]() &#124; [log]() |
| LRASPPNet     | M-V3S-D8 | 512x1024   | LR/POLICY/BS/EPOCH: 0.01/poly/16/660 | train/val       | 65.06% | [model]() &#124; [log]() |
| LRASPPNet     | M-V3L-D8 | 512x1024   | LR/POLICY/BS/EPOCH: 0.01/poly/16/660 | train/val       | 69.98% | [model]() &#124; [log]() |