import torch
import torch.nn as nn


class CNNBlock(nn.Module):
    def __init__(self, in_channels, out_channels, bn_act = True, **kwargs):
        super.__init__()
        self.conv = nn.Conv2d(in_channels, out_channels, bias = not bn_act, **kwargs)
        self.bn = nn.BatchNorm2d(out_channels)
        self.leaky = nn.LeakyReLU(0.1)
        self.use_bn_act = bn_act

    def forward(self, x):
        if self.use_bn_act:
            return self.leaky(self.bn(self.conv(x)))
        else:
            return self.conv(x)
        

class ResidualBlock(nn.Module):
    def __init__(self, channels, use_residual=True, num_repeats=1):
        super.__init__()
        self.layers = nn.ModuleList
        for repeat in num_repeats:
            self.layers += [
                CNNBlock
            ]


class ScalePrediction(nn.Module):
    pass


class YOLOv3(nn.Module):
    pass