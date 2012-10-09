---
layout: default 
title: Open source code 
---

This page describes the open source projects on [Matthew
Rocklin's](http://people.cs.uchicago.edu/~mrocklin) github page. It may
be slightly out of date.

If you'd prefer you can just go directly to [the standard github
page](http://github.com/mrocklin).

### Projects started by me

-   [APE](http://github.com/mrocklin/ape/): Static scheduling of
    array operations onto heterogeneous hardware. Wraps an MPI layer
    around the Theano project. Uses tompkins (see below) for
    scheduling.
-   [Matrix Algebra in
    Maude](http://github.com/mrocklin/matrix-algebra/): A tiny DSL
    for simplifying matrix expressions. It is written in the Maude
    system using rewrite rules. The eventual goal is to wrap the
    complexity of using BLAS and LAPACK into an easily expressible
    mathematical language.
-   [tompkins](http://github.com/mrocklin/tompkins/): A scheduler
    for computations on heterogeneous architectures including
    dependencies between tasks (represented as a DAG), and
    communication times. It solves the problem using an integer
    linear programming method described in an article by Tompkins.
    This code attempts to translate his math into clear Python code.
    Section and equation numbers are included. Uses the pulp library
    to describe the ILP.
-   [Shallow Water](http://github.com/mrocklin/ShallowWater/): A
    time dependent solver for the Shallow Water equations. This code
    uses numpy or Theano for low level computation. It was designed
    to demonstrate how mathematical solvers can be written clearly
    in a high-level language and use libraries for efficient
    low-level computation. This serves as an example of an important
    computation that can be well expressed using only array
    primitives.
-   [mailFeed](http://github.com/mrocklin/mailFeed): A simple Python
    library to automate the collection of e-mail from a remote
    server.
-   [HITS](http://github.com/mrocklin/hits): A simple web-app
    written in Clojure to collect, query, and interact with data
    from git repositories.
-   [gha](http://github.com/mrocklin/gha): A conglomeration of
    projects that analyze github. Mostly an exercise in large-graph
    interactions.

### Projects to which I contribute

-   [SymPy](http://github.com/mrocklin/sympy): A symbolic
    mathematics library within Python. Similar to Mathematica or
    Maple. I am the main contributor to the statistics and symbolic
    matrix expression modules.
-   [Theano](http://github.com/mrocklin/theano): A library that
    bridges the symbolics-numerics gap. The APE project mentioned
    above uses Theano as a backend. Much of the APE work is pushed
    upstream. My contributions in Theano are largely based around
    graph manipulation, concurrency, MPI, and rudimentary scheduling
    algorithms.
