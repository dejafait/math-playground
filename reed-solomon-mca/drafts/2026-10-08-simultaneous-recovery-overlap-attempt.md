# Simultaneous recovery — overlap compatibility attempt

Completed bounded attempt on the unchanged approved eleven-candidate target and
the saved EXPLORE assessment
`drafts/literature/2026-10-08-nine-union-simultaneous-recovery-count.md`.
Main gap: arbitrary sixteen-error equality. Essential inputs: L010,
audited L042–L043, and the unaudited partial bound L045. No rational
original chart, universal finite lift or equality is assumed.

The intermediate test is whether the all-eight-moment identities exclude
the twelve-candidate profiles j=11 or j=12. Their prospective exclusion
would prove eleven locally; extraction, other patterns, challenge source
identification and L044–L045 audits remain independent. Continue if
actual moment compatibility yields a new uniform restriction or eleven;
abandon the relaxed threshold only after a fully verified twelve-candidate
pencil. No such pencil or eleven-count proof was obtained.

The attempted mechanism uses the difference of L043's six-coordinate
word n(mu) and its recovered fourth error. For an overlap K={b} union S,
b in B and |S|=3 in O, this codeword is supported on nine labels.
Its degree-below-eight polynomial therefore has the seven known roots
O minus S. Write W(X)=product_(w in {w_1,w_2,w_3})(X-w). At every
coordinate of B other than b, the attempted elimination uses equations
of the form

    a_x(mu) product_(s in S)(x-s) = u W(x),

with a_y=-mu, a_z=1, a_h=q-mu*p,
a_d=1-(1+mu)r and nonzero u. These equations supply no bound eleven.
The direct single-tag determinant has the same degree budget as L010.

Known-result and duplicate coverage is reused from the supplied assessment.
The fixed opposite-label finite family, L016 fixed-triple enumeration,
and ATTEMPTS/021 support-only mechanism are not repeated. No external
source review, script, lemma or cross-notebook input has been added.

## Attempted elimination and its exact stopping point

This is a failed counting attempt, not a canonical theorem input. The
following records the full calculation so its limitation can be checked.
It makes no new lemma claim and is not inserted into the main argument.

Consider the putative twelve case. L045, still awaiting its separate
audit, makes each recovered error full weight and its support unique.
For an overlapping support K={b} union S, the codeword n-omega is
supported in B union S, of size nine. By L010's moment-kernel identity
it is an evaluation of P of degree at most seven. It is nonzero because
at least three singleton coefficients of n remain outside K. The seven
zeros O minus S therefore give

    P(X)=u product_(o in O minus S)(X-o),  u!=0.

Let f_S(X)=product_(s in S)(X-s). Since O is the disjoint union of
H minus U and the three w-labels, product_(o in O)(X-o)=Q(X)W(X).
For x in B minus {b}, all Q(x), W(x), and f_S(x) are nonzero, and
P(x)=n_x=c_x*a_x(mu). Cancelling Q(x)=c_x gives exactly

    a_x(mu) f_S(x)=u W(x),  x in B minus {b}.          (A)

In particular all five a_x(mu) in (A) must be nonzero. This is a
necessary restriction on actual recovery, rather than an assumption
that a quotient-compatible support has full weights. The factor u
may differ from one support to another. No subfield condition on
mu's original finite parameter, p,q,r or u has been imposed here.
The eligible mu itself lies in F_97 by L043; different eligible mu
give different original parameters by its formula (5).

For M_b=B minus {b}, put

    Delta_(b,x)=product_(v in M_b minus {x})(x-v),
    C_(b,x)=W(x)/Delta_(b,x),
    H_mu=q-p*mu,  D_mu=1-r-r*mu.

Every Delta is nonzero. The degree-four coefficient of the interpolant
of five values v_x at M_b is sum_x v_x/Delta_(b,x), by the leading
coefficients of the five Lagrange basis polynomials. Applied to (A),
the cubic f_S requires sum_x C_(b,x)/a_x(mu)=0. Clear only the
already nonzero a_x(mu) to obtain the necessary polynomial

    P_b(mu)=sum_(x in M_b) C_(b,x)
                         product_(v in M_b minus {x}) a_v(mu)=0. (B)

This interpolant calculation is performed to expose the dependence
on common p,q,r and W; it is not a reproof of the imported recurrence
theorem. That theorem and its all-eight-moment applicability remain
exactly as cited in L043. Equation (B) is only a necessary test here:
it does not enforce that the interpolant is monic with three distinct
roots in O, recover the tag coefficient, or verify a finite candidate.

