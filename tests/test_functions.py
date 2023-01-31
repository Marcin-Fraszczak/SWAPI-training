# from pages.functions import CATEGORIES, used_cols, handler, get_data
# import pandas as pd
#
#
# def test_handler_returns_dict_with_data():
#     for i in range(1, 7):
#         data = handler(CATEGORIES.get(i))
#         assert type(data) == dict
#         for key in ["count", "previous", "next", "results"]:
#             assert key in data.keys()
#         assert data["count"] > 0
#         assert len(data["results"]) > 0
#
#
# def test_get_data_returns_dataframe():
#     for i in range(1, 7):
#         df = get_data(i)
#         cols = list(df.columns)
#         assert isinstance(df, pd.DataFrame)
#         for col in used_cols.get(i):
#             assert col in cols
#         assert len(df) > 0
#
