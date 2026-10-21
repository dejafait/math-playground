# L092 — Uniform literal last-pair cutoff for d=6,...,33

## Hypotheses

Fix an integer 6<=d<=33. Take L055's 25 indexed pairs, changing only
H_0=40-d and H_24=32670621+d; every J and every other H is unchanged.
Set B=9250245 and kappa=23/11. For an integer 2<=t<=B set
b_i=0 for 0<=i<=22, b_23=t, b_24=B-t and a_i=2+18b_i.
Suppose real s_0,...,s_25 satisfy s_25=s_0, s_i>=540/11 and,
in literal indexed order, for every 0<=i<25,

\[
s_{i+1}=2^{-a_i}\left((27/16)^{J_i}(3/2)^{H_i}s_i
                  -(12/11)(3/2)^{H_i}-1\right)+\kappa,
\qquad 4J_i\log2\le\log s_i+\log(11/4).
\]

Logarithms are natural. Every outgoing own-input non-strict J guard
and endpoint, including closure, is required. There is no minimum,
seed, H guard, integer-junction, parity, residue, exact-valuation,
primitive-count or actual-word premise.

## Conclusion

No such tuple exists for any specified d and t. L077 rejects row24's
own-input J guard over the whole interval 2<=t<=9250245, including
t=B where a_24=2.

This is RESEARCH/KNOWN_IMPORTED under the prior IMPORT assessment
`drafts/literature/2026-10-20-uniform-last-pair-cutoff.md`: a local
application of existing audited data, not a new cutoff mechanism or
progress beyond the checked sources. The separate critical applicability
audit below found no defect. No survivor verdict, early-support assembly,
cyclic-order reduction, integer exclusion or actual-word transfer is
asserted. Universal eventual descent remains unresolved.

## Proof

Apply L077 independently of the full C077a conjunction. Its parameters
are r=25,p=23,q=24,tau=2<=B. L055's integer J table is strictly
increasing from J_0=8 to J_24=30998279. Here H_0>=7, and every
other H is at least 3. These are precisely the d=6,...,33 members of
L084's assessed family. The allocations and real subsystem above match
L077 (6) exactly at every input, including s_25=s_0.

Use L084's independent C constants

\[
\lambda_-=10584/10^{14},\quad\lambda_+=10585/10^{14},\quad e=2,
\quad T=24,\quad U=20000000000,
\]
\[
\ell=693147180559/10^{12},\quad
u=1098612288669/10^{12},\quad v=1011600911679/10^{12},
\]
\[
w_d=10^8(2/3)^{d-1},\quad L_0=1,\quad
L_i=w_d2^{i-1}\ (1\le i\le24),\qquad
Q_d=\frac{23}{11}\sum_{i=0}^{24}\frac1{L_i}.
\]

Every independent data test is supplied by the following canonical
L084 statements and its completed all-member critical audit:

* **L077 (3).** L084 (2) gives the positive Lambda enclosure at
  K=397573379,N=630138897. Its independent cutoff section proves
  eta_24>=eta_0>2 and
  e(1-lambda_+)/lambda_+=39999999995766/2117>47 for every member.
  Thus both eta bounds, lambda_+<1 and the domain test hold here.
* **L077 (4), incoming prefixes and sum.** L084 (1),(5) and its
  separate C-package audit give 0<L_i<=C_i(2) at every incoming
  index 0 through 24. At this boundary the actual tails are
  a_23=38,a_24=166504376. The complete finite reciprocal sum is
  1+(2/w_d)(1-2^(-24)), so Q_d is exactly the required sum times
  kappa. No incoming term is omitted. The closing product C_25
  is retained in Lambda, without imposing a lower prefix bound on it.
* **L077 (4), normalized cap and analytic directions.** L084 (6)
  defines exactly R_C(d)=Q_d/lambda_-+Q_d+kappa/L_24. Its completed
  all-member audit reconstructs both caps for all 37 members, places
  cap failures only at d=34,...,37 and explicitly records that all
  other cap comparisons pass. Hence R_C(d)<=U throughout the
  present range. This uses the audited all-member statement, not
  display (7), whose bound is restricted to d<=4, and not the H cap
  with denominator L_*=1. The same audited analytic package gives
  U<exp(24), 0<ell<log2, log3<u and log(11/4)<v.
