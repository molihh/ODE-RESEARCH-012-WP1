# Code and Contract

Implementation: `src/wp1_methods/`
- `specs.py`: five method descriptors + asset-type selector + exclusion reason.
- `builder.py`: deterministic Oracle claims + evidence; API ID separate from Asset ID.
- Uses WP2 `OracleEnvelope` and WP2 runtime `freeze_binding`/`replay`; no second factory.
- Does not modify WP4 public contracts, Oracle, Grader, or historical runs.
