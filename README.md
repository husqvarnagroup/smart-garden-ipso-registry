# Gardena IPSO Definitions

This repository contains LwM2M object definitions used with the GARDENA smart system.

The LwM2M object definitions consist of

* Objects defined in the [OMA LightweightM2M (LwM2M) Object and Resource Registry](https://technical.openmobilealliance.org/OMNA/LwM2M/LwM2MRegistry.html)
* Custom objects defined for the GARDENA smart system

> We currently disallow the modification of IPSO definition files in the `main` branch.

As almost every adjustment to an IPSO definition leads to at least a minor versioning
bump, we just forbid the modification of already released definitions.
This is quite strict. But it's simpler than checking for the versioning
rules for IPSO objects provided by the OMA.

## Rules

- Follow the rules specified by OMA: [LwM2M Core: Object Versioning](https://www.openmobilealliance.org/release/LightweightM2M/V1_2-20201110-A/HTML-Version/OMA-TS-LightweightM2M_Core-V1_2-20201110-A.html#7-2-0-72-Object-Versioning)
- Put all definition files into the `definitions` folder (no sub-folders)
- Don't delete old definitions (they could be in use at customers with old devices)
- Commit each version of a definition in a new file (and keep the old ones)
- Naming convention: `<optional-prefix><object-name>-<major-version>_<minor-version>.xml`
- Keep the [Confluence page](https://confluence-husqvarna.riada.se/display/SGS/Brave+New+World+IPSO+Registry)
up to date

## Where are the definitions used

These are the known parts of the GARDENA smart system that use the definitions.

### Firmware Update

The repository `sg-firmware-rollout` includes the IPSO definitions (this repo) as
a git submodule. The definitions are rolled out together with the firmware files to
ensure that the Gateway has always the newest definitions.

### Smart Garden Gateway

The most recent definitions are included in the Gateway image with a Yocto recipe.

### LwM2M Server

The latest definitions are packaged with the LwM2M server for easing development. It is
included as a submodule in the `sg-bnw-lwm2m-server` repository.

## References

- Confluence: [Brave New World IPSO Registry](https://confluence-husqvarna.riada.se/display/SGS/Brave+New+World+IPSO+Registry)
