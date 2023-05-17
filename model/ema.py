



from collections import OrderedDict
from torch.nn.parallel import DataParallel, DistributedDataParallel



def get_bare_model(network):
    """Get bare model, especially under wrapping with
    DistributedDataParallel or DataParallel.
    """
    if isinstance(network, (DataParallel, DistributedDataParallel)):
        network = network.module
    return network


def update_E(netG, netEMA, decay=0.999):
    model_params = OrderedDict(netG.named_parameters())
    shadow_params = OrderedDict(netEMA.named_parameters())
    for name, param in model_params.items():
        # see https://www.tensorflow.org/api_docs/python/tf/train/ExponentialMovingAverage
        # shadow_variable -= (1 - decay) * (shadow_variable - variable)
        shadow_params[name].sub_((1. - decay) * (shadow_params[name] - param))

    model_buffers = OrderedDict(netG.named_buffers())
    shadow_buffers = OrderedDict(netEMA.named_buffers())

    # check if both model contains the same set of keys
    assert model_buffers.keys() == shadow_buffers.keys()

    for name, buffer in model_buffers.items():
        # buffers are copied
        shadow_buffers[name].copy_(buffer)

