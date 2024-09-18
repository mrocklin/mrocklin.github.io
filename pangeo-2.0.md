---
title: What Does Pangeo 2.0 Look Like?
date: 2024-09-18
description: Past, present, and future of scalable geoscience in Python
blogpost: true
author: Matthew Rocklin
---


What does Pangeo 2.0 Look Like?
===============================

<img src="https://global.discourse-cdn.com/standard14/uploads/pangeo/original/1X/657e3c5e0885ee4e5c2062c58f9aa094fa4b14a4.png" width="40%" />


Past
----

In January 2018 I published a blogpost titled [Pangeo: JupyterHub, Dask, and XArray on the Cloud](https://matthewrocklin.com/blog/work/2018/01/22/pangeo-2), which introduced a new architecture for running scalable Python computations on the cloud using ...

- GCP
- Kubernetes
- Dask \+ Xarray
- Dask-Kubernetes (actually named Daskernetes at the time)
- Zarr (a brand new file format at the time)

This architecture was unveiled during an AMS workshop keynote, the 3-minute demo video of which is still available if you want a blast from the past:

<iframe width="560" height="315" src="https://www.youtube.com/embed/rSOJKbfNBNk?si=7yM7Fi1VIxLvGGcx" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

This coordinated work from many people.

### What was great about the Pangeo stack

This effort was impressive, and showed that it was possible to …

- Do large scale multi-dimensional distributed computing
- … from Python
- … on the cloud
- … interactively
- … for anyone with access to the internet

This was quite different from the standard at the time in the scientific/geo space, which was MPI codes or batch jobs run on supercomputers.  The Pangeo effort upended the status-quo at many scientific and government agencies trying to enable access and analytics on larger scale data.

### What was terrible about the Pangeo stack

Unfortunately, there were challenges with this stack:

1. **Kubernetes:** It required expertise of Kubernetes, and that expertise was rare

   *"What’s a pod?  Is it a Docker?  How do I upload a pod?"*

2. **Costs:** Controlling access and costs and usage was impossible

   *"I want my graduate students to use this, but I’m worried they’ll go beyond my budget"*

3. **Maintenance:** It was difficult to deploy and maintain

   *"How do I tune my cloud autoscaler?  Actually, what is a cloud auto-scaler?"*

4. **Regular Jobs:** It failed to address non-interactive use cases

   *"My notebook is great, but how do I run this job every day?"*

5. **Rigidity:** It assumed a uniform development environment

   *"I want to use the newest version of scikit-learn, but the Docker image has an old version"*

6. **Multi-cloud:** It didn’t work across regions or clouds

   *"How do I access my collaborator’s data in Europe?"*

   *"Does this work on Azure?"*

7. **Storage:** File formats were still wonky

   *"Zarr seems cool, but we’re still using NetCDF.*

   *Also, my data keeps updating, can Zarr expand like this?"*

8. **Scale:** Scale was still an issue

   *"This works great on 200 GiB, but when I move to the full dataset my workers start running out of memory"*

9. **Personnel:** It required people to keep it alive, and no one was paid to do so

There were incremental improvements in the components of the stack.  Dask-gateway replaced dask-kubernetes.  Zarr became more common.  Dask and Xarray both improved in scale.  There were also many extensions of it, with new libraries built on top of Xarray and a wonderful growth in community engagement.

However overall **this deployment architecture was a technological dead end** (at least in my opinion as original architect).  Personally I’m **proud that we were able to generate so much enthusiasm** (most of the credit here due to Ryan Abernathey, Rich Signell, and others who pushed the Pangeo stack within scientific circles) but mildly ashamed of the architecture itself.  It’s easy to build a cool demo with the Pangeo stack, but difficult to actually solve the computational and business needs of larger organizations.  **The Pangeo stack was fantastic demo-ware**.

## Present

Since 2018, there have been several re-imaginings of this stack.  There are full-platform options (everything included, but not particularly powerful) and some tool-specific options (innovative and powerful, but require assembly).  Let’s list a few in each category:

### Full Platform Options

- **2I2C** is a classic Kubernetes + JupyterHub architecture similar to what we built in 2018 (pure OSS), but sold with a service to set up and maintain it for organizations that don’t happen to keep a Kuberentes and cloud expert on staff.

- **Nebari** (née QHub) is a better architected execution of the same components, and with more components (workflow managers, editors, …)  Nebari is pure OSS and deployed using git-ops, but recognizing that people need help (OSS isn’t free to maintain) Nebari is often sold with services from Quansight who maintains it.

- **Saturn** took the same UX with Jupyter and Dask (and others tools), but dropped dask-gateway and JupyterHub, and instead added in a proper database-backed web application.  Saturn is a commercial SaaS product with one professionally managed central control plane that can be used anywhere.

### Innovative and Tool-Specific Options

- **Coiled (compute)** is what I and people around me built.

  Coiled focuses computation exclusively, while also including all of the user management and cost controls that were missing in Pangeo.  Coiled doesn’t serve Jupyter or store data.  Instead, it works with other tools users already have, running from anywhere people run Python (most notably, their existing laptop).

  I’ll claim (perhaps with hubris) that Coiled is among most high-end Python cloud compute platforms on the market today.  This product was built with creativity and soul, and delivers a developer experience that I’m proud of (and user praise seems to back this perspective).

- **Arraylake (storage)** is what Ryan Abernathey and Joe Hamman (the other two primary Pangeo architects) built at Earthmover.

  Arraylake is a data lake platform built around the Zarr data model which incorporates many database-style features, such as ACID transactions, data version control, fine-grained access controls, and a built-in data catalog.  A bit like Zarr \+ Git, or Delta Lake if you’re familiar with the dataframe storage space, Arraylake solves many of the data management challenges we experienced in the first iteration of Pangeo.

- **Other tooling** like workflow managers (Prefect, Dagster), code editors (VS Code), ML/AI tooling (PyTorch, LLMs) and more have come online.  The data infrastructure world today is a vibrant and mercurial environment.

### Status

Today I see a few things:

- **Coiled and Earthmover** deliver an innovative top-shelf experience to some geospatial users, but not many.  Those users tend to be early adopters and low-bureaucracy users like startups rather than older and larger organizations like NASA, weather agencies, and the energy majors.

- **Home Grown Pangeo 1.0 deployments** still get proposed within large agencies by IT groups who want to solve the data accessibility problem, but don’t land well on completion.

- **2I2C and Nabari deployments** are used in more on-prem-ish environments where SaaS isn’t welcome, but end up delivering mostly a JupyterHub+ experience.  While users report enjoying the cloud notebook capability, I haven’t seen an organization succeed with scalable/distributed computing with these platforms in practice.

- **Single large VMs** tend to be standard.  While simple, this often means that users don’t do full-dataset computations and, ironically, have crazy high cloud bills (single large VMs tend to be set up in a way that they stay on forever, which can be startlingly expensive).

### Community Developments

There has also been a lot of wonderful work in building community around Pangeo, with a thriving [discourse forum](https://discourse.pangeo.io/), numerous third-party packages like xbatcher, xradar, rechunker, etc.., educational groups like [Project Pythia](https://projectpythia.org/), and more.

While core technological innovation has struggled, there’s been a lot of innovation on the human side.

We’re at a strange place where we have a compelling POC (thanks Pangeo 1.0\!) that’s motivated a lot of people to act, but no great place for them to go just yet.  We also have an encouraging set of next-generation products (Coiled, Arraylake, Prefect, …) pointing the way to a bright future, but nothing that a mature organization can easily pull off the shelf. Procuring and integrating services from multiple different SaaS vendors comes with its own set of headaches.

## Future

So what should we do here?  What does the Pangeo 2.0 platform look like?  Ryan Abernathey and I were discussing this topic last week over drinks and started shooting lots of ideas at each other.

Is it just Coiled with notebooks and regular jobs?<br/>
Arraylake but with online update algorithms?<br/>
Does Saturn do everything people need?<br/>
Maybe it has to be on-prem like Nebari for government folks, but with a proper user database?  Can we get government on Cloud SaaS?<br/>
Maybe there are many different architectures for different kinds of applications and so organizations are fated to DIY?

I’ll give some of my opinionated constraints below.  I think that we got some things right with Coiled:

- [**Raw-cloud architecture**](https://docs.coiled.io/user_guide/why.html#how-raw-cloud-architecture) rather than Kubernetes
- [**Environment synchronization**](https://docs.coiled.io/user_guide/why.html#how-environment-synchronization) rather than Docker images
- [**Cost controls**](https://docs.coiled.io/user_guide/costs/index.html) **and [user management](https://docs.coiled.io/user_guide/users/index.html) in a database**, rather than JupyterHub/Kubernetes
- **Centrally managed SaaS product** with one set of operators, rather than several instances of the same stack
- **Trivial integrations** with other tools (our integration is just `import coiled` in a Python prompt)

But maybe we got some things wrong:

- **Notebooks:** while I still believe that notebooks and computation should be separable (it’s important to drive computations from things-other-than-notebooks) I now realize that single-node cloud notebooks are sometimes valuable, especially for organizations who want to deliver a more curated and homogenous experience to a population of non-power-users.  (I tend to overweight the experience of power-users)
- **Regular Batch Jobs:** while I still believe in integrating with best-in-class workflow orchestration products like Prefect/Dagster, some organizations want something trivial baked-in, particularly when migrating from an on-prem HPC-style environment
- **SaaS:** I’m actually still pretty convinced that this is the right way forward.  SaaS within government agencies has proven a major source of friction, but the development velocity is just so much faster.

Additionally, I’ll follow with some perhaps unpopular organizational perspectives:

- **Deployment Infrastructure should be SaaS rather tha OSS**
  - Faster iteration (we can release daily rather than monthly)
  - Better visibility (we can see every failure, often before users do)
  - Maintenance costs are a tiny fraction when shared among different user groups
    (we service hundreds of companies with a tiny cloud dev staff)
- **For-profit companies** move faster than the community
  - Most organizations mostly care about if it works, rather than who builds it

However, I still have lots of questions:

- **What key activities and pain points are people looking to solve today?**
  What features do you need?
  - Dask / Xarray features?
  - User / cost / administration features?
  - Notebooks in the cloud?
  - Better Scalability?
  - Batch jobs / workflow orchestration?
  - Databases and data catalogs?
- **How do geo-specific organizations buy software?**
  - Do you buy software or do you build everything yourself?
  - Do you deploy SaaS or do things have to be installed on-prem or in fully-isolated cloud VPCs?
  - Who makes these decisions?  What do they care about?
  - How do science users impact this decision-making process?

If you’ve made it to the end of this post then I could use your help answering these questions.  If you or someone you know works at an institution that buys this kind of software and are open to a 30 minute conversation, then I’d like to probe your brain with a few questions like these and gather your perspective.

Send me an e-mail at [pangeo-2.0-discovery@coiled.io](mailto:pangeo-2-discovery@coiled.io) and I’ll schedule a chat this week.
