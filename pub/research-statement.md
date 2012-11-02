---
title: Research Statement
layout: default
---

**This is a work in progress. In particular, not all of it is true yet**

The goal of my research is to promote independent development of mathematical and algorithmic solutions in scientific computing. Problems in this domain require a depth of scientific, mathematical, and computational expertise which are hard to find in combination in a single individual. My research endeavors to separate the scientific computing problem so that experts in each of these fields may contribute independently without close collaboration with the others. 

This is hard. Problems in scientific computing have high performance standards, and require tight integration between mathematical and algorithmic programmers. I have identified and developed a few separations in this field which allow for increased separability with minimal performance degradation. The projects below were designed to be composed to solve the problem of uncertainty propagation and be separably applicable to other domains.

Array Primitives
----------------

The majority of time spent in scientific applications is spent in the manipulation of arrays. Matrix algorithms are well studied, highly optimized on a variety of architectures, and very predictable. Linear algebra is also well known by mathematical programmers. For many of the projects listed below I restrict myself to a reduced programming paradigm that uses only bulk array operations as primitives. 

Array operations form a set of primitives which can describe many engineering and scientific computations with very little complexity and very little loss of programmer expressivity. Applications like the Kalman filter, PDE solvers, and common optimization algorithms can all be written with 10-100 operations. This reduced description enables the use of NP-hard algorithms that were infeasible when considering these problems when written in general languages.

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

We represent a computation as a directed acyclic graph (DAG) where nodes are tasks and directed edges are data dependencies. When a DAG is run on a sequential machine we select the order in which the tasks are executed. Several orders satisfy the data dependencies. When asynchronous jobs exist (as is the case with parallel communication) then the order in which jobs are executed can significantly impact runtime. How can we select the best ordering for a given DAG?

I solve this problem by posing and solving a more general problem. We want our orderings to satisfy a sequence of desires. The desires for the asynchronous problem above might be 

1.  Satisfy data dependencies 
2.  Run asynchronous jobs as early as possible and blocking waits as late as possible
3.  Avoid deadlocks

Each desire can be expressed as a separate DAG. We reduce the communication-compiutation overlap problem to the optimal merger of a sequence of DAGs in such a way that maintains the acyclic property and throws away the least number of important edges. I show how this formulation leads to reasonable orderings which overlap communication and computation and avoid deadlocks.

The method to describe and conditionally merge DAGs is more general than asynchronous communication. We could express other desires (e.g. free memory as early as possible) with the same framework. I expose the multi-dag ordering mechanism to mathematical programmers by taking in a sequence of comparator functions. This allows for a declarative and accessible description of ordering policy. This enables rapid prototyping and experimentation of different policies. This is implemented in a popular numerical computing and machine learning package, Theano. 

Mathematical Matrix Compilation
-------------------------------

I have a small language to describe and reason about matrix expressions mathematically. In contrast to numeric systems this project reasons about the mathematical attributes of matrices. By enabling a computer to infer properties such as symmetry, positive definiteness, and conditioning, we are able to generate better informed numeric code. 

In particular I translate matrix expressions into BLAS and LAPACK programs. These libraries contain different routines for different mathematical contexts. For example there is a more efficient multiply routine that may be used when a matrix is symmetric. Despite being highly optimized BLAS and LAPACK are rarely used by novice scientific programmers due to a challenging interface. Additionally the specialized routines (like symmetric matrix multiply) are rarely used even by expert programmers because it is challenging to consistently reason mathematically and numerically at the same time. 

We interface a logical programming framework to a computer algebra system to generate DAGs of BLAS/LAPACK calls from high-level code. We also provide a translation from this DAG to low-level Fortran code. We are able to gain substantial speedups not by implementing better algorithms but rather by using the correct ones.

Stats
-----

SymPy stats:  SymPy stats introduces a random variable type into a mathematical modeling language, SymPy, allowing users to construct and query stochastic models. Queries on expressions that contain multivariate normal random variables generate matrix expressions, effectively turning a specialized computational problem (uncertainty quantification) into a very general one (numeric linear algebra). 

Conclusion
----------

Each of these projects is designed to encapsulate exactly one body of expert knowledge. These projects are also designed to be composed so that they can solve scientific problems in concert. The desired result is that different experts can contribute to specific projects in a pipeline without deep knowledge of the other components. My hope is that by separating these components we

1. Enable reuse and give moderately high performance computing to a wider audience.
2. Enable contributions from that wider audience back to HPC
