def parse_storage_quota(quota_str):
    if not isinstance(quota_str, str) or not quota_str.strip():
        raise ValueError("Quota must be a non-empty string.")
    cleaned = quota_str.strip().upper()
    if len(cleaned) <= 2:
        raise ValueError("Invalid quota format.")
    val_str = cleaned[:-2]
    unit = cleaned[-2:]
    try:
        value = float(val_str)
    except ValueError:
        raise ValueError("Quota value must be numeric.")
    if value < 0:
        raise ValueError("Quota cannot be negative.")
    multipliers = {
        "MB": 0.001,
        "GB": 1.0,
        "TB": 1000.0
    }
    if unit not in multipliers:
        raise ValueError("Unsupported quota unit.")
    gb_total = value * multipliers[unit]
    return f"Quota: {gb_total:.2f} GB"
def compute_compression_ratio(size_metric_str):
    if not isinstance(size_metric_str, str) or not size_metric_str.strip():
        raise ValueError("Input must be a non-empty string.")
    parts = size_metric_str.split(':')
    if len(parts) != 2:
        raise ValueError("Input must contain raw:compressed values.")
    try:
        raw_bytes = float(parts[0])
        comp_bytes = float(parts[1])
    except ValueError:
        raise ValueError("Byte values must be numeric.")
    if raw_bytes < 0 or comp_bytes < 0:
        raise ValueError("Byte values cannot be negative.")
    if comp_bytes == 0:
        raise ValueError("Compressed bytes cannot be zero.")
    ratio = raw_bytes / comp_bytes
    return round(ratio, 2)
def lookup_bandwidth_tier_rate(tier_descriptor):
    if not isinstance(tier_descriptor, str) or not tier_descriptor.strip():
        raise ValueError("Tier descriptor must be a non-empty string.")
    prefix = tier_descriptor.strip().upper()[:3]
    tier_rates = {
        "HOT": 0.08,
        "COL": 0.05,
        "ARC": 0.02
    }
    if prefix not in tier_rates:
        raise ValueError("Unknown bandwidth tier.")
    return tier_rates[prefix]
def main():
    print("==== Running parse_storage_quota ====")
    q_input = input("Enter quota (e.g. 500MB, 10GB, 2TB): ")
    print(parse_storage_quota(q_input))
    print("\n==== Running compute_compression_ratio ====")
    c_input = input("Enter raw:compressed bytes (e.g. 1024:256): ")
    print("Compression Ratio:", compute_compression_ratio(c_input))
    print("\n==== Running lookup_bandwidth_tier_rate ====")
    t_input = input("Enter tier descriptor (e.g. HOT_TIER, COLD, ARCHIVE): ")
    print("Rate per GB: $", lookup_bandwidth_tier_rate(t_input))
if __name__ == "__main__":
    main()