The four tag cases expand as follows. Subscripts b on C are suppressed;
each C in a formula is evaluated for that formula's M_b.

* For b=y_i and y the other y-label,

      P_b=H_mu D_mu(C_y-mu(C_z1+C_z2))
                         -mu(D_mu C_h+H_mu C_d).

  This has degree at most three. At mu=0 it is
  q(1-r)C_y!=0. At mu=-1 the four coefficients other than H_mu
  are one, and sum_(x in M_b) C_x=0 because W has degree three.
  Consequently P_b(-1)=(1-p-q)C_h!=0. Thus P_b is not the zero
  polynomial, and this test permits up to three eligible parameters
  for each y tag; it does not reduce L010's capacity three.

* For b=z_i and z the other z-label,

      P_b=mu R_b,
      R_b=-H_mu D_mu(C_y1+C_y2)
                   +mu(H_mu D_mu C_z+D_mu C_h+H_mu C_d).

  The residual R_b has degree at most three. As in the first case,
  P_b(-1)=(1-p-q)C_h!=0, so R_b is nonzero. The removed factor
  mu concerns a stipulated error, not an eligible nonuniversal
  parameter. This again permits up to three per z tag.

* For b=h, put C_Y=C_y1+C_y2 and C_Z=C_z1+C_z2. Then

      P_h=mu R_h,
      R_h=-D_mu C_Y+mu(D_mu C_Z+C_d).

  Here C_Y+C_Z+C_d=0 by cubic interpolation. Hence R_h(-1)=0,
  so P_h is divisible by mu(mu+1), and the remaining factor has
  degree at most one. It is not identically zero: if C_Y!=0,
  R_h(0)=-(1-r)C_Y!=0; if C_Y=0 then C_Z=-C_d!=0 and
  R_h=mu*r*(1+mu)*C_d. Thus the test permits at most one
  eligible h overlap, exactly L010's remaining capacity.

* For b=d,

      P_d=mu R_d,
      R_d=-H_mu(C_y1+C_y2)
                         +mu(H_mu(C_z1+C_z2)+C_h).

  The residual has degree at most two. Evaluation gives
  P_d(-1)=(1-p-q)C_h!=0, so R_d is nonzero. This permits up
  to two eligible d overlaps, again the existing locator capacity.

All nonzero evaluations use the retained triple gates, W(x)!=0 on B,
and distinct B labels. No claimed positive parameter count follows
from these upper bounds. Degenerate leading coefficients can reduce
the degrees; their vanishing is not established uniformly over labels.

The residual per-tag budgets are therefore (1,2,3,3,3,3) in the order
(h,d,y_1,y_2,z_1,z_2). Both L045 profiles remain below them: for example
(1,2,2,2,2,2) sums to eleven and (1,2,3,2,2,2) sums to twelve.
This is a failure of the isolated polynomial-degree test, not evidence
that either profile is moment compatible. The equations for different
tags share p,q,r and W, and their interpolating cubics must split in
the same ten-label set O. Those simultaneous conditions were not solved.
The possible disjoint fourth support also remains unclassified.

## Decision and continuation

Outcome: EXPLORATION. One new symbolic elimination attempt reproduced
the existing individual capacities and established neither eleven nor
a twelve-candidate counterexample. It supplies no new theorem input,
global bound, certificate or novelty claim. The original main gap and
the 11/q–16/q interval are unchanged. Mathlib coverage was not checked.

Abandon summing the degrees in (B) as a proof of eleven. The unchanged
approved target remains ready under its saved assessment. A concrete
next test is to couple (A) for actual overlaps whose outside triples
share a pair. Their cubic ratio cancels that common pair; require the
same h,d recovery and singleton values at both parameters, retaining
arbitrary original finite chart and the j=11/j=12 alternatives. Such
a pair is not assumed to exist: the no-repeated-pair branch must be
retained. A contradiction for an assumed pair alone would be an
intermediate restriction, not the eleven bound. L010, L041, audited
L042–L043 and unaudited L045 remain essential; L044 is optional only
for rational normalized-weight reduction and remains unaudited.
Universal extraction, other patterns, L044–L045 audits, and ABF26
identification stay open. This is the first mathematical exploration
after step 098's ADVANCE, not a new literature turn or budget reset.
