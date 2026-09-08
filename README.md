# peatland-rewetting-utac

GenesisAeon Package 131 -- peatland rewetting: CO2 sink, methane rise,
and biodiversity honesty (Guenther 2020, Nationale Moorschutzstrategie
DE 2022, Kreyling 2021). **Deliberately has no UTAC/CREP/AFET bridge**
-- see [DISCLAIMER.md](DISCLAIMER.md).

Own package, **not** a P100/P107 extension (P100 is glacier-specific;
P107 has the wrong direction -- drained-peat emissions vs rewetting
sink).

For a plain-language German companion, see [WHITEPAPER.md](WHITEPAPER.md).

## What's real here

- **Guenther et al. (2020, *Nature Communications*)** -- DOI
  10.1038/s41467-020-15499-z: drained temperate **CO2 10.3 t/ha/yr**,
  **CH4 7.9 kg/ha/yr**; rewetted **CO2 -0.4 t/ha/yr (net sink)**,
  **CH4 205.9 kg/ha/yr**. Earlier rewetting is better; methane rise
  does not negate climate benefit if before 2050.
- **2024 Author Correction** -- DOI 10.1038/s41467-024-47604-x:
  N2O-to-CO2 factor bug (14 vs 28) fixed; **correction already applied**
  to cited numbers.
- **Nationale Moorschutzstrategie DE (2022-11-09, bmuv):** at least
  **5 Mt CO2e/yr** reduction by 2030; drained peat ~**53 Mt CO2e/yr**
  (~**7.5%** of German GHG).
- **Kreyling et al. (2021, *Nature Communications*)** -- DOI
  10.1038/s41467-021-25619-y: **320** vs **243** fen sites; Shannon
  **1.46+/-0.04** vs **1.75+/-0.04**; **63%** outside natural biodiv
  range; **no convergence over three decades**.

**Explicitly omitted:** unverified ~20 t CO2e/ha/yr savings figure
(`is_20_tonnes_per_hectare_figure_confirmed()` -> `False`).

## Quickstart

```bash
pip install peatland-rewetting-utac
```

```python
from peatland_rewetting_utac import (
    DRAINED_TEMPERATE_CO2_T_HA_YR,
    REWETTED_CO2_T_HA_YR,
    REWETTED_CH4_KG_HA_YR,
    is_rewetting_a_net_co2_sink,
    does_methane_increase_after_rewetting,
    does_methane_increase_negate_climate_benefit,
    does_rewetting_fully_restore_original_biodiversity,
    is_20_tonnes_per_hectare_figure_confirmed,
)

print(DRAINED_TEMPERATE_CO2_T_HA_YR)  # 10.3
print(REWETTED_CO2_T_HA_YR)  # -0.4
print(REWETTED_CH4_KG_HA_YR)  # 205.9
print(is_rewetting_a_net_co2_sink())  # True
print(does_methane_increase_after_rewetting())  # True
print(does_methane_increase_negate_climate_benefit())  # False
print(does_rewetting_fully_restore_original_biodiversity())  # False
print(is_20_tonnes_per_hectare_figure_confirmed())  # False
```

## Development

```bash
pip install -e ".[dev]"
ruff check src tests
mypy src
pytest
```

## Citation

See [CITATION.cff](CITATION.cff) and [.zenodo.json](.zenodo.json).
