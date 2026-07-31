---
title: Modern Pandas
date: 2023-04-24
description: Will Pandas survive competition from Polars and DuckDB?
blogpost: true
author: Matthew Rocklin
category: writing
---

Modern Pandas
=============

Pandas is not beautiful.<br>
Pandas is not efficient.<br>
Pandas is not easy to learn.<br>
And yet... Pandas is *used*.

Every few years a new library tries to dethrone Pandas.
These never stick.

People don't switch libraries for 100% speedups.<br>
People don't switch libraries for nicer syntax.<br>
People switch libraries because the new library lets them do important things they couldn't do before.<br>
Winning on pure performance is hard without 10-100x speedups.
You need to cover the vast functionality Pandas offers, and then add something *new*.

The libraries that have survived haven't replaced pandas, they've *extended
it*, like Dask, GeoPandas, and RAPIDS.

However!  Today, there are a couple of challengers that feel different.  Maybe
Pandas' time has come.

## Will Polars and DuckDB replace Pandas?

Polars and DuckDB both provide 10x speedups, the ability to operate
efficiently on larger-than-memory datasets, have decent syntax (DuckDB with the
help of Ibis) and may have enough momentum behind them to gain the ecosystem
support necessary to displace the panda king.  This would be great!  🎉

Alternatively, Pandas could innovate and evolve, that would be great too!  🎉

This article lays out a vision for what it would mean for Pandas to innovate
itself into a position where current newcomers (polars, duckdb) have a lot to
offer, but probably not enough to disrupt the ecosystem.


## What do Polars and DuckDB offer over Pandas?

These libraries let you process more data at interactive speeds.  They let you
handle new data types (decimals, missing booleans, efficiently encoded
strings).  They accomplish this with a few important features:

- Efficient data type storage with Arrow
- Efficient handling of memory
- Multi-threaded parallel computing
- Query optimization
- SQL parsing (in the case of DuckDB)

## We're actually pretty close already

Pandas 2.0 was released recently.  It includes two major features
that people should be aware of, which handle the first two listed objectives.

1.  PyArrow data types, notably PyArrow strings

    Efficient data type storage with Arrow  ✅

2.  Copy-on-write

    Efficient handling of memory ✅

These defaults haven't been switched on yet, but they cover 80% of the use case
for these first two features.

Additionally Dask Dataframe (whose develoment collaborates tightly with Pandas)
provides parallel computing

- Multi-threaded parallel computing ✅

This leaves Query optimization and SQL parsing.  There are actually a couple of
ongoing experiments right now:

-  Query optimization ✅: https://github.com/mrocklin/dask-match
-  SQL Parsing ✅: https://github.com/dask-contrib/dask-sql with https://arrow.apache.org/datafusion/

Should these become more fully supported then we get the full featureset:

- Efficient data type storage with Arrow  ✅
- Efficient handling of memory ✅
- Multi-threaded parallel computing ✅
- Query optimization ✅
- SQL parsing (in the case of DuckDB) ✅

This provides a vision of a "Modern Pandas" that gets most of the benefits of
newer infrastructure and thinking, but also offers a smooth evolution path for
users and the greater ecosystem.

## Modern Pandas won't be as good

It's worth noting though that none of these efforts are likely to be as good as
a ground-up reinvention like Polars or DuckDB, which can tightly integrate all
of these features together, and without the inertia of legacy usage.

With the Modern Pandas approach these features are bolted-on after the fact,
taking the constraints of an ongoing userbase into consideration.  It's hard to
build a building perfectly when people still live inside during construction.

## Modern Pandas may be better

And yet these features aren't isolated to just this one use case.
Other related projects get these same benefits.  Other downstream pandas
libraries (geopandas, modin, ...) benefit from the pandas improvement.  Other
downstream Dask libraries (dask-image, xarray, ...) benefit from the query
optimization.  Other dataframe libraries (rapids) benefit from the SQL parsing.


## Final Reflections

I've been screwing around in the "better-than-pandas" space for the last decade
or so.  This is the first time I've thought "🤔 yeah, that might be a realistic
pandas 2.0".  I'm excited for that.  To be clear Dask will attach itself to
whatever system wins.  Dask follows users, whatever they choose.

I find myself mildly more enthusiastic about the "Modern Pandas" approach
though, mostly because I like to see communities grow and innovate from within.

Regardless, the next couple of years are going to be interesting for the Python
data space.  Either pandas will feel pressure to grow and innovate (🎉) or the
ecosystem will enter a somewhat fragmented period and we'll have to communciate
more and establish protocols.  Either way users will be better served after a
few years, and we'll have lots of thinking to do.
