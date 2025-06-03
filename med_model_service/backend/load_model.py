from .llava_med.model import get_model_components

tokenizer, model, image_processor, context_len = get_model_components()