from __future__ import annotations

from peatland_rewetting_utac import (
    BULK_DENSITY_CHANGE_PCT,
    DRAINED_PEAT_EMISSIONS_MT_CO2E_YR,
    DRAINED_TEMPERATE_CH4_KG_HA_YR,
    DRAINED_TEMPERATE_CO2_T_HA_YR,
    GUENTHER_2020_CITATION,
    GUENTHER_2024_AUTHOR_CORRECTION_CITATION,
    GUENTHER_CO2_ONLY_DIFFERENCE_NOTE,
    KREYLING_2021_CITATION,
    KREYLING_NO_CONVERGENCE_NOTE,
    MEAN_YEARS_AFTER_REWETTING,
    ORGANIC_MATTER_CHANGE_PCT,
    OWN_PACKAGE_NOTE,
    PACKAGE_ID,
    PCT_REWETTED_OUTSIDE_NATURAL_BIODIV_RANGE,
    REWETTED_CH4_KG_HA_YR,
    REWETTED_CO2_T_HA_YR,
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
    __version__,
    does_methane_increase_after_rewetting,
    does_methane_increase_negate_climate_benefit,
    does_rewetting_fully_restore_original_biodiversity,
    is_20_tonnes_per_hectare_figure_confirmed,
    is_rewetting_a_net_co2_sink,
)


def test_package_id_and_version() -> None:
    assert PACKAGE_ID == 131
    assert __version__ == "1.0.0"


def test_guenther_2020_fluxes() -> None:
    assert GUENTHER_2020_CITATION["doi"] == "10.1038/s41467-020-15499-z"
    assert DRAINED_TEMPERATE_CO2_T_HA_YR == 10.3
    assert DRAINED_TEMPERATE_CH4_KG_HA_YR == 7.9
    assert REWETTED_CO2_T_HA_YR == -0.4
    assert REWETTED_CH4_KG_HA_YR == 205.9
    assert REWETTED_CO2_T_HA_YR < 0
    assert REWETTED_CH4_KG_HA_YR > DRAINED_TEMPERATE_CH4_KG_HA_YR


def test_guenther_2024_author_correction() -> None:
    assert (
        GUENTHER_2024_AUTHOR_CORRECTION_CITATION["doi"]
        == "10.1038/s41467-024-47604-x"
    )
    note = GUENTHER_2024_AUTHOR_CORRECTION_CITATION["note"].lower()
    assert "14" in note and "28" in note
    assert "n2o" in note
    assert "correct" in note


def test_moorschutzstrategie_de() -> None:
    assert TARGET_REDUCTION_MT_CO2E_YR_BY_2030 == 5.0
    assert DRAINED_PEAT_EMISSIONS_MT_CO2E_YR == 53
    assert SHARE_OF_GERMAN_GHG_PCT == 7.5


def test_kreyling_2021_biodiversity() -> None:
    assert KREYLING_2021_CITATION["doi"] == "10.1038/s41467-021-25619-y"
    assert SITES_REWETTED == 320
    assert SITES_NEAR_NATURAL == 243
    assert MEAN_YEARS_AFTER_REWETTING == 9
    assert YEARS_AFTER_REWETTING_SPAN_LOW == 1
    assert YEARS_AFTER_REWETTING_SPAN_HIGH == 54
    assert SHANNON_REWETTED == 1.46
    assert SHANNON_REWETTED_SE == 0.04
    assert SHANNON_NEAR_NATURAL == 1.75
    assert SHANNON_NEAR_NATURAL_SE == 0.04
    assert SHANNON_REWETTED < SHANNON_NEAR_NATURAL
    assert PCT_REWETTED_OUTSIDE_NATURAL_BIODIV_RANGE == 63
    assert TALL_HERB_COVER_INCREASE_PCT == 66
    assert WATER_TABLE_REWETTED_CM == 5.0
    assert WATER_TABLE_NEAR_NATURAL_CM == -1.5
    assert ORGANIC_MATTER_CHANGE_PCT == -18
    assert BULK_DENSITY_CHANGE_PCT == 61
    assert "no convergence" in KREYLING_NO_CONVERGENCE_NOTE.lower()


def test_honesty_structural() -> None:
    assert is_rewetting_a_net_co2_sink() is True
    assert does_methane_increase_after_rewetting() is True
    assert does_methane_increase_negate_climate_benefit() is False
    assert does_rewetting_fully_restore_original_biodiversity() is False
    assert is_20_tonnes_per_hectare_figure_confirmed() is False


def test_twenty_tonnes_figure_excluded() -> None:
    assert "intentionally omitted" in TWENTY_TONNES_EXCLUSION_NOTE.lower()
    assert "20" in TWENTY_TONNES_EXCLUSION_NOTE
    # Must not appear as an encoded usable numeric savings constant.
    from peatland_rewetting_utac import constants as c

    names = [n for n in dir(c) if n.isupper()]
    assert "TWENTY_TONNES_EXCLUSION_NOTE" in names
    assert not any(
        n
        for n in names
        if ("20" in n or "TWENTY" in n)
        and n.endswith(("_T_HA_YR", "_CO2E_HA_YR", "_SAVINGS"))
    )
    # Guenther CO2-only difference note must warn against mixing.
    assert "10.7" in GUENTHER_CO2_ONLY_DIFFERENCE_NOTE
    assert "20" in GUENTHER_CO2_ONLY_DIFFERENCE_NOTE


def test_own_package_not_p100_p107_extension() -> None:
    assert "P100" in OWN_PACKAGE_NOTE
    assert "P107" in OWN_PACKAGE_NOTE
    assert "Own package" in OWN_PACKAGE_NOTE


def test_no_crep_afet_gamma_bridge_symbols() -> None:
    import peatland_rewetting_utac as m
    from pathlib import Path
    import re

    public = " ".join(n for n in dir(m) if not n.startswith("_")).upper()
    assert "CREP" not in public
    assert "AFET" not in public
    assert "GAMMA" not in public

    # Disclaimer may mention "no UTAC/CREP/AFET bridge"; strip that phrase,
    # then ensure no remaining bridge vocabulary / Gamma inventions.
    src = Path(m.__file__).resolve().parent
    blob = "\n".join(p.read_text(encoding="utf-8") for p in src.glob("*.py"))
    assert re.search(r"no\s+UTAC/CREP/AFET", blob, flags=re.IGNORECASE)
    cleaned = re.sub(
        r"no\s+UTAC/CREP/AFET(?:\s+bridge)?",
        "",
        blob,
        flags=re.IGNORECASE,
    ).upper()
    assert "CREP" not in cleaned
    assert "AFET" not in cleaned
    assert "GAMMA" not in cleaned