* **L077 (5).** L084 (8) and its audit give incoming exponents
  k_24=271907920-(d-1), d_24(2)=306970783-(d-1), and exactly
  \[
  T+k_{24}u-(d_{24}(2)+4J_{24})\ell+v
  =F^C(d)=-2102267684691/500000000000-(d-1)(u-\ell)<-4.20<0.
  \]
  These certified exponents include the extra 36 boundary halvings
  in row23. The changed closing tail remains in N rather than this
  incoming prefix. The positive log3 and negative log2 coefficients
  have the enclosure directions required in L077.

All L077 (3)–(5) tests therefore hold for each specified d. Invoke its
already proved full-interval conclusion: row24's right-minus-left
own-input J margin is strictly negative at every integer 2<=t<=B.
The hypothesized non-strict guard requires that same margin to be
nonnegative, a contradiction. L077 includes both varying tails and
the final tail 2; no monotonicity reproof or new calculation is needed.

The standard affine input already specialized in L077/L084 is
Halbeisen–Hungerbuehler, *Optimal bounds for the length of rational
Collatz cycles*, Acta Arith. 78 (1997), 227–239,
DOI 10.4064/aa-78-3-227-239,
[section 2, equations (2)–(4), Lemma 2, pp. 228–229](https://www.math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
Only formal real affine composition with positive fixed-point denominator
is used. Positive-real analytic coverage is the already inspected
[DLMF 4.5.1](https://dlmf.nist.gov/4.5.E1),
[4.6.4](https://dlmf.nist.gov/4.6.E4) and
[4.2.19](https://dlmf.nist.gov/4.2.E19); exact bounds and qualifications
are imported from L077/L084. No source theorem is reproved.

L087 is the narrower d=5 comparison, not an input to this proof.
L091 motivates a possible later assembly and is not invoked. L084's
failed S offsets and Attempt 032's full-test stop remain valid; neither
is a premise of this independent cutoff. Both original d=0 rational
witnesses remain valid. No statement about t=0,1 follows here.

### Independent critical applicability audit — 2026-10-21, step 390

This RESEARCH/REPRODUCTION proof audit uses the prior SPECIALIZE
assessment `drafts/literature/2026-10-21-uniform-last-pair-critical-audit.md`.
It found no defect in the stated citation-only application. This validates
the existing local cutoff input; it supplies no new exclusion, numerical
certificate or mathematics beyond the cited results. The precise primary
citations above and their inspected coverage are reused. No criterion,
monotonicity argument or finite certificate is reconstructed.

**Table, counts and subsystem.** Inspection of all 25 canonical L055
pairs confirms integer, strictly increasing J values, starting at 8 and
ending at 30998279. For 6<=d<=33 the changed H_0 lies between 7 and
34, the changed H_24 is positive and exceeds H_0, and every other H
is unchanged and at least 3. These are exactly members of L084's
1<=d<=37 family. The opposite H changes preserve sum H; the specified
two tails preserve sum a=2*25+18B. Therefore L077 (1) has precisely
L084's K=397573379,N=630138897. Here r=25,p=23,q=24 and
tau=2<=B=9250245. Every real endpoint, lower-domain bound and
non-strict own-input J guard is L077 (6), with the same kappa and
s_25=s_0. Only the L055 pair table is imported, not its stronger
witness hypotheses. No rotation or minimum selection enters.

**Every condition in L077 (3).** L084 (2) and its independent analytic
audit give 0<lambda_-<Lambda<lambda_+<1 with the exact constants
printed above. The independent C proof and all-member audit establish
eta_0>2 and eta_24>=eta_0 throughout the family: the least first-row
H in that larger family is 3, and both subtracted eta factors decrease
with J and H. Consequently e=2 meets both endpoint eta requirements.
The audited exact quotient 39999999995766/2117>47 is the required
e(1-lambda_+)/lambda_+ domain comparison. These are unconditional
finite data; none uses the failed support-offset test.

**All incoming bounds and the full reciprocal sum in L077 (4).**
The boundary t=2 gives exactly a_23=38 and a_24=166504376.
The C package in L084 proves c_0>w_d and c_i>2 for every row
1 through 23 with these actual tails, including tail 38 at row23.
Its induction yields L_0=C_0=1 and 0<L_i<=C_i(2) for all
1<=i<=24. Thus all 25 incoming indices are covered. The complete
finite reciprocal sum is 1+(2/w_d)(1-2^(-24)); Q_d is exactly
kappa times this sum, so its required weak inequality holds with
equality. The closing row24 is absent from incoming C_24 and present
in the full product C_25=exp(-Lambda). There is no lower incoming
prefix requirement on C_25 and no omitted closing equation.

**Cap scope and analytic directions in L077 (4).** The required cap
is exactly L084 (6)'s R_C(d), including kappa/L_24. The H cap's
different denominator L_*=1 is not substituted. Display (7) covers
only d<=4 and alone would be insufficient. The completed canonical
audit explicitly reconstructs both caps for all 37 members, records
their failures precisely at d=34,...,37 and states that all other
cap comparisons pass. L084's conclusion independently records that
no other tested inequality fails. These statements affirmatively cover
every requested d=6,...,33, without relying on a certificate preview
or a bare success flag. There is no conflict with the narrower display.
The same audit verifies the degree-40 positive exponential lower sum
and intermediate threshold giving U<exp(24), as well as the exact
outward inequalities 0<ell<log2, log3<u and log(11/4)<v.
Thus every positivity, rationality and analytic direction in (4) matches.

**Boundary test (5) and the full-interval implication.** The incoming
exponents in L084 (8) are k_24=271907920-(d-1) and
d_24(2)=306970783-(d-1). Only the changed H_0 occurs in this
prefix; the compensating H_24 remains in the full product. The
denominator prefix includes row23's extra 36 halvings, while the
closing tail belongs to N. Together with the unchanged outgoing
J_24=30998279 these are precisely the operands of L077 (5), giving
the displayed F^C(d). The positive log3 coefficient takes its upper
bound u; the negative log2 coefficient takes its lower bound ell.
The audited expression is strictly below -4.20 for all 37 members,
hence for this range. No boundary datum is borrowed from the d=0
benchmark or from L087's d=5 application.

L077's existing conclusion applies to any real endpoint tuple in this
literal family, since its positive-denominator uniqueness identifies the
tuple used in its boundary estimate. Its audited proof (9)–(12) retains
both changing tails in closure and shows that the same row24 margin
decreases over the entire parameter interval. It therefore makes
log(s_24)+log(11/4)-4J_24 log2 strictly negative for every integer
2<=t<=B. The hypothesized guard at that same outgoing input requires
this expression to be nonnegative. The contradiction includes t=B,
where a_24=2; it assumes no growth of either varying row. This is
the quantified theorem application, not an extrapolation from sampling.

**Scope and dependency check.** Only L055's pairs, L077's independent
criterion and L084's audited finite data are direct inputs, as recorded
in the unchanged DAG. L087 is comparison only, and L091 is motivation
for a later assembly, not a premise. Attempt 032's failed S test and
full-conjunction stop remain intact. No full C077a or L083 theorem,
survivor verdict, H/seed/minimum condition, integer junction, realization
or primitive-count premise has entered. Both original d=0 witnesses
remain valid. Survivor exclusion, broader allocation assembly, cyclic
orders, actual-word transfer and universal eventual descent remain open.
The argument is unchanged, so PROOF.md and DAG.md are not edited;
this canonical audit supersedes their older pending-audit prose for L092.

## Mathlib

Full matching coverage has not been checked. Supporting affine,
logarithm and exponential facts do not constitute this application;
no absence or formal verification is claimed.
