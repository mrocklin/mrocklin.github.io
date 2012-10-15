---
title: Research Statement
layout: default
---

**This is a work in progress. In particular, not all of it is true yet**

The goal of my research is to promote independent development of mathematical and algorithmic solutions in scientific computing. Problems in this domain require a depth of scientific, mathematical, and computational expertise which are hard to find in combination in a single individual. My research endeavors to separate the scientific computing problem so that experts in each of these fields may contribute independently without close collaboration with the others. 

This is hard. Problems in scientific computing have very high performance standards, and often require tight integration between mathematical and algorithmic programmers. I have identified and developed a few separations in this field which allow for increased separability with minimal performance degradation. The projects listed below were designed to be composed to solve the problem of uncertainty propagation when used together but to also be generally applicable to other domains.

Array Primitives
----------------

The majority of time spent in scientific applications is spent in the manipulation of arrays. Algorithmically matrix operations are well studied, highly optimized on a variety of architectures, and very regular/predictable. Mathematically linear algebra is known by many mathematical programmers and benefits from a rich theory. For many (but not all) of the projects listed below we restrict ourselves to a reduced programming paradigm that uses only bulk array operations as primitives. 

Array operations form a set of primitives which can describe many engineering and scientific computations with very little complexity and very little loss of programmer expressivity. Applications like the Kalman filter, PDE solvers, and common optimization algorithms can all be written with 10-100 operations. This reduced description enables the use of exhaustive NP-hard algorithms that were infeasible when considering these problems when written in general languages.

### A Language, Theano

My work provides general infrastructure to any computation described as a DAG. For experimentation we use a front-end provided by the Theano project. Theano presents a MatLab like language to the user and delivers a convenient DAG form as output. Separately, Theano also performs standard compiler optimizations (loop fusion, common subexpressions, ...) and conveniently delivers both CPU and GPU implementations of many array operations. I use Theano for the following purposes:

1. As an input language
2. As a compiler of some optimizations (i.e. loop fusion)
3. As a code generator for local low-level array code on CPUs and GPUs

Scheduling
----------

I pose the scheduling problem as an mixed integer linear program and solve it for some common problems. I study the suitability of this method over heterogeneous architectures. Static scheduling and integer programming is possible because of the predictability of array primitives and the low complexity of scientific computations in this language.

DAG Ordering
------------

We often represent general computations as a DAG where nodes are tasks and edges represent data dependencies. When this DAG is run on a single sequential machine we must select the order in which the tasks are run. In general there are several valid orders that satisfy the data dependencies. When some jobs are asynchronous (as happens when communication with other computers is considered) then the order in which jobs are executed can significantly impact runtime. 

I solve this problem by posing and solving a more general problem. We want our orderings to satisfy a sequence of desires. The desires for the asynchronous problems above might be 

1. Satisfy data dependencies 
2. Run asynchronous jobs as early as possible and blocking waits as late as possible
3. Avoid deadlocks

Each desire can be expressed as a separate DAG. We merge these DAGs (collect as many dependencies/edges as possible) while still maintaining the DAG property. I show how this formulation leads to reasonable orderings which overlap communication and computation and avoid deadlocks automatically.

The method to describe and conditionally merge DAGs is far more general than asynchronous communication however. We could express other desires, such as the desire to free memory as early as possible, just as easily. I expose this multi-dag ordering mechanism to mathematical programmers in the Theano project, allowing for a high-level description of ordering policy. This enables rapid prototyping and experimentation of different policies.

Matrix Expressions
------------------

I have created a small language to describe and reason about matrix expressions mathematically. In contrast to numeric systems this project reasons about the mathematical qualities of matrices and linear operators. By enabling a computer to infer properties such as symmetry, positive definiteness, and poor conditioning, I am able to generate better informed numeric code. 

In particular I translate matrix expressions into BLAS and LAPACk programs. These libraries contain different routines for different mathematical contexts (such as a more efficient routine that may be used when a matrix is symmetric). Despite being highly optimized BLAS and LAPACK are rarely used by novice scientific programmers due to a challenging interface. Additionally the specialized routines are rarely used even by expert programmers because it is challenging to consistently reason mathematically and numerically at the same time. By generating mathematically informed code I pose that we can gain a fair fraction on top of expert code and an order of magnitude over novice code.

Stats
-----

SymPy stats:  SymPy stats introduces a random variable type into a mathematical modeling language, SymPy, allowing users to construct and query stochastic models. Queries on expressions that contain multivariate normal random variables generate matrix expressions, effectively turning a specialized computational problem (uncertainty quantification) into a very general one (numeric linear algebra). This can be composed with the Matrix Expressions project above.

Conclusion
----------

Each of these projects is designed to encapsulate exactly one body of expert knowledge. These projects are also designed to be composed so that they can solve scientific problems in concert. The desired result is that different experts can contribute to specific projects in a pipeline without deep knowledge of the other components. My hope is that by separating these components we

1. Enable reuse and give moderately high performance computing to a wider audience.
2. Enable contributions from that wider audience back to HPC
