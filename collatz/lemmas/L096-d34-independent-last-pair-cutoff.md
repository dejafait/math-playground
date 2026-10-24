# L096 — Independent d34 literal last-pair cutoff with a replacement cap

## Hypotheses

Use all 25 indexed pairs of L055, changing only H_0=6 and
H_24=32670655 (the d=34 member of L084). In particular J_0=8,
J_24=30998279 and the J_i are strictly increasing, with J_i>=2,H_i>=3.
Fix B=9250245 and an integer 0<=t<=B, in literal indexed order. Set
a_i=2 for i<23, a_23=2+18t and a_24=2+18(B-t).
Let kappa=23/11. The tested real subsystem has s_25=s_0 and, for
every i=0,...,24, including closure,

\[
s_i\ge540/11,\qquad
s_{i+1}=2^{-a_i}\{(27/16)^{J_i}(3/2)^{H_i}s_i
                 -(12/11)(3/2)^{H_i}-1\}+\kappa,
\]
\[
4J_i\log2\le\log s_i+\log(11/4).
\tag{1}
\]

No H guard, seed, minimum location, integer junction, parity, residue,
valuation, actual-word or primitive-count premise is imposed.

## Conclusion

For every integer 0<=t<=B the endpoint equations alone have exactly one
real solution. It is positive rational and every unshifted input
n_i=s_i-kappa is greater than 47. For every integer 2<=t<=9250245,
its own-input row24 J guard fails: its right-minus-left margin is
strictly below

\[
F=-4396220984253/250000000000<-17.58<0.
\tag{2}
\]

Thus any tuple satisfying (1) must have t=0 or t=1. This asserts no
feasibility or H verdict for those parameters and supplies no early-support,
cyclic-order, allocation-simplex or actual-word reduction. L095 is a
possible later complement, not a premise or an assembly here.

This is local REPRODUCTION under the prior SPECIALIZE assessment
`drafts/literature/2026-10-23-d34-independent-last-pair-cutoff.md`,
not progress beyond the inspected general affine/analytic machinery.
The changed finite C certificate is the local advance. The separate critical
audit below found no defect. Attempt032, both d0 rational witnesses and universal
eventual descent remain unchanged.

## Proof

### Imported criterion and independent endpoint data

