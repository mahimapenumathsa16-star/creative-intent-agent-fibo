import torch
from diffusers import StableDiffusionPipeline
from PIL import Image
import json
from datetime import datetime

# ---- LOAD FIBO MODEL ----
model_id = "briaai/BRIA-2.3"

pipe = StableDiffusionPipeline.from_pretrained(
    model_id,
    torch_dtype=torch.float32
)

pipe = pipe.to("cpu")

# ---- LOAD GENERATED JSON ----
with open("final_fibo_config.json", "r") as f:
    config = json.load(f)

# ---- TRANSLATE JSON TO LIGHT PROMPT ----
prompt = (
    "Premium skincare product photography, "
    "soft natural lighting, warm neutral tones, "
    "intimate and calm mood, professional studio quality"
)

# ---- GENERATE IMAGE ----
image = pipe(
    prompt=prompt,
    num_inference_steps=30
).images[0]

# ---- SAVE OUTPUT ----
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"fibo_image_{timestamp}.png"
image.save(filename)

print(f"✅ FIBO IMAGE GENERATED: {filename}")
