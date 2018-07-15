import mxnet
from mxnet import gluon
import mxnet.gluon.nn as nn

class DecomposableAtten(gluon.Block):
    def __init__(self, hidden_size: int, inp_size: int, **kwargs):
        super(DecomposableAtten, self).__init__(**kwargs)
        with self.name_scope():
            self.f1 = nn.Dense(inp_size)
            self.

