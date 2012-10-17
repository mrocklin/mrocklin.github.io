Matrix Expressions
==================

Linear algebra is well understood by both scientists and computers. 

Scientists are able to describe a wide variety of problems, such as the Kalman Filter presented below, as matrix expressions

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

Mathematically this field is very mature and well understood. Matrices have attributes like symmetry, conditioning, positive definiteness, etc... which supply a rich context in which algrorithms may be selected. 

Computers also have a mature understanding of linear algebra. Libraries like BLAS and LAPACK provide highly optimized code on a variety of architectures. There are several routines for various operations which can be used in different contexts. The Kalman filter above can be written in BLAS and LAPACK as follows

.. code-block:: C

    void kalman(float[] mu, float[] Sigma, float[] H, float[] R, float[] data)
    {
    ...
    }

In the ``C`` code there are routines like ``GEMM`` and ``SYMM``. Each of these routines performs a matrix multiply but ``SYMM`` is a more efficient routine that can be applied only when one of its arguments is symmetric. While the code above is far more compact than a naive implementation, the BLAS and LAPACK interfaces remain challenging for non-expert users. Even expert users may neglect to use ``SYMM`` instead of ``GEMM``. This may be because the added complexity of a wider interface or because they have forgotten or were never aware that ``Sigma`` was symmetric.

In this project we build a translator from matrix expressions to BLAS/LAPACK code.

Reasoning about Matrix Properties
---------------------------------

Given that ``A`` and ``B`` are matrices and that ``A`` is symmetric we can reason that ``B'AB`` must also be symmetric. In order to fully use the special routines in BLAS and LAPACK we will need to teach computers to reason about matrix expressions in the same way. We implement this by creating a logic programming system.

Simplification
--------------

Given the ability to reason about matrix properties we can also encode several special simplifications that only exist in certain contexts for example

.. :math:
    
    X^T \rightarrow X \textrm{if} X \textrm{is symmetric}

Simplifications like this allow us to reduce the complexity of the computation before generating code. These simplifications are orthogonal to simplifications performed by standard compilers.

Code Generation
---------------

Finally from a simplified computation and set of known facts we can generate BLAS/LAPACK code.

Outreach
--------

This system was translated to the Python project SymPy and offers full integration into the standard scientific computing stack. A matrix problem can be described, simplified, printed into C code, compiled and linked to a Python function transparently within an interactive session. This function can then be called using NumPy arrays, providing substantial speedups above traditional code.
