# WP1 Method-Chain Evidence

For each method:

- suite preflight READY (5/5);
- Oracle VALID + verify_hash true;
- EvaluationBinding freeze/verify;
- actual `new-evaluator` PASS;
- replay true, provider_calls=0;
- report byte-identical.

Raw evidence: `evidence/results.json`, `evidence/run-*`, `evidence/ev-*`, `evidence/suite-*`.

All five pass the method chain; unified T1–T7 runner integration is not done.
