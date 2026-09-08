"""peatland-rewetting-utac -- peatland rewetting: CO2 sink, methane rise,
and biodiversity honesty (Guenther 2020, Moorschutzstrategie DE 2022,
Kreyling 2021).

GenesisAeon Package 131. Own package, not a P100/P107 extension.
Deliberately NO UTAC/CREP/AFET bridge -- see DISCLAIMER.md.

The unverified ~20 t CO2e/ha/yr savings figure is intentionally omitted
as a usable constant; is_20_tonnes_per_hectare_figure_confirmed()
returns False as a negative check.
"""

from __future__ import annotations

from .constants import (
    BULK_DENSITY_CHANGE_PCT,
    DRAINED_PEAT_EMISSIONS_MT_CO2E_YR,
    DRAINED_TEMPERATE_CH4_KG_HA_YR,
    DRAINED_TEMPERATE_CO2_T_HA_YR,
    GUENTHER_2020_CITATION,
    GUENTHER_2020_CORE_MESSAGE_NOTE,
    GUENTHER_2024_AUTHOR_CORRECTION_CITATION,
    GUENTHER_CO2_ONLY_DIFFERENCE_NOTE,
    KREYLING_2021_CITATION,
    KREYLING_NO_CONVERGENCE_NOTE,
    MEAN_YEARS_AFTER_REWETTING,
    MOORSCHUTZSTRATEGIE_SCOPE_NOTE,
    NATIONALE_MOORSCHUTZSTRATEGIE_CITATION,
    ORGANIC_MATTER_CHANGE_PCT,
    OWN_PACKAGE_NOTE,
    PACKAGE_ID,
    PCT_REWETTED_OUTSIDE_NATURAL_BIODIV_RANGE,
    REWETTED_CH4_KG_HA_YR,
    REWETTED_CO2_T_HA_YR,
    SCOPE_NOTE,
    SHANNON_NEAR_NATURAL,
    SHANNON_NEAR_NATURAL_SE,
    SHANNON_REWETTED,
    SHANNON_REWETTED_SE,
    SHARE_OF_GERMAN_GHG_PCT,
    SITES_NEAR_NATURAL,
    SITES_REWETTED,
    TALL_HERB_COVER_INCREASE_PCT,
    TARGET_REDUCTION_MT_CO2E_YR_BY_2030,
    TWENTY_TONNES_EXCLUSION_NOTE,
    WATER_TABLE_NEAR_NATURAL_CM,
    WATER_TABLE_REWETTED_CM,
    YEARS_AFTER_REWETTING_SPAN_HIGH,
    YEARS_AFTER_REWETTING_SPAN_LOW,
)
from .honesty import (
    does_methane_increase_after_rewetting,
    does_methane_increase_negate_climate_benefit,
    does_rewetting_fully_restore_original_biodiversity,
    is_20_tonnes_per_hectare_figure_confirmed,
    is_rewetting_a_net_co2_sink,
)

__version__ = "1.0.0"

__all__ = [
    "BULK_DENSITY_CHANGE_PCT",
    "DRAINED_PEAT_EMISSIONS_MT_CO2E_YR",
    "DRAINED_TEMPERATE_CH4_KG_HA_YR",
    "DRAINED_TEMPERATE_CO2_T_HA_YR",
    "GUENTHER_2020_CITATION",
    "GUENTHER_2020_CORE_MESSAGE_NOTE",
    "GUENTHER_2024_AUTHOR_CORRECTION_CITATION",
    "GUENTHER_CO2_ONLY_DIFFERENCE_NOTE",
    "KREYLING_2021_CITATION",
    "KREYLING_NO_CONVERGENCE_NOTE",
    "MEAN_YEARS_AFTER_REWETTING",
    "MOORSCHUTZSTRATEGIE_SCOPE_NOTE",
    "NATIONALE_MOORSCHUTZSTRATEGIE_CITATION",
    "ORGANIC_MATTER_CHANGE_PCT",
    "OWN_PACKAGE_NOTE",
    "PACKAGE_ID",
    "PCT_REWETTED_OUTSIDE_NATURAL_BIODIV_RANGE",
    "REWETTED_CH4_KG_HA_YR",
    "REWETTED_CO2_T_HA_YR",
    "SCOPE_NOTE",
    "SHANNON_NEAR_NATURAL",
    "SHANNON_NEAR_NATURAL_SE",
    "SHANNON_REWETTED",
    "SHANNON_REWETTED_SE",
    "SHARE_OF_GERMAN_GHG_PCT",
    "SITES_NEAR_NATURAL",
    "SITES_REWETTED",
    "TALL_HERB_COVER_INCREASE_PCT",
    "TARGET_REDUCTION_MT_CO2E_YR_BY_2030",
    "TWENTY_TONNES_EXCLUSION_NOTE",
    "WATER_TABLE_NEAR_NATURAL_CM",
    "WATER_TABLE_REWETTED_CM",
    "YEARS_AFTER_REWETTING_SPAN_HIGH",
    "YEARS_AFTER_REWETTING_SPAN_LOW",
    "does_methane_increase_after_rewetting",
    "does_methane_increase_negate_climate_benefit",
    "does_rewetting_fully_restore_original_biodiversity",
    "is_20_tonnes_per_hectare_figure_confirmed",
    "is_rewetting_a_net_co2_sink",
    "__version__",
]
