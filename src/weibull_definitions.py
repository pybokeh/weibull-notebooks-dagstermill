from dagster import Definitions
from dagstermill import ConfigurableLocalOutputNotebookIOManager
from weibull_assets import weibull_jupyter_notebook


defs = Definitions(
	assets=[weibull_jupyter_notebook],
	resources={
        "output_notebook_io_manager": ConfigurableLocalOutputNotebookIOManager(),
    },
)
