# Finite signed smoothed laws — working checkpoint1300

17 November 2026. One mathematical attempt under the pre-existing
EXPLORE assessment1298/review1299; no new source assessment is being
approved here. Main gap: actual-Xi all-degree Q positivity in
L030-L032/C032a. The bounded target is the exact finite signed-law
exponential-moment question in that assessment, including cancellation
of the leading cusp. C032j supplies the individual laws, not a theorem
about their signed sum. Stop1297 remains scoped to its old surrogate.

Interim derivation, still being checked: write p=p_sigma and, for
complex w, try

    R(w)=integral_0^infinity [p(x)-p(iw)]/(x^2+w^2) dx,
    O(w)=2*pi*integral_0^w p(it) dt,
    E(w)=4*integral_0^w t R(t) dt.

Because p is even entire, its divided difference removes the apparent
denominator zeros. Its logarithmic real-axis growth appears to give
locally uniform domination at infinity. Thus R should be entire even,
E entire even, O entire odd, and b(w)=E(w)+O(w) should continue
B_sigma(w^2) from Re(w)>0. This must be justified in full, including
w=0 and x=0, before becoming a canonical statement.

If valid, a finite combination has a transform analytic at s=0 only
if sum_j a_j exp(-E_j(w))*sinh(O_j(w)) vanishes identically. This is an
all-order condition, not merely sum_j a_j p_sigma_j(0)=0. Conditional
on nonnegativity, evenness of the entire lifted transform may also
force every positive exponential moment, by moment positivity and
the entire Taylor series. No linear independence, impossible-mixture
result, positive example or actual-Xi transfer has been established.

Source use: C032j; Sra2611.00345v1 Lemma A.4 and the Stieltjes formula
in the proof of Proposition A.8 (printed pp.13,17), whose exact
hypotheses and proof cases were retrieved. No divergent moments are
subtracted. No mathematical script or numerical evidence is needed.

Continuation test: rigorously establish the complete analytic
condition and see whether it settles cancellation. If independence
remains unpaid, retain that precise residual rather than claiming a
stop for the finite signed mechanism. A theorem about sums of
zero-free entire functions is a possible later source lead, not an
import or an approved continuation in this checkpoint.

Completed1300: the integral domination, entire lift, moment equivalence,
and distinct-width separation are now proved in canonical C032k.
The earlier tentative wording above is retained as the interruption
checkpoint, not the final statement. Pairwise nonproportionality is
proved, but finite linear independence is not inferred. No positive
example or exclusion of all mixtures is claimed. The sole next action
is recorded in PROGRESS.md and its REVIEW_REQUIRED assessment; a
general zero-free-entire dependence theorem remains an unread lead.
