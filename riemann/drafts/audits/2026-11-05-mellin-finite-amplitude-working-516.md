# Finite Mellin amplitude audit — step516 working record

Approved target and classification: exact finite T_amp test in
`drafts/literature/2026-11-05-mellin-finite-amplitude-audit.md`;
SPECIALIZE / REPRODUCTION. Reused the completed step515 primary-source,
duplicate and failure comparison; the global-import stop is separate.
Inputs inspected: L019, audited L797 and audited L798. No new source
premise, supplement or cross-notebook input is needed.

Main gap is actual-Xi all-degree mixed positivity. This attempt pays
only a local amplitude term. Continue if the normalized finite cost
is <=31 eta/25 on all D; distinguish a failed supremum majorant from
a failed integral. Global tails, endpoint, quotients/inversion and
sufficient signs remain unresolved.

Reasoning saved before completion: Re A>0 gives |Im a|<1/sqrt(2)<5/7.
Thus z=x+av, |v|<=3/(16u), has |Im z|<pi/4-13/(112u) and
Re z>=u-3/(16u)>0. Candidate theta parameter bound is

    Re(pi exp(2z)) > Q (7/8) sin(13/(56u)) > Q/(5u).

For the last comparison use u>3, sin t>=t(1-t^2/6), and an exact
rational comparison. Q/(5u)>1 follows from the increase of e^(2u)/u
on u>=3 and pi e^6>1000 (L797).

On compact subsets of |Im z|<pi/4 the theta series is normally
convergent by a polynomial-times-Gaussian majorant. Dividing by H
gives the n=1 correction -(3/(2pi))exp(-2z), plus n>=2 terms with
coefficients n^4-(3/(2pi))n^2 exp(-2z). The first correction is
bounded by eta's first term. For t=Re(pi exp(2z))>1, the absolute
tail is at most sum (n^4+n^2/2) exp(-(n^2-1)t). Adjacent terms have
ratio <=(81/16)exp(-5t)<1/10, since e^5>98. Its first term is
18 exp(-3t); hence the sum is <20 exp(-3t).

L798 supplies decrement 85Qv^2/48 and B<(2801/600)Q. The normalized
phase-weight integral is <sqrt(2801/2125)<23/20<31/25. This would
prove a stronger finite amplitude allowance once the details and
factorization are written canonically. No candidate RH solution.

Completed: the full proof, exact comparisons, source qualifications
and Mathlib status are canonical in L799. The simpler sine estimate
sin y>(99/100)y gives the explicit parameter margin 9009/44800>1/5.
No counterexample or failed bound arose. The resulting <23eta/20
allowance is a source reproduction with independent review pending.
Reuse the unchanged approved assessment and exact target for that
critical review; do not reopen global assembly or source supplements.
