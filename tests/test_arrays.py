import jax.numpy as jnp
import numpy as np


def test_array():
    a = jnp.arange(3)
    print(a.devices())
    assert False
