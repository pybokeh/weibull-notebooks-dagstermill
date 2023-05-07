from dagstermill import define_dagstermill_asset
from dagster import file_relative_path


weibull_jupyter_notebook = define_dagstermill_asset(
    name="weibull_jupyter",
    notebook_path=file_relative_path(__file__, "notebooks/weibull_complete_failure_data.ipynb"),
    group_name="weibull",
)

