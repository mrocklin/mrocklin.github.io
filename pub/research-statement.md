---
title: Research Statement
layout: default
---

**This is a work in progress. In particular, not all of it is yet true**

The goal of my research is to promote independent development of mathematical and algorithmic solutions in scientific computing. Problems in this domain require a depth of scientific, mathematical, and computational expertise which are hard to find in combination in a individual. My research endeavors to separate the scientific computing problem so that experts in each of these fields may contribute independently without close collaboration with the others. 

This is hard. Problems in scientific computing have high performance standards, and require tight integration between mathematical and algorithmic programmers. I have identified and developed a few abstractions in this field which allow for increased separability with minimal performance degradation. The projects below were designed to be composed to solve the problem of uncertainty propagation and be separably applicable to other domains.


Compiling Matrix Expressions into BLAS/LAPACK Calls
---------------------------------------------------

Many scientific problems may be compactly represented as a sequence of matrix expressions.  This motivated the development of BLAS and LAPACK, ubiquitous interfaces to libraries of dense linear algebra routines. They include thousands of well-tuned functions for special cases. While BLAS/LAPACK are very powerful their utility is limited by the ability of scientific programmers to select and call the correct sequence of subroutines to solve their problem.

We use logical programming, pattern matching, strategies, and a declarative definition of BLAS/LAPACK to compile a natural mathematical description of matrix expressions into a DAG of specific BLAS/LAPACK calls. We can then generate Fortran code that uses these libraries in a sensible way. We are able to gain substantial speedups not by implementing better algorithms but rather by selecting and composing the correct ones.


Static Scheduling onto Heterogeneous Architectures
--------------------------------------------------

We represent BLAS/LAPACK computations as a DAG. If we have a parallel machine we may wish to schedule the individual jobs onto the different resources. We may also wish to use hetergeneous compute nodes (e.g. CPUs + GPUs) if available.  Due to uncertainty of runtimes the scheduling task is traditionally done greedily and dynamically at runtime.

We analyze the feasiblity of static scheduling of array operations onto heterogeneous architecture using integer programming. This difficult problem is only feasible due to the following structure

1.  The regularity of array computations makes them preditable and modellable.
2.  The BLAS/LAPACK interface is implemented on a variety of hardware, exposing a common set of primtitives on heterogeneous compute nodes
3.  The small complexity of these DAGs enables the use of traditionally inaccessible NP-hard algorithms and their approximations.


DAG Ordering
------------

Finally, when we compute a single DAG on a sequential machine we select the order in which the tasks are executed. Several valid orderings may satisfy the data dependencies, giving us room to declare and satisfy additional policies. One such policy in the case of parallel scheduling would be to maximize communication/computation overlap by starting asynchronous transfer jobs as early as possible and starting blocking waits as late as possible.

We represent each policy (e.g. data-dependence or communication-overlap) as a separate DAG.  In general the policies will conflict so we also enforce a meta-policy DAG (e.g. data-dependence trumps communication-overlap).  We may then abstract this problem to the maximal union of a DAG of DAGs.  We must find a conglomerate DAG which contains as many edges from each DAG as possible, respecting their relative ordering.

The method to describe and conditionally merge DAGs is more general than asynchronous communication. We could express other desires (e.g. free memory as early as possible) with the same framework.  This declarative description of policies enables rapid prototyping by non-expert users.

Conclusion
----------

These projects are also designed to be composed so that they can solve scientific problems in concert.  They were also designed for independent use and development.  Care was taken so that the interface of each project is accessible to mathematical programmers.

The desired result is that different experts can contribute to specific projects in a pipeline without deep knowledge of the other components. My hope is that by separating these components we

1. Enable reuse and give moderately high performance computing to a wider audience.
2. Enable contributions from that wider audience back to HPC

Userbase Penetration
--------------------

This work is well integrated into open source projects with large communities. I have a small but growing userbase generating feedback.
