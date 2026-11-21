# Normalized branch range attempt1272 — working checkpoint

Approved target: decide delta=0 versus delta>0 in review1270's exact
COVERED_TARGET, reusing source readiness1271. Main gap remains
L030-L032/C032a actual-Xi positivity. A decision would screen an
approximate common-profile bridge; it would not identify the source
metric or establish positivity.

The required discriminator is a uniform relative defect bound or a
compact complex sequence with unit two-component plus norm and
vanishing defect. Both sigma components must use the same input.
Inputs: C032e and L016,L018-L020. Preserve exact-stop1268/audit1270
and Green-source-stop1266. No numerical fitting or new literature is
needed for the already approved bounded attempt.

Initial reduction (to be written rigorously before any conclusion):
put h=f/Psi. Positivity and smoothness make this a bijection of
C_c^infinity(0,infinity), not a bounded isometry of an asserted source
space. In the auxiliary H=L2(0,infinity), define A h by the two
kernels (1+t)exp(sigma*t/8)Psi(t), and B h by the two kernels
((1-c)-(1+c)t)exp(sigma*t/8)Psi(t), t=s+u. The full-theta tail in
C032e (8) makes integral t times the squared absolute kernels finite;
the rectangular operators are Hilbert-Schmidt. The common compact
core is dense in H, permitting approximation in both output norms.
This supplies a possible valid domain/core reduction, but by itself
does not decide delta or pay Douglas's range-inclusion hypothesis.

Pending: verify all reduction bounds, retain complex cancellations,
and test whether the special kernels give the needed relative
comparison. Any unclosed range assertion must remain explicitly open.

Completed bounded attempt1272: the domain/core reduction and exact
Douglas applicability are written in canonical C032f. The pending
domain assertions above are now justified there. The attempt did not
decide the normalized threshold: neither actual adjoint-range
inclusion nor a separating range obstruction was obtained. The
pointwise shortcut fails at a positive kernel root; its precise scope
is saved in ATTEMPTS/2026-11-17-normalized-branch-pointwise-stop-1272.md.
No finite fit or numerical script was used. Outcome EXPLORATION,
classification REPRODUCTION; this is one mathematical attempt.

Retain the same approved target for one further bounded range test.
With the C032f operators, test whether A*(0,exp(-u)) belongs to
ran B*. This vector lies in Y. Nonmembership would decide delta=0
by C032f (5); a solution for this one vector would not establish
inclusion or a positive delta. No solution or nonmembership is
asserted now. Do not repeat the paid domain/core reduction or infer
coercivity from scalar kernel signs. If this test supplies no new
input, reassess the mechanism under the two-attempt rule. Source
metric, completed transport and all-degree actual-Xi positivity
remain separate; no central creative mechanism is justified by this
reduction alone.
