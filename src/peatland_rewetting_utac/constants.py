"""Verified constants for peatland rewetting: CO2 sink, methane rise, and biodiversity honesty.

GenesisAeon Package 131. Own package, not a P100/P107 extension (P100 is
glacier-specific; P107 encodes drained-peat *emissions* rather than the
rewetting *sink* direction). Pure-science, deliberately NO UTAC/CREP/AFET
bridge -- see DISCLAIMER.md.

Core-tier sources (exact figures from Paket-Prompts P131):
- Guenther et al. 2020, Nature Communications, DOI 10.1038/s41467-020-15499-z
  (2024 Author Correction DOI 10.1038/s41467-024-47604-x already applied)
- Nationale Moorschutzstrategie DE, adopted 2022-11-09 (bmuv)
- Kreyling et al. 2021, Nature Communications, DOI 10.1038/s41467-021-25619-y

The unverified ~20 t CO2e/ha/yr savings figure from secondary sources is
intentionally NOT encoded as a usable constant -- see
TWENTY_TONNES_EXCLUSION_NOTE and is_20_tonnes_per_hectare_figure_confirmed().
"""

from __future__ import annotations

PACKAGE_ID = 131

# =====================================================================
# Guenther, A., Barthelmes, A., Huth, V., Joosten, H., Jurasinski, G.,
# Koebsch, F., Couwenberg, J. (2020). "Prompt rewetting of drained
# peatlands reduces climate warming despite methane emissions."
# Nature Communications, 11, 1644. DOI: 10.1038/s41467-020-15499-z
#
# 2024 Author Correction DOI 10.1038/s41467-024-47604-x fixed an N2O->CO2
# molar conversion-factor bug (14 vs 28) in supplementary software.
# Cited numbers below already reflect the corrected record.
# =====================================================================

GUENTHER_2020_CITATION = {
    "authors": (
        "Guenther, A., Barthelmes, A., Huth, V., Joosten, H., "
        "Jurasinski, G., Koebsch, F., Couwenberg, J."
    ),
    "year": 2020,
    "title": (
        "Prompt rewetting of drained peatlands reduces climate warming "
        "despite methane emissions"
    ),
    "journal": "Nature Communications",
    "volume": 11,
    "article_id": "1644",
    "doi": "10.1038/s41467-020-15499-z",
}

GUENTHER_2024_AUTHOR_CORRECTION_CITATION = {
    "authors": (
        "Guenther, A., Barthelmes, A., Huth, V., Joosten, H., "
        "Jurasinski, G., Koebsch, F., Couwenberg, J."
    ),
    "year": 2024,
    "title": (
        "Author Correction: Prompt rewetting of drained peatlands "
        "reduces climate warming despite methane emissions"
    ),
    "journal": "Nature Communications",
    "doi": "10.1038/s41467-024-47604-x",
    "note": (
        "Code error in supplementary software (p.5, lines 163-165) used "
        "the wrong molar N2O-to-CO2-equivalent conversion factor (14 "
        "instead of 28) in the radiative-forcing calculation. Corrected; "
        "cited Guenther 2020 numbers in this package already incorporate "
        "the correction."
    ),
}

# Temperate drained peatland fluxes (Guenther et al. 2020).
DRAINED_TEMPERATE_CO2_T_HA_YR = 10.3
DRAINED_TEMPERATE_CH4_KG_HA_YR = 7.9

# Rewetted peatland fluxes (Guenther et al. 2020).
REWETTED_CO2_T_HA_YR = -0.4  # net CO2 sink
REWETTED_CH4_KG_HA_YR = 205.9

GUENTHER_2020_CORE_MESSAGE_NOTE = (
    "Guenther et al. (2020) qualitative / time-critical core message: the "
    "earlier drained peatlands are rewetted, the better. The methane "
    "increase does not negate the climate benefit IF rewetting happens "
    "before 2050. This is not encoded as a single net-benefit constant."
)

# Guenther's own CO2-only difference (10.3 -> -0.4) is ~10.7 t CO2/ha/yr.
# Do NOT confuse or merge this with the unverified ~20 t CO2e/ha/yr figure.
GUENTHER_CO2_ONLY_DIFFERENCE_NOTE = (
    "Guenther 2020 own CO2 difference (drained 10.3 -> rewetted -0.4 "
    "t/ha/yr, i.e. about 10.7 t CO2/ha/yr) is a real but narrower "
    "(CO2-only, not Germany-specific) quantity. Do not confuse or mix "
    "it with the unverified secondary-source '~20 t CO2e/ha/yr' savings "
    "figure (see TWENTY_TONNES_EXCLUSION_NOTE)."
)

