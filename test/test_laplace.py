# -*- coding: utf-8 -*-
#
import numpy
import pytest

import optimesh

from meshes import simple1, pacman


@pytest.mark.parametrize(
    "mesh, ref1, ref2, refi",
    [
        (simple1, 5.0, 2.1213203435596424, 1.0),
        (pacman, 1917.9950540725958, 74.99386491032608, 5.0),
    ],
)
def test_fixed_point(mesh, ref1, ref2, refi):
    X, cells = mesh()

    X, cells = optimesh.laplace.fixed_point(X, cells, 0.0, 10)

    # Test if we're dealing with the mesh we expect.
    nc = X.flatten()
    norm1 = numpy.linalg.norm(nc, ord=1)
    norm2 = numpy.linalg.norm(nc, ord=2)
    normi = numpy.linalg.norm(nc, ord=numpy.inf)

    tol = 1.0e-12
    assert abs(norm1 - ref1) < tol * ref1
    assert abs(norm2 - ref2) < tol * ref2
    assert abs(normi - refi) < tol * refi
    return


@pytest.mark.parametrize(
    "mesh, ref1, ref2, refi",
    [
        (simple1, 5.0, 2.1213203435596424, 1.0),
        (pacman, 1861.1845672600928, 73.12639677872326, 5.0),
    ],
)
def test_linear_solve(mesh, ref1, ref2, refi):
    X, cells = mesh()

    X, cells = optimesh.laplace.linear_solve(X, cells, 0.0, 10)

    # Test if we're dealing with the mesh we expect.
    nc = X.flatten()
    norm1 = numpy.linalg.norm(nc, ord=1)
    norm2 = numpy.linalg.norm(nc, ord=2)
    normi = numpy.linalg.norm(nc, ord=numpy.inf)

    tol = 1.0e-12
    assert abs(norm1 - ref1) < tol * ref1
    assert abs(norm2 - ref2) < tol * ref2
    assert abs(normi - refi) < tol * refi
    return