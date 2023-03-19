import evaluate
from evaluate.utils import launch_gradio_widget


module = evaluate.load("Viona/fuzzy_reordering")
launch_gradio_widget(module)