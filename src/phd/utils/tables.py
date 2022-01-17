from typing import Dict, List, Tuple

import pandas as pd
from pandas.io.formats.style import Styler

GENERAL_PROPS = [
    (
        "font-family",
        '"Times New Roman", Georgia, serif',
    )
]
GENERAL_STYLE = {
    "selector": "",
    "props": GENERAL_PROPS,
}
HEADER_PROPS = [
    ("font-size", "1em"),
    ("border", "1px solid grey"),
    ("text-align", "center"),
]
HEADER_STYLE = {
    "selector": "th",
    "props": HEADER_PROPS,
}
CELL_PROPS = [
    ("font-size", "1em"),
    ("border", "1px solid grey"),
    ("padding", "2px"),
]
CELL_STYLE = {
    "selector": "td",
    "props": CELL_PROPS,
}
TABLE_STYLES = [
    GENERAL_STYLE,
    HEADER_STYLE,
    CELL_STYLE,
]
TABLE_PROPERIES = {
    "font-size": "1em",
    "text-align": "center",
}


def style_df(
    df: pd.DataFrame,
    styles: List[Dict[str, Tuple[str, str]]] = None,
    properties: Dict[str, str] = None,
    hide_index: bool = False,
    number_format: str = None,
    number_format_subset: List[str] = None,
) -> Styler:
    styles = styles or TABLE_STYLES
    properties = properties or TABLE_PROPERIES
    styled = df.style.set_table_styles(styles).set_properties(**properties)
    if number_format is not None:
        styled = styled.format(number_format, subset=number_format_subset)
    if hide_index:
        return styled.hide_index()
    return styled
