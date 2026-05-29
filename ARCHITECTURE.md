# Architecture — RoboPerceive (AMD Developer Hackathon: ACT II)

> Robot perception and vision-language-action (VLA) inference on **AMD Instinct MI300X** / ROCm 7.x. All compute runs on the **AMD AI Developer Cloud** — no local GPU required.

## High-level flow

```
  Camera frames + natural-language task goal
              │
              ▼
  ┌─────────────────────────────────────────┐
  │  Perception pipeline                    │
  │   ┌─────────────────────────────────┐   │
  │   │ Frame decode & preprocessing    │   │   CPU pre-processing
  │   └─────────────┬───────────────────┘   │
  │                 ▼                       │
  │   ┌─────────────────────────────────┐   │
  │   │ Vision encoder (ViT / CLIP)     │   │   MI300X · ROCm 7.x
  │   └─────────────┬───────────────────┘   │
  └─────────────────┼───────────────────────┘
                    │  visual tokens
                    ▼
  ┌─────────────────────────────────────────┐
  │  VLA policy model                       │
  │   ┌─────────────────────────────────┐   │
  │   │ Language-conditioned transformer │   │   MI300X · 192 GB VRAM
  │   │ (OpenVLA or fine-tuned LLaVA)   │   │   PyTorch on ROCm
  │   └─────────────┬───────────────────┘   │
  └─────────────────┼───────────────────────┘
                    │  action logits
                    ▼
  ┌─────────────────────────────────────────┐
  │  Action agent                           │
  │   ┌─────────────────────────────────┐   │   structured output
  │   │ Action parser + dispatcher      │   │   → robot command tokens
  │   └─────────────┬───────────────────┘   │
  └─────────────────┼───────────────────────┘
                    │
                    ▼
  ┌─────────────────────────────────────────┐
  │  Simulation / demo environment          │   PyBullet or MuJoCo
  │  (lightweight, for end-to-end demo)     │   hosted alongside inference
  └─────────────────────────────────────────┘
                    │
                    ▼
         Public demo URL + benchmark report
```

## Components

| Component | Role |
|---|---|
| **Frame decode & preprocessing** | Resize, normalize, and batch incoming camera frames on CPU before passing to GPU. |
| **Vision encoder** | ViT or CLIP backbone — encodes image observations into visual token embeddings on MI300X. |
| **VLA policy model** | Language-conditioned transformer (OpenVLA / fine-tuned LLaVA-style) maps visual tokens + task goal to action logits. Runs entirely on AMD MI300X via PyTorch/ROCm. |
| **Action agent** | Parses action logits into structured robot commands (move, grasp, navigate); dispatches to sim. |
| **Simulation environment** | PyBullet or MuJoCo sim for closed-loop evaluation; not GPU-bound — runs on the same cloud VM. |
| **Inference server** | FastAPI/uvicorn REST endpoint; accepts `{image_b64, goal}`, returns `{action}`. |
| **Benchmarking harness** | Measures throughput (steps/s) and latency (ms/step) for FP16 and INT8 on MI300X; results included in submission. |

## Compute

| Resource | Value |
|---|---|
| GPU | AMD Instinct MI300X |
| VRAM | 192 GB (unified HBM3) |
| Runtime | ROCm 7.x |
| Platform | AMD AI Developer Cloud |
| Framework | PyTorch (ROCm build) |

The MI300X's large unified memory pool allows the full vision backbone + language policy to run in a single forward pass without model parallelism, which simplifies the inference stack considerably.

## Notes

- All model weights are open-source (OpenVLA, LLaVA, or equivalent permissive-licensed checkpoints).
- The repo is MIT-licensed in compliance with lablab.ai submission rules.
- Benchmarking on MI300X (FP16 vs INT8 throughput) is explicitly encouraged by the challenge — results will be in the demo.
