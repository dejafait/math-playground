# 2026-10-14 — Thirteen-adic reduction-order shortcut fails

RESEARCH / NEGATIVE / REPRODUCTION. Under the approved SPECIALIZE
assessment, [L068](../lemmas/L068-thirteen-reduction-order.md) computes
#E1(F13)=10 and #E1(F_(13^12))=23,298,078,211,200, divisible by thirteen.
The complete 169-pair enumeration and independent integer matrix
check are saved in `scripts/thirteen-reduction-order/order-certificate.json`;
all ten consistency checks pass. This is a local specialization of
Milne's known theorem, not progress beyond the checked source theory.

Bruin Lemma 4.2's prime-to-thirteen reduction-order premise fails.
Park only that sufficient index shortcut at thirteen; no actual
subgroup-index divisibility, rank, branch exclusion or global power
lifting follows. L067 and the separate ATTEMPTS/029–030 stops remain
unchanged. A separate critical audit of L068 is the next target,
with REVIEW_REQUIRED coverage. No complete candidate exists.
