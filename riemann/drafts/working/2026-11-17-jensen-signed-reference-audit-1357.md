# Signed-reference audit1357 — completed

Gate: unchanged assessment1355, SPECIALIZE/REPRODUCTION. The exact target
is C019f's uniform limit, signed normalization, finite tails and full rational
sign certificate on [1,4]. Main gap: L030–L032/C032a all-degree actual-Xi
positivity. A retained limit can support later local root transfer; actual
root uniqueness/simplicity, effective onset and global closure are separate.

Reviewed the supplied overview/DAG, C019f and its complete script, C019c,
relevant C019e passages, parent coverage1354 and stops1345/1355. Preserve all
prior work. Initial notebook git status was oversized; subsequent inspection
is confined to affected paths. No sibling notebooks or runtime state read.

The audit is complete. Full reasoning and the retained qualifications are
canonical in C019f's critical-audit1357 passage. The independent checker
scripts/jensen-edge/audit_signed_reference_1357.py verifies all 606 saved
terms using closed-form coefficients, the full rational constant and tail
calculations, and 1304 assertions. Its complete certificate is
scripts/jensen-edge/signed-reference-audit-1357.json. The source replay in
scripts/jensen-edge/replay-1357/signed-reference-1355.json is byte-identical.
No failed mathematical inequality or enclosure was found. Same-sign
endpoints remain an obstruction to the original opposition target, not a
new obstruction discovered by this audit.

One replay wrapper initially set __file__ to a relative path, so the
original script's final display-only relative_to(Path.cwd()) raised a
ValueError after writing the certificate. Repeating with an absolute
__file__ completed the assertions and byte comparison. The original
script and certificate were never changed. An initial draft patch had a
misspelled absolute path and was rejected; the corrected relative-path
patch created this notebook-local file. No outside file was written.

This is RESEARCH/REPRODUCTION and a local ADVANCE in validation of the
existing input, not a stronger theorem or a discovery beyond the checked
sources. Actual-polynomial identification/transfer is separately nominated
with REVIEW_REQUIRED; no new mathematics is performed on that target.
