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

    void kalman(float[] mu, float[] Sigma, float[] H, float[] R, float[] data, float[] out_mu, float[] out_Sigma)
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

Given the ability to reason about matrix properties we can also encode several special simplifications that only exist in certain contexts

.. :math:
    
    X^T \rightarrow X \textrm{if} X \textrm{is symmetric}

Simplifications like this allow us to reduce the complexity of the computation before generating code. These simplifications are orthogonal to simplifications performed by standard compilers.

Encoding Linear Algebra
-----------------------

We attemt to encode te expert knowledge necessary for automated numerical linear algebra. While the field is mature the knowledge within it does not lend itself to a highly structured description in code. Additionally, any system that does encode the logic of linear algebra should be accessible to other mathematicians so that they can extend and verify its correctness.

With these goals in mind we encode the rules of linear algera into a logical programming framework so that rules like 

    XY is symmetric if X is symmetric and Y is symmetric

exist independently from how these logical rules are applied in the expression. This separates the mathematical code from algorithmic code allowing verification of one without deep understanding of the other.

Non-Confluence
--------------

There are multiple equally valid programs to compute a single matrix expression. For example when computing :math:`X\cdot Y\cdot Z` we can order the multiplies in two ways :math:`(X\cdot Y)\cdot Z` or :math:`X\cdot (Y\cdot Z)`. Alternatively when implementing a backsolve we must first factor the matrix. We may choose to peform a QR decompision or a LU decomposition with equal validity. In different contexts, either depending on the inputs or on the hardware one choice may be prefered.

We can step through all possibilities by implementing branching rules. If we have a cost model we can select the optimal program. 

We may also perform a guided search through this space with dynamic programming.

Code Generation
---------------

Finally from a simplified computation, a set of known facts, and a cost model we can generate BLAS/LAPACK code.

Outreach
--------

This system was translated to the Python project SymPy and offers full integration into the standard scientific computing stack. A matrix problem can be described, simplified, printed into C code, compiled and linked to a Python function transparently within an interactive session. This function can then be called using NumPy arrays, providing substantial speedups above traditional code.
