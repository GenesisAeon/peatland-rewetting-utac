# DISCLAIMER - Real Science, Rewetting Sink + Biodiversity Honesty, No Bridge

> **Why no UTAC/CREP/AFET bridge:** not only because the cited literature
> already provides the necessary quantitative structure -- a deliberate
> choice. This project's highly speculative AFET/UTAC experiments must
> never stand in the way of climate/ecology topics being accessible and
> usable to people who don't work inside that construct and aren't
> looking for renormalization groups. Real, checkable science, without
> the burden of an unproven framework. See `PACKAGE_REGISTRY.md`'s
> "Why no UTAC/CREP/AFET bridge in the climate/ecology series" (2026-08-31)
> in the GenesisAeon workspace root for the full canonical note.

**Status: Real, independently documented peatland-rewetting science
(CO2 sink, methane rise, German Moorschutz strategy, fen biodiversity
honesty). NO UTAC/CREP/AFET bridge.**

## Where this package came from

Built from `Apps/Paket-Prompts_P130-P132.md` section **P131 only**
(2026-09-08), twin structure matching `ocean-acidification-utac` /
`permafrost-utac` and sibling `river-gauge-shipping-utac` (P130)
(constants, honesty `is_*`/`does_*`, hatchling, DISCLAIMER,
CITATION.cff, README). **Own package**, not a P100/P107 extension
(P100 is glacier-specific; P107 encodes drained-peat *emissions*
rather than the rewetting *sink* direction).

## What this is

Core-tier constants encoded exactly from the P131 prompt:

- **Guenther, A. et al. (2020)**, *Nature Communications* 11, 1644,
  DOI: 10.1038/s41467-020-15499-z
  - temperate drained peat: **CO2 = 10.3 t/ha/yr**, **CH4 = 7.9 kg/ha/yr**
  - rewetted peat: **CO2 = -0.4 t/ha/yr (net sink)**, **CH4 = 205.9 kg/ha/yr**
  - core message is qualitative / time-critical: earlier rewetting is
    better; methane rise does **not** negate the climate benefit if
    rewetting happens **before 2050** -- not encoded as a single
    net-benefit number
- **2024 Author Correction**, DOI: **10.1038/s41467-024-47604-x** --
  real and confirmed: a code error in the supplementary software
  (p.5, lines 163-165) used the wrong molar N2O-to-CO2-equivalent
  conversion factor (**14 instead of 28**) in the radiative-forcing
  calculation. **This correction exists and is already incorporated
  into the Guenther numbers cited in this package.**
- **Nationale Moorschutzstrategie (Germany), adopted 2022-11-09**
  (bmuv): target of **at least 5 Mt CO2e/yr** reduction by 2030;
  drained peat soils cause **approx. 53 Mt CO2e/yr** (~**7.5%** of
  German GHG emissions).
- **Kreyling, J. et al. (2021)**, *Nature Communications* 12, 5693,
  DOI: 10.1038/s41467-021-25619-y -- **320** rewetted vs **243**
  near-natural fen sites, temperate Europe, mean **9 years** after
  rewetting (span 1-54); Shannon **1.46+/-0.04** vs **1.75+/-0.04**;
  **63%** of rewetted sites outside natural biodiversity range; tall
  herb cover **+66%**; water table **+5.0 cm** vs **-1.5 cm**; organic
  matter **-18%**; bulk density **+61%**; **no convergence over three
  decades**.

## Honesty checks (structural)

- `is_rewetting_a_net_co2_sink()` -> `True`
- `does_methane_increase_after_rewetting()` -> `True`
- `does_methane_increase_negate_climate_benefit()` -> `False`
  (if rewetting before 2050, per Guenther 2020)
- `does_rewetting_fully_restore_original_biodiversity()` -> `False`
- `is_20_tonnes_per_hectare_figure_confirmed()` -> `False`
  (negative check so the unverified figure is not later encoded)

## What this is NOT

- **Does not encode the unverified ~20 t CO2e/ha/yr savings figure**
  from secondary sources. Origin not found in the Moorschutzstrategie
  PDF or on bmuv.de -- omitted deliberately. Do not confuse it with
  Guenther 2020's own CO2-only difference (~10.7 t CO2/ha/yr from
  10.3 -> -0.4).
- **Not a claim that rewetting fully restores original biodiversity.**
  Kreyling 2021 is the honesty finding: CO2 benefits without full
  ecological restoration, even after decades.
- **Not a P100/P107 extension.** Own package (P131).
- **No UTAC/CREP/AFET bridge. No invented DOIs, Gamma, or numbers.**

## References

- Guenther, A., Barthelmes, A., Huth, V., Joosten, H., Jurasinski, G.,
  Koebsch, F., Couwenberg, J. (2020). "Prompt rewetting of drained
  peatlands reduces climate warming despite methane emissions."
  *Nature Communications*, 11, 1644. DOI: 10.1038/s41467-020-15499-z.
- Guenther, A. et al. (2024). Author Correction. *Nature
  Communications*. DOI: 10.1038/s41467-024-47604-x (N2O-to-CO2 factor
  14 vs 28 bug fixed; correction already applied to cited numbers).
- Nationale Moorschutzstrategie (Deutschland), adopted 2022-11-09
  (bmuv.de).
- Kreyling, J. et al. (2021). "Rewetting does not return drained fen
  peatlands to their old selves." *Nature Communications*, 12, 5693.
  DOI: 10.1038/s41467-021-25619-y.
