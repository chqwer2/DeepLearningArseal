
def get_model_mac(net, inp_shape = (3, 256, 256)):


    # pip install ptflops
    from ptflops import get_model_complexity_info
    FLOPS = 0
    macs, params = get_model_complexity_info(net, inp_shape, verbose=False, print_per_layer_stat=True)


    # params = float(params[:-4])
    # MACs (G) in log scale
    print(params)
    macs = float(macs[:-4]) + FLOPS / 10 ** 9


    print('mac', macs, params)