Apply only L077's independent sufficient criterion (3)–(5) and its
already proved implication (7)–(12), with r=25,p=23,q=24,tau=2.
L084's full failed O/S/C conjunction is unused. The formal affine
composition underlying L077 is Halbeisen–Hungerbuehler, *Optimal bounds
for the length of rational Collatz cycles*, Acta Arithmetica 78 (1997),
227–239, DOI 10.4064/aa-78-3-227-239,
[section2, equations(2)–(4), Lemma2, pp.228–229](https://www.math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
The assessed theorem and essential proof cases concern finite binary
words and nonzero-denominator affine fixed points. Here only formal
real affine algebra is needed; no coding or realization converse is
imported, and neither that theorem nor L077's quantified proof is reproved.

The opposite changes to H preserve totals K=397573379,N=630138897,
where N counts all tails. Use

\[
\lambda_-=10584/10^{14},\quad\lambda_+=10585/10^{14},\quad e=2.
\]

L084's audited all-member analytic/eta data cover this d. The fresh
certificate below also verifies 0<lambda_-<Lambda<lambda_+<1, where
Lambda=N log2-K log3. For the eta_i in L077 (2),

\[
\eta_0=23/11-(16/27)^8(12/11+(2/3)^6)>2.
\]

Both subtracted powers decrease when J or H increases. The actual
J_24>=J_0,H_24>=H_0 therefore give eta_24>=eta_0>e. Also

\[
e(1-\lambda_+)/\lambda_+=39999999995766/2117>47.
\]

These are exactly L077 (3). Its endpoint uniqueness, positivity, rationality,
domain and monotonicity conclusions apply independently of boundary tests
and of any guard feasibility. In particular the last input decreases in t;
no growth assumption on either varying row is made.

### Complete incoming data and replacement C cap at t=2

At this boundary the actual last tails are 38 and 166504376. They
sum with the other tails to 166504460. Take

\[
w=10^8(2/3)^{33}=858993459200000000/5559060566555523,
\quad L_0=1,\quad L_i=w2^{i-1}\ (1\le i\le24).
\]

Row0 has multiplier c_0=3^30/2^40>w. Each row1 through23 has
J_i>=15,H_i>=72 and actual tail at most38. L084's audited exact
comparison 3^117/2^170>2 therefore bounds each c_i>2 at this
boundary. The certificate additionally retains strictly positive full
log(c_i/2) intervals for every one of these 23 factors, with all
amplified errors. Positive multiplication gives C_i(2)>=L_i for
every incoming i=0,...,24, including the empty prefix and row24.
No bound is imposed on C_25=exp(-Lambda)<1: it stays in the fixed-point
denominator. The complete reciprocal sum is

\[
\sum_{i=0}^{24}1/L_i=1+(2/w)(1-2^{-24}),\qquad
Q=\kappa\sum_{i=0}^{24}1/L_i
 =33575514807333220126518847/15852670688344145920000000.
\]

Use exactly one replacement pair U=21000000000,T=24. C's required
cap, with its own last denominator L_24, is exactly

\[
R_C=Q/\lambda_-+Q+\kappa/L_{24}
=1024643396328334125257370040340156339/
  51203816700877209600000000.
\tag{3}
\]

Exact rational comparison gives
20011074610<R_C<20011074611<U. The positive sum
P_40(24)=sum_(k=0)^40 24^k/k! satisfies
26462988572<P_40(24)<exp(24), hence U<exp(T).
This freshly certifies L077 (4)'s changed cap; the old fixed
U=20000000000 fails and remains recorded in L084/Attempt032.
H's different cap term kappa/L_* is never substituted here, and
L095's H certificate is not used as a C certificate.

### Own-input row24 and full analytic error

Use the outward rationals

\[
\ell=693147180559/10^{12}<\log2,\quad
u=1098612288669/10^{12}>\log3,\quad
v=1011600911679/10^{12}>\log(11/4).
\]

These positive-real analytic bounds reuse the assessed coverage
[DLMF4.5.1](https://dlmf.nist.gov/4.5.E1),
[4.6.4](https://dlmf.nist.gov/4.6.E4) and
[4.2.19](https://dlmf.nist.gov/4.2.E19). The already assessed rational
series enclosure at x in {2,3,11/4}, with z=(x-1)/(x+1) in (0,1), is
P=2 sum_(j=0)^99 z^(2j+1)/(2j+1)<log x<P+R,
R=2z^201/[201(1-z^2)]. The certificate freshly evaluates these sums,
all remainders and opposite-endpoint Lambda bounds. Its positive degree40
exponential lower sum uses T=24>0. No new analytic theorem is required.

The complete incoming exponents at row24 are
k_24=271907887,d_24(2)=306970750. In particular the denominator
includes row23's actual extra36 halvings. The own outgoing J_24 gives
d_24(2)+4J_24=430963866. Consequently L077 (5) is exactly

\[
24+271907887u-430963866\ell+v
=-4396220984253/250000000000=F<0.
\]

Both integer coefficients are positive. Relative to the exact expression
E=24+k_24 log3-(d_24(2)+4J_24)log2+log(11/4), the complete
outward error, including the v error, obeys the certified rational bounds

\[
649476133/10^{12}<F-E<649476134/10^{12}<1/1000.
\tag{4}
\]

Thus no unamplified or omitted logarithm error supplies the sign.
All L077 (3)–(5) premises hold. Its strict normalized-input inequality
(11) and own-input comparison (12) put the actual row24 J margin
strictly below F at t=2. Its positive-coefficient formula (10) makes
that margin decrease for every larger t. This proves (2) on the entire
closed integer interval 2<=t<=B, including t=B with final tail2.
The non-strict J guard in (1) is contradicted by a strictly negative
margin. No minimum, seed, guard feasibility or other allocation/order
exhaustion is needed.

### Reproduction evidence and qualifications

Run `python3 scripts/postspell-word-count/certify_d34_independent_cutoff.py`.
Full evidence is in
`scripts/postspell-word-count/d34-independent-cutoff-certificate.json`:
244 rational/integer comparisons pass, no failures. It saves the full
table and boundary tails, source hash, all 25 incoming exponents and
reciprocals, all 23 full-factor analytic intervals, exact series terms
and remainders, complete cap, exponential terms and amplified J error.
The full selected incoming array, factor enclosures, cap, tails and
summary were inspected; these are complete outward certificates, not
truncated numerical previews. The calculation supplements the displayed
exact comparisons and the imported quantified implication. It does not
independently audit that implication or certify integer realization.

### Independent critical audit — 2026-10-23, step422

This RESEARCH/REPRODUCTION proof audit uses the prior SPECIALIZE assessment
`drafts/literature/2026-10-23-d34-independent-cutoff-critical-audit.md`.
It found no defect in the independent cutoff, endpoint/domain assertion
or complete new finite certificate. It validates this existing local
specialization; it adds no stronger exclusion or claim of progress beyond
the inspected source machinery. Import audited L077 (3)–(12) with the
precise affine and analytic citations above, rather than reprove its
criterion. L055 supplies the indexed pairs only. L084's independent
C/all-member audit supplies the matching scope and preserves its failed
old cap; its full failed conjunction is never invoked.

**Independent full reconstruction.** Run
`python3 scripts/postspell-word-count/audit_d34_independent_cutoff.py`.
The program neither imports nor executes the constructor. A separate
transcription of all 25 L055 pairs matches the canonical table; exactly
H_0 and H_24 change by -34 and +34. It reconstructs every mathematical
field of the original certificate, including all 244 comparison records
with fresh operands, differences and verdicts. Exact key sets, array
lengths and unique comparison names prevent silent omissions. All 2424
recursive leaf comparisons and 205 additional checks pass, with no
mismatch or failed inequality. These counts include repeated operands,
not distinct mathematical conclusions. Full evidence and source hashes
are in `scripts/postspell-word-count/d34-independent-cutoff-audit-certificate.json`.
The construction certificate is unchanged.

**Every independent premise.** Integer domains, increasing J, unchanged
K=397573379,N=630138897, and all 25 tails match L077 (1)–(2).
The Lambda interval is strictly inside [lambda_-,lambda_+], itself
inside (0,1). The factored eta_0 is strictly greater than e=2;
the checked J_24>=J_0,H_24>=H_0 and decreasing subtracted powers give
eta_24>=eta_0. No large-power numerical approximation is needed for
that last eta. The exact domain bound is 39999999995766/2117>47.
These certify all of (3), independently of any unknown guards. L077's
unique rational fixed point and uniform strict lower domain therefore
apply for every 0<=t<=B. Its unchanged-row growth proof uses only
rows0–22; neither varying row is required to grow.

At tau=2 the last tails are exactly 38 and 166504376. All incoming
prefix exponents are recomputed by direct sums of the actual rows;
the closing exponents are separately K,N. The exact row0 coefficient
3^30/2^40 exceeds w. For each row1–23 the verified J>=15,H>=72,
a<=38 give the common factor bound 3^117/2^170>2; all 23 full
log(c_i/2) intervals independently have positive lower endpoints.
Thus the induction supplies all 25 incoming lower bounds, including
L_0=1 and L_24. It asserts nothing about C_25>=1; in fact the full
product is exp(-Lambda)<1 and remains in the closing denominator.

Every reciprocal, their complete sum, Q and the separate final term
kappa/L_24 are reconstructed. Their exact R_C is (3), strictly between
20011074610 and 20011074611, hence below U=21000000000. The original
U=20000000000 still fails. The recurrence e_0=1,
e_k=24e_(k-1)/k checks all 41 exponential terms through degree40;
their positive sum exceeds 26462988572>U. Positive omitted terms make
the inequality to exp(24) strict. All of (4) now holds with C's final
denominator, independently of L095 or H's different final cap term.

**Full analytic evidence and signs.** Successive rational powers
regenerate every one of the 300 original logarithm terms, all three
remainder bounds, both Lambda endpoints and all amplified errors.
The arguments 2,3,11/4 have series parameters 1/3,1/2,7/15 in (0,1);
the assessed remainder after 100 terms starts with exponent201.
The three outward constants ell,u,v have their claimed strict signs.
Every complete original analytic interval is checked, not merely its
rounded display or a stored pass flag.

A second evaluation uses 128 terms at 2,3/2,11/8, with parameters
1/3,1/5,3/19. The positive-real identities log3=log2+log(3/2) and
log(11/4)=log2+log(11/8) give

\[
\Lambda=(N-K)\log2-K\log(3/2),
\quad
E=24+(k_{24}-430963866+1)\log2
       +k_{24}\log(3/2)+\log(11/8).
\]

The fresh intervals lie strictly inside the original Lambda and E
intervals. Likewise all 23 factor intervals from this decomposition
lie inside their original intervals and have positive lower endpoints.
Signs select the correct endpoints even for negative coefficients.
This is a second application of the already assessed series, not a new
analytic input. The exact incoming values k_24=271907887,
d_24(2)=306970750 retain all extra36 row23 halvings. The outgoing
J_24=30998279 gives the positive negative-log2 coefficient430963866.
Both evaluations verify (4)'s complete error bounds, including v:
649476133/10^12<F-E<649476134/10^12<1/1000. Direct rational
evaluation gives exactly F=-4396220984253/250000000000<-17.58.
E is an upper expression for the actual margin, not an enclosure of
that margin; the strict implication comes from L077 (11)–(12).

**Closed interval and scope.** With all (3)–(5) premises matched,
L077 puts the actual own-input row24 margin strictly below F at t=2.
Its formula (10) has positive coefficients and x=2^(-18t): n_24,
and hence its J margin, strictly decreases with t. The full product
keeps both changing tails, so this applies through t=B, where a_24=2.
The same outgoing row24 and its own input are tested throughout;
a strictly negative margin contradicts the non-strict J guard. This
is a quantified implication, not extrapolation from sampled parameters.

No minimum/seed, H guard, guard feasibility, integrality, parity or
valuation realization, early-support/order exhaustion or actual-word
premise has entered. Attempt032, both d0 witnesses and unfinished work
are preserved. The full selected audit summary, cap, failure and mismatch
records were inspected; the verifier processes every original field and
complete analytic operand. No mathematical statement or dependency has
changed, so DAG.md and PROOF.md are unchanged; this canonical audit
supersedes their older pending-audit prose for L096. Survivor assembly,
early-support/order reduction, actual-word transfer and universal eventual
descent remain unresolved. Full matching Mathlib coverage remains unchecked.

## Mathlib

Full matching Mathlib coverage for this finite d34 cutoff has not been
checked. Supporting rational/log/exp and affine results would not supply
the table certificate or a matching theorem. The precise formal affine
citation and positive-real analytic coverage above suffice for this
informal specialization; no formal verification or absence claim is made.
