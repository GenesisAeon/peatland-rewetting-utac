"""Structural honesty checks for peatland-rewetting-utac (P131).

These functions encode documented scientific findings and epistemic
limits -- not derived model outputs. Always return the fixed booleans
below.
"""

from __future__ import annotations

from .constants import (
    DRAINED_TEMPERATE_CH4_KG_HA_YR,
    MEAN_YEARS_AFTER_REWETTING,
    PCT_REWETTED_OUTSIDE_NATURAL_BIODIV_RANGE,
    REWETTED_CH4_KG_HA_YR,
    REWETTED_CO2_T_HA_YR,
    TWENTY_TONNES_EXCLUSION_NOTE,
)


def is_rewetting_a_net_co2_sink() -> bool:
    """Whether rewetted temperate peatland is a net CO2 sink.

    Guenther et al. (2020): REWETTED_CO2_T_HA_YR = -0.4 t/ha/yr.
    Always True.
    """
    assert REWETTED_CO2_T_HA_YR < 0
    return True


def does_methane_increase_after_rewetting() -> bool:
    """Whether CH4 emissions rise after rewetting.

    Guenther et al. (2020): drained 7.9 -> rewetted 205.9 kg CH4/ha/yr.
    Always True.
    """
    assert REWETTED_CH4_KG_HA_YR > DRAINED_TEMPERATE_CH4_KG_HA_YR
    return True


def does_methane_increase_negate_climate_benefit() -> bool:
    """Whether the methane increase cancels the climate benefit.

    Guenther et al. (2020): methane rise does NOT negate the climate
    benefit if rewetting happens before 2050. Always False under that
    documented condition.
    """
    return False


def does_rewetting_fully_restore_original_biodiversity() -> bool:
    """Whether rewetting fully restores original / near-natural
    biodiversity.

    Kreyling et al. (2021): 63% of rewetted sites lie outside the
    natural biodiversity range; no convergence over three decades
    (mean ~9 years after rewetting in the study sample). Always False.
    """
    _ = (PCT_REWETTED_OUTSIDE_NATURAL_BIODIV_RANGE, MEAN_YEARS_AFTER_REWETTING)
    return False


def is_20_tonnes_per_hectare_figure_confirmed() -> bool:
    """Whether the secondary-source '~20 t CO2e/ha/yr savings' figure
    is confirmed.

    Origin not found in Moorschutzstrategie PDF or on bmuv.de.
    Intentionally encoded as a negative check so the unverified figure
    is not later introduced as a constant. Always False.
    """
    _ = TWENTY_TONNES_EXCLUSION_NOTE
    return False
