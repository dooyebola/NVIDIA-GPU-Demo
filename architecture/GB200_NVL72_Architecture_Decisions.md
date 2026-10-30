## Architecture Decision 002 — AI Workload Requirements

**Status:** Proposed — Not Yet Validated

### Business Objective

Design a conceptual enterprise AI inference platform
capable of serving large language models to multiple
customers while supporting performance, reliability,
and future infrastructure expansion.

### Proposed Workload

- Workload Type: Enterprise AI inference
- AI Model Class: 405B parameters
- Model Precision: BF16
- Maximum Context Length: 32,000 tokens
- Target Concurrent Active Requests: 100
- Availability Objective: 99.9%
- p95 Time to First Token: 5 seconds or less

### Proposed Infrastructure

- NVIDIA GB200 NVL72
- 72 NVIDIA Blackwell GPUs
- 36 NVIDIA Grace CPUs
- 18 Compute Trays
- 9 NVLink Switch Trays

### Proposed Software

- vLLM for AI model serving
- Kubernetes for workload orchestration
- NVIDIA GPU Operator for GPU integration

### Preliminary Memory Sizing

Model parameters: 405 billion
Precision: BF16 (2 bytes per parameter)

Estimated model weight memory:

405,000,000,000 x 2 = 810,000,000,000 bytes

Approximately 810 GB of model weights.

This does not include:
- KV cache
- Runtime overhead
- Temporary allocations
- Model replicas
- Other serving requirements

### Architecture Considerations

1. Estimate total GPU memory requirements.
2. Determine model parallelism strategy.
3. Evaluate concurrent request capacity.
4. Define latency and throughput objectives.
5. Plan networking and storage requirements.
6. Design monitoring and alerting.
7. Evaluate high availability and recovery.
8. Compare NVL72 against smaller alternatives.

### Validation Status

This architecture is a conceptual engineering study.

GPU sizing, concurrency, latency, availability,
and hardware selection require further analysis.

No physical GB200 NVL72 deployment has occurred.

## Architecture Decision 003 — GPU Capacity Sizing

**Status:** Preliminary Analysis

### Model Weight Memory

Model parameters: 405 billion
Precision: BF16
Bytes per parameter: 2

Estimated weights:
405,000,000,000 * 2 = 810 GB

### Additional Memory Requirements

- KV cache for active requests
- Model execution overhead
- Temporary GPU allocations
- Memory for concurrent inference
- Model replicas and redundancy

### Outstanding Calculations

1. Determine the model's KV-cache architecture.
2. Estimate average and maximum active tokens.
3. Calculate KV-cache memory requirements.
4. Estimate runtime memory overhead.
5. Calculate minimum GPU count for model weights.
6. Evaluate GPU parallelism configurations.
7. Compare smaller GPU cluster options.
8. Validate throughput and latency targets.

### Design Limitation

The current workload requirements are hypothetical.
No physical GB200 NVL72 system has been tested.

The full 72-GPU rack has not yet been
justified by capacity or performance analysis.