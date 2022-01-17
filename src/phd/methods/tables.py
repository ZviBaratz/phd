from pathlib import Path

import pandas as pd
from pandas.io.formats.style import Styler
from phd.utils.book import get_chapters_root
from phd.utils.tables import style_df

CHAPTERS: Path = get_chapters_root()
MPRAGE_COUNT_CSV: Path = CHAPTERS / "methods/assets/mprage_protocol_counts.csv"
CAPTION: str = "MPRAGE counts aggregated by acquisition parameters."


def read_mprage_counts(csv_path: Path = MPRAGE_COUNT_CSV) -> pd.DataFrame:
    return pd.read_csv(csv_path)


def display_mprage_counts(
    csv_path: Path = MPRAGE_COUNT_CSV, hide_index: bool = True
) -> Styler:
    df = read_mprage_counts(csv_path)
    total_count = df["Count"].sum()
    return (
        style_df(
            df,
            hide_index=hide_index,
            number_format="{:.4g}",
            number_format_subset=list(df.columns)[:-1],
        )
        .bar(subset="Count", vmin=0, vmax=total_count)
        .set_caption(CAPTION)
        .background_gradient(
            subset=[
                name
                for name in df.columns
                if name not in ["Count", "Spatial Resolution (mm)"]
            ]
        )
    )
