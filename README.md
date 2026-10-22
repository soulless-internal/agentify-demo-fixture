# Agentify synthetic release fixture

Preparation only; no hosted repository or product run exists yet.
All values are synthetic integer cents. No dependencies, accounts or deployment.
Run the release check: `python3 -m unittest -v`.
The seeded version intentionally fails exactly one of three tests.
The executing product agent should diagnose and repair the failure on a branch.
A successful merge must be followed by running this check on the merged revision.
That verifies code; it is not evidence of deployment to a service.
