# amd-act-ii — Workflow

AMD ACT II — GrootNet hackathon delivery (build Jul 6-11). 5 roles: Platform/Infra Eng (AMD cloud/MI300X/ROCm) -> ML/Agent Eng -> Integration Eng -> Demo/Pitch Owner -> Team Lead (Accountable, hi@forenly.ai). Each handoff notifies Discord #amd-act. Track by correlationId=amd-act-ii.

Conductor: `amd_act_ii_pipeline` (v1). Roles: Platform/Infra Eng -> ML/Agent Eng -> Integration Eng -> Demo/Pitch Owner -> Team Lead (Accountable). Notifies Discord #amd-act.

```mermaid
flowchart TD
  notify_setup["notify notify_setup"]
  prehack_setup_gate["HITL prehack_setup_gate"]
  notify_setup --> prehack_setup_gate
  setup_router{setup_router}
  prehack_setup_gate --> setup_router
  notify_build1["notify notify_build1"]
  setup_router --> notify_build1
  build_agent_core["build_agent_core"]
  notify_build1 --> build_agent_core
  agent_core_gate["HITL agent_core_gate"]
  build_agent_core --> agent_core_gate
  notify_build2["notify notify_build2"]
  agent_core_gate --> notify_build2
  build_sprint2["fork build_sprint2"]
  notify_build2 --> build_sprint2
  rocm_serving["rocm_serving"]
  build_sprint2 --> rocm_serving
  integration_mesh["integration_mesh"]
  build_sprint2 --> integration_mesh
  build_sprint2_join["join"]
  rocm_serving --> build_sprint2_join
  integration_mesh --> build_sprint2_join
  integration_gate["HITL integration_gate"]
  build_sprint2_join --> integration_gate
  notify_demo["notify notify_demo"]
  integration_gate --> notify_demo
  demo_prep["demo_prep"]
  notify_demo --> demo_prep
  final_gate["HITL final_gate"]
  demo_prep --> final_gate
  final_router{final_router}
  final_gate --> final_router
  submit["submit"]
  final_router --> submit
  notify_done["notify notify_done"]
  submit --> notify_done
```
