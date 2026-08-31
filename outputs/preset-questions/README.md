# Preset Question Outputs

The automated frozen-fixture suite writes its research runs here instead of mixing
them with arbitrary research runs in the parent `outputs/` directory.

Each question-specific directory contains its report, research log, trace, and nested
Evaluator-v1 results. Aggregate suite results and manifests are stored in
`evaluation-results/` when the batch runner is executed.
