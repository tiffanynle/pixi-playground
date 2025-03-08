import jax.numpy as jnp


def test_array():
    a = jnp.arange(3)
    print(a.devices())
    assert False
