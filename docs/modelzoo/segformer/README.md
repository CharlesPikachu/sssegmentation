## Introduction

<a href="https://github.com/NVlabs/SegFormer">Official Repo</a>

<a href="https://github.com/SegmentationBLWX/sssegmentation/blob/main/ssseg/modules/models/segmentors/segformer/segformer.py">Code Snippet</a>

<details>
<summary align="left"><a href="https://arxiv.org/pdf/2105.15203.pdf">SegFormer (NeurIPS'2021)</a></summary>

```latex
@article{xie2021segformer,
    title={SegFormer: Simple and Efficient Design for Semantic Segmentation with Transformers},
    author={Xie, Enze and Wang, Wenhai and Yu, Zhiding and Anandkumar, Anima and Alvarez, Jose M and Luo, Ping},
    journal={arXiv preprint arXiv:2105.15203},
    year={2021}
}
```

</details>


## Results

#### PASCAL VOC

| Backbone    | Pretrain               | Crop Size  | Schedule                                | Train/Eval Set     | mIoU   | Download                                                                                                                                                                                                                                                                                                                                                                     |
| :-:         | :-:                    | :-:        | :-:                                     | :-:                | :-:    | :-:                                                                                                                                                                                                                                                                                                                                                                          |
| MIT-B1      | ImageNet-1k-224x224    | 512x512    | LR/POLICY/BS/EPOCH: 0.00006/poly/16/60  | trainaug/val       | 77.46% | [cfg](https://raw.githubusercontent.com/SegmentationBLWX/sssegmentation/main/ssseg/configs/segformer/segformer_mitb1_voc.py) &#124; [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_segformer/segformer_mitb1_voc.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_segformer/segformer_mitb1_voc.log) |
| MIT-B3      | ImageNet-1k-224x224    | 512x512    | LR/POLICY/BS/EPOCH: 0.00006/poly/16/60  | trainaug/val       | 81.98% | [cfg](https://raw.githubusercontent.com/SegmentationBLWX/sssegmentation/main/ssseg/configs/segformer/segformer_mitb3_voc.py) &#124; [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_segformer/segformer_mitb3_voc.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_segformer/segformer_mitb3_voc.log) |

#### ADE20k

| Backbone    | Pretrain               | Crop Size  | Schedule                                | Train/Eval Set  | mIoU   | Download                                                                                                                                                                                                                                                                                                                                                                              |
| :-:         | :-:                    | :-:        | :-:                                     | :-:             | :-:    | :-:                                                                                                                                                                                                                                                                                                                                                                                   |
| MIT-B0      | ImageNet-1k-224x224    | 512x512    | LR/POLICY/BS/EPOCH: 0.00006/poly/16/130 | train/val       | 37.57% | [cfg](https://raw.githubusercontent.com/SegmentationBLWX/sssegmentation/main/ssseg/configs/segformer/segformer_mitb0_ade20k.py) &#124; [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_segformer/segformer_mitb0_ade20k.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_segformer/segformer_mitb0_ade20k.log) |
| MIT-B1      | ImageNet-1k-224x224    | 512x512    | LR/POLICY/BS/EPOCH: 0.00006/poly/16/130 | train/val       | 42.25% | [cfg](https://raw.githubusercontent.com/SegmentationBLWX/sssegmentation/main/ssseg/configs/segformer/segformer_mitb1_ade20k.py) &#124; [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_segformer/segformer_mitb1_ade20k.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_segformer/segformer_mitb1_ade20k.log) |
| MIT-B2      | ImageNet-1k-224x224    | 512x512    | LR/POLICY/BS/EPOCH: 0.00006/poly/16/130 | train/val       | 46.35% | [cfg](https://raw.githubusercontent.com/SegmentationBLWX/sssegmentation/main/ssseg/configs/segformer/segformer_mitb2_ade20k.py) &#124; [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_segformer/segformer_mitb2_ade20k.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_segformer/segformer_mitb2_ade20k.log) |
| MIT-B3      | ImageNet-1k-224x224    | 512x512    | LR/POLICY/BS/EPOCH: 0.00006/poly/16/130 | train/val       | 48.31% | [cfg](https://raw.githubusercontent.com/SegmentationBLWX/sssegmentation/main/ssseg/configs/segformer/segformer_mitb3_ade20k.py) &#124; [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_segformer/segformer_mitb3_ade20k.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_segformer/segformer_mitb3_ade20k.log) |
| MIT-B4      | ImageNet-1k-224x224    | 512x512    | LR/POLICY/BS/EPOCH: 0.00006/poly/16/130 | train/val       | 48.59% | [cfg](https://raw.githubusercontent.com/SegmentationBLWX/sssegmentation/main/ssseg/configs/segformer/segformer_mitb4_ade20k.py) &#124; [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_segformer/segformer_mitb4_ade20k.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_segformer/segformer_mitb4_ade20k.log) |
| MIT-B5      | ImageNet-1k-224x224    | 512x512    | LR/POLICY/BS/EPOCH: 0.00006/poly/16/130 | train/val       | 49.61% | [cfg](https://raw.githubusercontent.com/SegmentationBLWX/sssegmentation/main/ssseg/configs/segformer/segformer_mitb5_ade20k.py) &#124; [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_segformer/segformer_mitb5_ade20k.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_segformer/segformer_mitb5_ade20k.log) |

#### CityScapes

| Backbone    | Pretrain               | Crop Size  | Schedule                                | Train/Eval Set  | mIoU   | Download                                                                                                                                                                                                                                                                                                                                                                                          |
| :-:         | :-:                    | :-:        | :-:                                     | :-:             | :-:    | :-:                                                                                                                                                                                                                                                                                                                                                                                               |
| MIT-B1      | ImageNet-1k-224x224    | 1024x1024  | LR/POLICY/BS/EPOCH: 0.00006/poly/8/440  | train/val       |        | [cfg](https://raw.githubusercontent.com/SegmentationBLWX/sssegmentation/main/ssseg/configs/segformer/segformer_mitb1_cityscapes.py) &#124; [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_segformer/segformer_mitb1_cityscapes.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_segformer/segformer_mitb1_cityscapes.log) |
| MIT-B3      | ImageNet-1k-224x224    | 1024x1024  | LR/POLICY/BS/EPOCH: 0.00006/poly/8/440  | train/val       |        | [cfg](https://raw.githubusercontent.com/SegmentationBLWX/sssegmentation/main/ssseg/configs/segformer/segformer_mitb3_cityscapes.py) &#124; [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_segformer/segformer_mitb3_cityscapes.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_segformer/segformer_mitb3_cityscapes.log) |


## More

You can also download the model weights from following sources:

- BaiduNetdisk: https://pan.baidu.com/s/1gD-NJJWOtaHCtB0qHE79rA with access code **s757**