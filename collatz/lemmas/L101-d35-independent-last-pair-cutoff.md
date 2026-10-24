# L101 — Independent d35 literal last-pair cutoff with a replacement cap

## Hypotheses

Use the full indexed table of L055, changing only H_0=5 and
H_24=32670656 (d=35 in L084). Thus r=25, J_0=8,
J_24=30998279, all J_i are strictly increasing and J_i>=2,H_i>=3.
Fix B=9250245 and an integer 0<=t<=B, in literal indexed order.
Put a_i=2 for i<23, a_23=2+18t, a_24=2+18(B-t) and kappa=23/11.
The tested real subsystem consists of s_25=s_0 and, for every
i=0,...,24 including closure,

\[
s_i\ge540/11,\qquad
s_{i+1}=2^{-a_i}\left((27/16)^{J_i}(3/2)^{H_i}s_i
                  -(12/11)(3/2)^{H_i}-1\right)+\kappa,
\]
\[
4J_i\log2\le\log s_i+\log(11/4).
\tag{1}
\]

No H guard, seed, minimum location, junction integrality, parity,
residue, valuation, actual-word or primitive-count premise is imposed.

## Conclusion

For every integer 0<=t<=B the endpoint equations alone have exactly
one real solution. It is positive rational and every unshifted input
n_i=s_i-kappa is greater than47. For every integer 2<=t<=9250245,
its own-input row24 J guard fails: its right-minus-left margin is
strictly below

\[
F=-8995174522561/500000000000<-17.99<0.
\tag{2}
\]

Consequently any tuple satisfying (1) has t=0 or t=1. This asserts
no survivor feasibility, early-support or cyclic-order reduction,
allocation-simplex exclusion or actual-word transfer. L100 is a
possible later companion, not a premise or an assembly here.

This is local REPRODUCTION under the prior SPECIALIZE assessment
`drafts/literature/2026-10-24-d35-independent-last-pair-cutoff.md`.
The changed finite certificate is the advance; no progress beyond the
inspected general affine/analytic machinery is claimed. The separate
step458 critical audit below found no defect. Attempt032, the failed
full S/C/H tests, both d0 witnesses and universal descent remain intact.

## Proof

### Independent imported criterion and endpoint premises

