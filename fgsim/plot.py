import matplotlib.pyplot as plt

from .config import conf


def plot3d(arr):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    ax.scatter(*arr)
    ax.set_xlabel("X Label")
    ax.set_ylabel("Y Label")
    ax.set_zlabel("Z Label")
    fig.savefig(f"wd/{conf.tag}/plot_posD_3d.png")


def plot_z_pos(foo, zval):
    fig = plt.figure()
    ax = fig.add_subplot()

    arr = foo[foo[..., 2] == zval]
    ax.scatter(arr[:, 0], arr[:, 1])
    fig.savefig(f"wd/{conf.tag}/plot_posD_2d.png")


def plotlosses(losses_g, losses_d):
    from matplotlib import pyplot as plt

    # plot and save the generator and discriminator loss
    plt.figure()
    plt.plot(losses_g, label="Generator loss")
    plt.plot(losses_d, label="Discriminator Loss")
    plt.legend()
    plt.savefig(f"wd/{conf.tag}/loss.png")
