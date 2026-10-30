
# GB200 NVL72 Cost Scenario Calculator
# All prices and throughput values below are
# ILLUSTRATIVE, not vendor quotes or benchmarks.

gpu_price_per_hour = 10.00
hours_per_month = 730
full_rack_gpus = 72

# Fictional throughput assumptions for modeling.
# These must eventually be replaced with measurements.
scenarios = {
    16: 1000,
    24: 1600,
    72: 4200
}

load_factor = 0.60

print("GB200 NVL72 - Hypothetical Cost Comparison")
print("NOT actual vendor pricing or benchmark data")
print("-" * 55)

for gpu_count, peak_tokens_sec in scenarios.items():
    allocated_hourly = gpu_count * gpu_price_per_hour
    full_rack_hourly = (
        full_rack_gpus * gpu_price_per_hour
    )

    delivered_tokens_hour = (
        peak_tokens_sec * load_factor * 3600
    )

    allocated_per_million = (
        allocated_hourly / delivered_tokens_hour
        * 1_000_000
    )

    rack_per_million = (
        full_rack_hourly / delivered_tokens_hour
        * 1_000_000
    )

    print(f"\nConfiguration: {gpu_count} GPUs")
    print(f"Allocated hourly cost: ${allocated_hourly:,.2f}")
    print(f"Allocated monthly cost: ${allocated_hourly * hours_per_month:,.2f}")
    print(f"Full-rack hourly cost: ${full_rack_hourly:,.2f}")
    print(f"Assumed output tokens/sec: {peak_tokens_sec}")
    print(f"Assumed load factor: {load_factor:.0%}")
    print(f"Allocated cost/1M tokens: ${allocated_per_million:.2f}")
    print(f"Full-rack cost/1M tokens: ${rack_per_million:.2f}")

print("\nIMPORTANT LIMITATIONS")
print("- No GB200 performance was measured.")
print("- GPU pricing is fictional.")
print("- Networking, cooling and operations excluded.")
print("- Input-token processing costs not modeled.")
print("- SLA compliance has not been validated.")