Apply only L077 (3)–(5) and its audited implication (7)–(12), with
p=23,q=24,tau=2. Its formal affine input is Halbeisen–Hungerbuehler,
*Optimal bounds for the length of rational Collatz cycles*, Acta
Arithmetica78 (1997),227–239, DOI10.4064/aa-78-3-227-239,
[section2 equations(2)–(4), Lemma2, pp.228–229](https://www.math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
The finite binary-word and nonzero-denominator hypotheses concern
formal affine composition; only that real algebra is used. Neither
the source theorem nor L077's quantified proof is reproved. The failed
full O/S/C conjunction of L084 supplies no premise.

The opposite H changes preserve K=397573379,N=630138897, with all
tails included. Use lambda_-=10584/10^14,lambda_+=10585/10^14,e=2.
L084's completed all-member audit covers the independent analytic/eta
data here; the fresh rational certificate below also verifies
0<lambda_-<Lambda=N log2-K log3<lambda_+<1.
For eta_i=kappa-(16/27)^{J_i}(12/11+(2/3)^{H_i}), exact arithmetic gives

\[
\eta_0=142223884206271/68630377364883>2,
\qquad e(1-\lambda_+)/\lambda_+=39999999995766/2117>47.
\]

Both subtracted positive powers decrease with increasing J,H. Since
J_24>=J_0,H_24>=H_0, eta_24>=eta_0>e. These are all L077 (3)
premises. Its endpoint uniqueness, positive rationality, uniform domain
and monotonicity therefore apply without assuming guard feasibility.
In particular the final input strictly decreases in t; growth of either
varying row is not assumed.

### Complete incoming certificate and the one replacement cap

At t=2, the last two tails are38 and166504376; the complete tail
sum is166504460. Use

\[
w=10^8(2/3)^{34}=1717986918400000000/16677181699666569,
\quad L_0=1,\quad L_i=w2^{i-1}\quad(1\le i\le24).
\]

The exact row0 multiplier is c_0=3^29/2^39>w>0. Every row1–23
has J>=15,H>=72 and actual tail at most38. Thus the already audited
L084 comparison gives c_i>=3^117/2^170>2. The fresh certificate also
encloses every actual log(c_i/2), with all23 lower endpoints positive.
Induction gives C_i(2)>=L_i>0 at all25 incoming indices0–24.
No bound is imposed on C_25=exp(-Lambda)<1; it remains in the
fixed-point denominator with both changing closing tails.

Retain the complete finite reciprocal sum:

\[
Q=\kappa\sum_{i=0}^{24}1/L_i
 =\kappa\left(1+(2/w)(1-2^{-24})\right)
 =67580051164552809819556541/31705341376688291840000000.
\]

Use exactly U=21000000000,T=24. The required C cap is

\[
R_C=Q/\lambda_-+Q+\kappa/L_{24}
=187489044665819986358454838929133547/
  9309784854704947200000000.
\tag{3}
\]

Exact comparison gives20138923465<R_C<20138923466<U. The positive
degree40 partial sum P_40(24)=sum_(k=0)^40 24^k/k! exceeds26462988572
and is strictly below exp(24). Hence U<exp(T), proving the changed
cap in L077 (4). The old cap20000000000 still fails. C's own
kappa/L_24 term is retained; H's different L_* term is unused.

### Own-input row24 test with complete analytic error

Reuse the assessed positive-real series coverage
[DLMF4.5.1](https://dlmf.nist.gov/4.5.E1),
[4.6.4](https://dlmf.nist.gov/4.6.E4),
[4.2.19](https://dlmf.nist.gov/4.2.E19). For x in{2,3,11/4},
z=(x-1)/(x+1) is respectively1/3,1/2,7/15, in(0,1). The existing
enclosure scheme gives P<log x<P+R, where
P=2 sum_(j=0)^99 z^(2j+1)/(2j+1) and
R=2z^201/[201(1-z^2)]. Its fresh rational evaluations verify

\[
0<\ell=693147180559/10^{12}<\log2,\quad
\log3<u=1098612288669/10^{12},\quad
\log(11/4)<v=1011600911679/10^{12}.
\]

The opposite interval endpoints also certify both Lambda bounds above;
all coefficient-amplified remainders are retained. The exponential
partial sum uses T=24>0. These are applications of the inspected series,
not new analytic results.

The complete incoming exponents at row24 are k=271907886,
d=306970749. The denominator includes row23's extra36 halvings.
Its own outgoing J_24 gives R_0=d+4J_24=430963865. Therefore

\[
24+271907886u-430963865\ell+v
=-8995174522561/500000000000=F<0.
\]

Both coefficients are positive. For the exact expression
E=24+k log3-R_0 log2+log(11/4), the full outward error satisfies

\[
649476131/10^{12}<F-E<649476132/10^{12}<1/1000.
\tag{4}
\]

Indeed F-E=k(u-log3)+R_0(log2-ell)+(v-log(11/4)); applying the
three complete series intervals in their indicated directions gives
(4), as recorded exactly in the certificate. No error term is dropped.
All L077 (3)–(5) data tests now hold. Its strict normalized-input bound
(11) makes the actual row24 J margin strictly below F at t=2;
its positive-coefficient formula(10) makes that margin decrease for
all larger t. This proves(2) on the full closed interval2<=t<=B,
including t=B with final tail2, contradicting the non-strict guard.

### Reproduction evidence and limits

Run `python3 scripts/postspell-word-count/certify_d35_independent_cutoff.py`.
Full evidence is saved in
`scripts/postspell-word-count/d35-independent-cutoff-certificate.json`:
244 exact comparisons pass with no failures. The script specializes
the earlier d34 certificate implementation to the independently approved
d35 constants; it is not an independent audit. It saves the complete
table/source hash, tails and closing counts, all25 incoming exponents
and reciprocals, all23 factor intervals, all analytic series terms and
remainders, the full cap and amplified own-input J error. Complete
incoming/factor/cap/tail records and the exact summary were inspected.
The finite evidence supplements the displayed comparisons and L077's
quantified implication. It certifies no guard-feasible survivor,
minimum/seed, integrality, realization, early-support/order reduction,
assembly or actual-word transfer. The independent audit below supersedes
the construction's pending-audit status.

### Independent critical audit — 2026-10-24, step458

This RESEARCH/REPRODUCTION proof audit uses the unchanged prior SPECIALIZE
assessment `drafts/literature/2026-10-24-d35-independent-cutoff-critical-audit.md`.
It found no defect in the stated literal d35 cutoff or complete finite
certificate. This independently verifies an existing restricted input;
it supplies no stronger bound or mathematical discovery beyond the
inspected sources. The precise affine and analytic citations above are
reused. The failed full O/S/C package is not invoked; L100 is not an
input to this audit. Attempt032 and both d0 witnesses remain valid.

**Complete independent reconstruction.** Run
`python3 scripts/postspell-word-count/audit_d35_independent_cutoff.py`.
The verifier reuses the inspected d34 independent-audit framework, with
all changed d35 operands freshly matched. It neither imports nor executes
either constructor. A separate transcription of all 25 original pairs
is compared with the complete canonical L055 table, then only H_0 and
H_24 are changed by -35 and +35. Direct partial sums reconstruct all
incoming exponents and the closing counts. The audit regenerates every
original certificate field, including all 244 comparison operands,
relations, differences and truth values, and compares the complete
comparison-name set to prevent omitted or duplicated checks. Saved order
is used only for presentation. All 2424 scalar leaves match, and all
206 additional exact checks pass, with no failures or mismatches.

The full audit certificate is
`scripts/postspell-word-count/d35-independent-cutoff-audit-certificate.json`.
It retains the reconstructed certificate, separate table, every analytic
term and remainder, additional comparisons with full operands, source
hashes and failures. The complete incoming, cap and factor-enclosure
records were also inspected with the bounded JSON inspector's selected
full-value mode. A hash or passing constructor flag is not the basis of
the verdict: all mathematical certificate fields were recomputed.

**Endpoint and domain applicability.** The table has integer strictly
increasing J_i>=8 and H_i>=5, r=25 and integer B=9250245. Both
changing tails contribute to N=630138897; K=397573379 is unchanged.
The independently reconstructed opposite-endpoint logarithm comparisons
give lambda_-<Lambda<lambda_+<1. Thus D=exp(Lambda)-1 is positive,
with lambda_-<D<lambda_+/(1-lambda_+). The exact eta_0 and domain
fractions displayed above agree with the independent reconstruction.
Increasing both J and H decreases the two positive terms subtracted
from kappa, so the checked J_24>=J_0,H_24>=H_0 give eta_24>=eta_0>2.
All other eta_i are strictly between zero and kappa by L077 (2).
These are precisely L077 (3), without guard-feasibility premises.

For completeness of the application, put x=2^(-18t), C=C_24(0)>0
and A=sum_(j<24)eta_j/C_j(0)>0. L077's already audited formulas give
n_0=(A+eta_24/(Cx))/D and
n_24=eta_24/D+CA(1+D)x/D. Both changing tails are retained through
the constant full product 1/(1+D); only the incoming prefix C_24
varies as Cx. Every coefficient is positive. The unchanged tail-2
rows give C_i>=1 for i<=23; hence n_i>=n_0>47 there. Independently
n_24>eta_24/D>47. The unique real fixed point therefore has the
claimed positive rational domain at every integer 0<=t<=B, including
t=B. No growth assumption at either varying row, minimum or seed enters.

**All incoming bounds and the complete C cap.** At t=2 the reconstructed
tails are exactly 38 and166504376, with total166504460. The row0
multiplier is exactly 3^29/2^39>w. For each row1–23 the verified
J>=15,H>=72 and actual tail<=38 imply c_i>=3^117/2^170>2, since
the bases 27/16 and3/2 exceed1. Each actual log(c_i/2) is also
independently positive. Multiplying these inequalities yields all25
incoming lower bounds, including the empty prefix and row24. Their
complete reciprocals reproduce Q and the full fraction (3). There is
no lower bound on C_25; its value exp(-Lambda)<1 remains in D.

In particular, the final shift term is
kappa/L_24=383575179092331087/158526706883441459200000000.
The verified strict bounds are
20138923465<R_C<20138923466<21000000000.
All41 positive exponential terms through degree40 were regenerated by
the recurrence t_0=1,t_k=24t_(k-1)/k. Their sum is greater than
26462988572, proving U<exp(24). The old cap20000000000 still fails;
neither that failure nor the failed support test is erased. H's distinct
last term kappa/L_* is not substituted for C's last term.

**Analytic signs and complete amplified error.** Successive powers
regenerate all300 terms and all three geometric remainder bounds for
log2,log3,log(11/4). The positive-real arguments are in the assessed
domains, so the stated strict lower and upper enclosures apply. All
coefficients multiplying the remainders are included in the Lambda,
factor and row24 intervals. A second evaluation uses128 terms at
2,3/2,11/8 and the identities
log3=log2+log(3/2), log(11/4)=log2+log(11/8).
It independently encloses Lambda as
(N-K)log2-K log(3/2), and E as
24+(k-R_0+1)log2+k log(3/2)+log(11/8).
Coefficient signs select opposite interval endpoints where needed.
Every alternate factor interval, the alternate Lambda interval and
the alternate E interval lie strictly inside the corresponding original
intervals. This is reuse of the assessed analytic method, not an
uncertified floating-point comparison or a new analytic theorem.

The reconstructed incoming exponents are k=271907886,d=306970749;
the latter contains all36 transferred halvings. The outgoing J_24,
not an incoming row's guard, gives R_0=430963865. Exact substitution
reproduces F in (2). Both methods verify (4), including the full
log(11/4) error: 649476131/10^12<F-E<649476132/10^12.
This encloses the difference between the rational upper expression and
its exact logarithmic expression; it is not a two-sided enclosure of
the actual guard margin.

**Whole-interval implication and limits.** All quantities in L077 (11)
are positive and S=sum eta_i/C_i<Q, so
s_24/C_24<Q/lambda_-+Q+kappa/L_24=R_C<U<exp(24).
Taking logarithms gives the actual row24 margin strictly below E<F<0
at t=2. In the formula for n_24 above, the coefficient of x is strictly
positive; as t increases, x strictly decreases. Thus s_24 and its
own-input J margin strictly decrease. This proves the same bound for
every integer2<=t<=B, with a_24(B)=2; it is not a sampled-parameter
inference. The strictly negative margin contradicts the non-strict guard.

No mathematical correction or dependency change was required. This
canonical audit supersedes older pending-audit wording for L101 in the
overview; PROOF.md and DAG.md are unchanged because the argument and
its direct inputs are unchanged. No survivor feasibility, full guard
conjunction, integer realization, early-support/order reduction,
assembly, actual-word transfer or universal eventual descent is proved.

## Mathlib

Full matching coverage for this table specialization is unchecked.
Supporting log, exponential and rational-sum facts are not a matching
cutoff theorem. Unknown coverage is not absence; no external Lean
verification is claimed.