# =====================================================================
# Nationale Moorschutzstrategie (Deutschland), adopted 2022-11-09.
# Confirmed from bmuv.de / BMU pages.
# =====================================================================

NATIONALE_MOORSCHUTZSTRATEGIE_CITATION = {
    "title": "Nationale Moorschutzstrategie",
    "jurisdiction": "Germany",
    "adopted": "2022-11-09",
    "source": "bmuv.de",
}

TARGET_REDUCTION_MT_CO2E_YR_BY_2030 = 5.0  # at least
DRAINED_PEAT_EMISSIONS_MT_CO2E_YR = 53  # approx. current
SHARE_OF_GERMAN_GHG_PCT = 7.5  # approx. share of German GHG emissions

MOORSCHUTZSTRATEGIE_SCOPE_NOTE = (
    "Nationale Moorschutzstrategie DE (adopted 2022-11-09): target of "
    "at least 5 Mt CO2e/yr reduction by 2030; drained peat soils cause "
    "approx. 53 Mt CO2e/yr (~7.5% of German GHG emissions). Figures are "
    "policy / inventory order-of-magnitude as stated by bmuv."
)

# =====================================================================
# Kreyling, J. et al. (2021). "Rewetting does not return drained fen
# peatlands to their old selves." Nature Communications, 12, 5693.
# DOI: 10.1038/s41467-021-25619-y (PMC8492760).
# =====================================================================

KREYLING_2021_CITATION = {
    "authors": "Kreyling, J. et al.",
    "year": 2021,
    "title": "Rewetting does not return drained fen peatlands to their old selves",
    "journal": "Nature Communications",
    "volume": 12,
    "article_id": "5693",
    "doi": "10.1038/s41467-021-25619-y",
    "pmc": "PMC8492760",
}

SITES_REWETTED = 320
SITES_NEAR_NATURAL = 243
MEAN_YEARS_AFTER_REWETTING = 9  # span 1-54 years
YEARS_AFTER_REWETTING_SPAN_LOW = 1
YEARS_AFTER_REWETTING_SPAN_HIGH = 54

SHANNON_REWETTED = 1.46
SHANNON_REWETTED_SE = 0.04
SHANNON_NEAR_NATURAL = 1.75
SHANNON_NEAR_NATURAL_SE = 0.04

PCT_REWETTED_OUTSIDE_NATURAL_BIODIV_RANGE = 63
TALL_HERB_COVER_INCREASE_PCT = 66

WATER_TABLE_REWETTED_CM = 5.0  # +5.0 cm
WATER_TABLE_NEAR_NATURAL_CM = -1.5

ORGANIC_MATTER_CHANGE_PCT = -18
BULK_DENSITY_CHANGE_PCT = 61

KREYLING_NO_CONVERGENCE_NOTE = (
    "Kreyling et al. (2021): no convergence tendency toward near-natural "
    "biodiversity over three decades. Rewetting brings CO2 benefits but "
    "does NOT fully restore original ecological conditions, even after "
    "decades. This is the central biodiversity honesty finding."
)

# =====================================================================
# Explicit exclusion: unverified ~20 t CO2e/ha/yr savings figure
# =====================================================================

TWENTY_TONNES_EXCLUSION_NOTE = (
    "The often-cited '~20 t CO2e/ha/yr savings through rewetting' from "
    "secondary sources is intentionally omitted: its origin could not be "
    "found in the Moorschutzstrategie PDF nor on bmuv.de. Do not encode "
    "it as a usable constant. Do not confuse it with Guenther 2020's "
    "own CO2-only difference (~10.7 t CO2/ha/yr)."
)

OWN_PACKAGE_NOTE = (
    "Own package (P131), not a P100/P107 extension. P100 is glacier-"
    "specific; P107 has the wrong direction (drained-peat emissions "
    "rather than rewetting sink). Cross-reference siblings in docs only."
)

SCOPE_NOTE = (
    "Pure-science peatland rewetting package: Guenther 2020 fluxes "
    "(temperate), Nationale Moorschutzstrategie DE 2022 targets/"
    "inventory, Kreyling 2021 fen biodiversity. No UTAC/CREP/AFET "
    "bridge. No invented numbers. No unverified 20 t/ha/yr constant."
)
