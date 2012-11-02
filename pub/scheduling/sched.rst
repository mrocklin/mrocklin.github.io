Static Scheduling of Array Computations on Heterogeneous Architectures
======================================================================

Challenges
----------

Computational machinery grows more distributed and more heterogeneous. This
burdens computational scientists who want to effectively use their hardware. In
particular it is challenging to precompute an optimal schedule for a particular
computation on a particular set of machines for the following reasons

1.  Algorithms to compute optimal solutions to scheduling problems are NP-Hard and the complexity of the relevant programs is often high.
2.  The runtimes of the components of the computation are difficult to predict
3.  Different computational machines within the system may require separate code to be written

As a result most schedulers resort to dynamic techniques, allocating jobs greedily as new resources come online. While this is a robust technique for general programming it may not be appropriate for computational kernels in a high performance setting.

Simplified context: Array operations
------------------------------------

We approach the static scheduling program in a simplified context. We only consider computations with bulk array primitives. In this sense we can describe programs like the following

.. code-block:: python

    C = dot(A, B)
    D = solve(A, x) + C

But not programs like the following

.. code-block:: C

    for(int i = 0; i < n; i++)
        for(int j = 0; j < m; j++)
            for(int k = 0; k < l; k++)
                C[i, j] = A[i, k] * B[k, j]

In practice restricting programmers to the higher level abstractions does not significantly lessen programmer expressivity.

In this context the challenges of optimal static scheduling are reduced:

1.  NP-Hard: Algorithms are still NP-Hard but computaitons can often be written with very few operations. Some NP-Hard algorithms can be run in reasonable times on this small scale.
2.  Predictability: Array computations are very regular and are often predictable even in complex memory hierarchies. See [references]
3.  Heterogeneity: Array operations are well supported by popular libraries (BLAS/LAPACK) and optimized implementations with a common interface exist on a variety of architectures.

In this work we show how a variety of computational kernels can be described with array primitives. We specify a few heterogeneous networks and schedule these computations onto these networks with two static scheduling algorithms. 

describe a few computations with array primitive operations, schedule them on a variety of networks using two static scheduling algorithms and run and

Background - Static Scheduling onto Heterogeneous Architecture 
--------------------------------------------------------------

List Scheduling
~~~~~~~~~~~~~~~

Integer Programming Solution
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Computations
------------

We construct the following computations naturally with array primitives.

The Kalman Filter
~~~~~~~~~~~~~~~~~

The Kalman filter is a standard algorithm in data assimilation. It is the Bayes update in the case when all varibles and measurements follow a multivariate normal distribution. This is a dominating assumption in practice and so this computation is used widely. It is used in a variety of contexts ranging from numerical weather prediction run on large super computers, to unmanned vehicle flight and in-car GPS navigation run on embedded hardware.

Given variables :math:`\mu` and :math:`\Sigma` represent the mean and variance of the prior,  :math:`H` represents an observation operator, :math:`R` the known variance of the measurement and :math:`data`, the observed measurement, we can fully describe the Kalman filter with the following matrix expressions

.. math:: 

    \mu' = 
    \begin{smallmatrix}
        \mu + \Sigma H^T \left(R + H \Sigma H^T\right)^{-1} 
        \left(  H \mu - data\right)
    \end{smallmatrix}

.. math:: 

    \Sigma' = 
    \begin{smallmatrix}
        \left(\mathbb{I} - 
        \Sigma H^T \left(R + H \Sigma H^T\right)^{-1} H\right) \Sigma
    \end{smallmatrix}

*TODO: add more computations*

Networks
--------

Parallel computations of this sort are often implemented by an expert for a particular architecture. Because we have separated the scheduling problem we can describe our computations separately from the hardware on which they will run. We may now explore both spaces independently.

We consider each of these computations on a variety of networks

1.  A single CPU-GPU pair
2.  A local machine with distant access to a small cluster
3.  A small cluster of machines, some of which have GPUs

These networks are common in moderate performace computing settings and stress the heterogeneity of both compute devices and interconnects.

Outreach
--------

We provide interfaces for this project to popular computing libraries in the Python scientific computing ecosystem.
