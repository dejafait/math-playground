# C999r conditional cutoff audit608 — working record

Approved target: audit C999r(1)-(3), N>=512 and arbitrary complex inputs,
under its unchanged c_*, whole-core, analytic and arithmetic contracts.
Assessment606, approved separately in607, is reused without expansion.
Main gap: L030-L032/C032a actual-Xi positivity. A sound norm remainder
could pay the infinite complement of a later signed finite comparison;
no normalized finite margin or entry certificate is currently supplied.

Read C999r in full, C744v Sections3-4, C744z hypotheses/conclusion and
Sections1-3, and C999k Section1. Rechecked stops537/598/600/603: these
reject particular sufficient finite certificates or implementation
allowances, not the present exact compression. No cross-notebook input.

Initial audit notes, not yet a verdict:
- The C744v lower envelope implies h_n>=d_n for n>=512 by pi>3.
  The finite b bounds every remaining negative diagonal term.
- The restricted form must be used on V0; E need not map into Dom(A0).
  Check the spectral form identity and all domain hypotheses explicitly.
- The moment columns have signs (+,+) and (-,+); their independence
  separates parity even for complex coefficients. The retained sum is
  minus the omitted sum, so the low-mode correction is added.
- Check the two-sided E remainder and each nonnormal R product, including
  all retained crossing terms in (11), with no commuting projection.
- Audit the min branches, allowance lower bound and strict threshold(13).

Continuation test: uphold the complete conditional bound or record a
specific error and its effect; do not tune constants or infer signs.
Canonical audit evidence and its final verdict will be saved in C999r.

Completed608: C999r Section5 contains the full independent audit and
precise citations. All stated conditional bounds and threshold(13) are
upheld, including the ineffective allowance. The hypotheses, constants
and direct inputs are unchanged. No source computation or sign was
independently validated; this draft is only the preserved work record.
