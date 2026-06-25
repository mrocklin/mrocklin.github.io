---
title: Frisky and Xarray Example
date: 2026-06-25
tagline: Dask in Rust driving Xarray
description: Let's run Xarray workloads on this new thing I built, Frisky, a Dask scheduler in Rust.
blogpost: true
author: Matthew Rocklin
---

# Frisky and Xarray Example

A couple months ago I was doing some consulting work for a finance group that used Dask and Xarray at the ~10 TiB scale.  It was slow.  I decided to make it faster.

What resulted was three weeks of AI development on a couple historical projects I had mothballed,

-  [`frisky`](https://getfrisky.dev), a Rust implementation of the Dask scheduler
-  [`dask-array`](https://github.com/mrocklin/dask-array), query optimization for dask arrays, and now also written in Rust

Both are now available on PyPI and, when combined with git main versions of `dask` and `xarray`, form a system for Xarray computations that is high performance, and usually doesn't break :)

## Pain

If you suffer from the following, then this is for you:

-  Large task graphs (over a million)
-  Long wait times before things happen on the dashboard
-  Sensitivity to chunk size
-  Rechunking generally

## Solution

It's hard to convey everything that goes into making something fast.  I use "Rust!" above as a catch-all that people today seem to latch onto, but real performance has much more to do with thoroughness and diligent attention to detail over hundreds of iterations.  It goes well beyond a choice of language.

I don't know how to capture that in words, so instead I'll just show you, and hope it comes across.

<div class="video-container">
<iframe src="https://www.youtube.com/embed/aie_7ElUq9w?si=Md96L-kJ2hr4L06A" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>

## Try it out

Install these things:

```
frisky>=0.3.0
dask-array>=0.3.0
git+https://github.com/dask/dask@main
git+https://github.com/pydata/xarray@main
```

At the top of your Xarray code, run this to use the new `dask-array` package instead of `dask.array`:

```python
from dask_array.xarray import register
register()
```

And then around your Dask Client, do this to turn your Dask cluster into a Frisky cluster:

```python
from frisky import hijack
client = hijack(client)
```

And then run as normal.  Enjoy.

If you don't have a Dask/Xarray workload handy, just run the Frisky demo:

```
$ frisky demo
```
And report the inevitable issues at
[github.com/mrocklin/frisky-issues](https://github.com/mrocklin/frisky-issues)

Have fun!
