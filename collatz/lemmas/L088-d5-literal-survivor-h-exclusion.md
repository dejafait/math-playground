# L088 — d=5 literal survivor roots fail their own-input H guard

## Hypotheses

Take L055's 25 indexed pairs in literal order, changing only H_0=35
and H_24=32670626. Set B=9250245 and kappa=23/11. Fix t in {0,1},
put b_0=...=b_22=0, b_23=t, b_24=B-t and a_i=2+18b_i.
Consider real s_0,...,s_25 satisfying s_25=s_0 and all 25 endpoints

\[
s_{i+1}=2^{-a_i}\left((27/16)^{J_i}(3/2)^{H_i}s_i
                 -(12/11)(3/2)^{H_i}-1\right)+\kappa.
\tag{1}
\]

No J guard, H guard, lower-domain condition, minimum, seed,
integer-junction, parity, residue, exact-valuation, primitive-count or
actual-word premise is assumed. Logarithms below are natural.

## Conclusion

For each specified t there is exactly one real endpoint tuple. It is
positive rational, every n_i=s_i-kappa is greater than 47, and

\[
\log s_{18}+J_{18}\log(27/16)-H_{18}\log2
<-\frac{81550766911}{50000000000}<0.
\tag{2}
\]

Thus neither endpoint root satisfies its own outgoing row18 strict H
guard, whose required margin is positive. Neither is a full L051
real-system witness. This does not classify any other allocation or
order, nor establish an actual-word exclusion or universal descent.

This is RESEARCH/REPRODUCTION under the prior SPECIALIZE assessment
`drafts/literature/2026-10-20-d5-literal-survivor-h-test.md`.
The progress is a local fixed-root applicability result, using existing
audited data and specializing L083's cap/margin proof without its
unavailable all-order reduction. It is not a new mechanism beyond the
sources checked. The separate critical audit below found no defect.

## Proof

### Independent endpoint hypotheses

Use L077's independent endpoint assertion under its (3), rather than
L083's full theorem or C077a. The table has r=25,p=23,q=24, strictly
increasing J_i>=8 and H_i>=3. The two allocations in (1) are precisely
L077's last-pair allocations. L084 (2) and its completed all-member
audit give the unchanged totals and certified inequalities

\[
K=397573379,\quad N=630138897,\quad
0<\lambda_-:=10584/10^{14}<\Lambda=N\log2-K\log3
<\lambda_+:=10585/10^{14}<1.
\tag{3}
\]

The independent C/H section of L084 proves eta_24>=eta_0>2, with
eta_i=kappa-(16/27)^{J_i}(12/11+(2/3)^{H_i}). The same audited
data give 2(1-lambda_+)/lambda_+=39999999995766/2117>47.
Hence L077 (3) holds with e=2, without any O/S test. Its endpoint
assertion is independent of its J-guard hypothesis and boundary tests:
L077 (7)–(10) give the unique real cyclic root, rational with n_i>47.
In particular all logarithms used below have positive arguments.

Write c_i(t)=3^{3J_i+H_i}/2^{4J_i+H_i+a_i(t)},
C_i(t)=product_{j<i} c_j(t), C_0=1. Import the already specialized
L077 endpoint identities

\[
D=\exp(\Lambda)-1>\Lambda>\lambda_-,\qquad
S(t)=\sum_{j=0}^{24}\eta_j/C_j(t),\qquad
n_i=C_i(t)\left(S(t)/D+\sum_{j<i}\eta_j/C_j(t)\right),
\quad 0<\eta_j<\kappa.
\tag{4}
\]

The full product C_25=exp(-Lambda) includes the compensating closing
tail. At t=0 the two final tails are 2,166504412; at t=1 they are
20,166504394. Both lists have total tail 166504460 and denominator
exponent N in (3). No closing prefix is assumed at least 1.

### Restricted cap proof with every premise matched

Specialize only L083 (6)–(8), before its separate C077a reduction.
Here t is fixed in advance, so no reduction is needed to establish
0<=t<=m=1. Its endpoint formulas and eta bounds are (4), independently
licensed above. Use L084's independent H data, not C's t=2 data:

\[
w=10^8(2/3)^4=1600000000/81,\quad L_0=1,\quad
L_i=w2^{i-1}\ (1\le i\le24),\qquad L_*:=\min_i L_i=1.
\tag{5}
\]

L084 (5) and its complete C/H audit certify C_i(1)>=L_i for all
incoming indices 0 through 24. In detail row0 has c_0=3^{59}/2^{69}>w;
each row1 through row23 has multiplier greater than 2 at the H
package's actual tails, including row23's tail 20. The unchanged
pairs satisfy J>=15,H>=72, so the audited common lower comparison
3^{117}/2^{170}>2 applies. Multiplication proves every incoming
bound in (5). The compensating row24 tail stays in closure.
By L077's prefix identities, C_i(t)=C_i(0) for i<=23 and
C_24(t)=C_24(0)2^{-18t}; therefore C_i(t)>=C_i(1)>=L_i for both
specified t. This does not assume growth of either varying row.

The complete finite reciprocal sum, rather than an infinite surrogate,
and L084's independently audited d=5 H cap are

\[
\sum_{i=0}^{24}1/L_i
=1+(2/w)(1-2^{-24})=\frac{2684354831790883}{2684354560000000},
\quad Q:=\kappa\sum_{i=0}^{24}1/L_i
=\frac{61740161131190309}{29527900160000000},
\]
\[
R_H:=Q/\lambda_-+Q+\kappa/L_*
=\frac{771752014303243320582804778807}{39065411911680000000}
<20000000000<\exp(24).
\tag{6}
\]

The last analytic comparison is imported from L084's audited positive
degree-40 exponential lower sum. Its completed all-member audit covers
the d=5 cap; L084's displayed (7), limited to d<=4, is not invoked.
Every L_i>=1 and the actual minimum is attained at i=0. L_24 is
not substituted for L_* in this H bound.

For completeness, the precise restricted implication needed from
L083 follows directly from these matched premises. Equations (4)–(6)
give 0<S(t)<Q and every proper partial sum in (4) is less than Q.
Consequently at each incoming index

\[
0<\frac{s_i}{C_i(t)}
=\frac{S(t)}D+\sum_{j<i}\frac{\eta_j}{C_j(t)}
                    +\frac{\kappa}{C_i(t)}
<Q/\lambda_-+Q+\kappa/L_*<\exp(24).
\tag{7}
\]

Thus log s_i<24+log C_i(t). The strict sign follows already from
eta_j<kappa and D>lambda_-; no J/H guard, O/S datum, minimum or seed
enters this argument. This verifies why the earlier L083 proof case,
unlike that lemma's full theorem, is available here.

### Own-input row18 margin and exponent directions

Put A_i=sum_{j<i}(3J_j+H_j) and
D_i^0=sum_{j<i}(4J_j+H_j+2). Only incoming index 24 includes
row23's extra tail: D_i(t)=D_i^0 for i<=23 and
D_24(t)=D_24^0+18t>=D_24^0. Hence the smallest denominator
exponents are those at t=0, whereas the incoming lower bounds in
(5) used t=1. This matches both distinct comparisons in L083 (9).
Its coefficients are positive, so the audited analytic directions

\[
0<\ell:=693147180559/10^{12}<\log2,\qquad
\log3<u:=1098612288669/10^{12}
\]

give, using (7) at the row's own input,

\[
\log s_i+J_i\log(27/16)-H_i\log2
<24+(A_i+3J_i)u-(D_i^0+4J_i+H_i)\ell.
\tag{8}
\]

At row18 the unchanged pair is J_18=693015,H_18=3295208.
L084 (9) and its audited prefix sums, decreasing both incoming
exponents by 4 from d=1, give A_18=6078919,D_18^0=6862836.
Neither exponent depends on t here. Substitution in (8) is exactly

\[
24+8157964u-12930104\ell
=-\frac{81550766911}{50000000000}<0.
\tag{9}
\]

This proves (2) at both specified roots. One failed necessary strict
H guard suffices, irrespective of the other guards' verdicts.

### Sources, checks and limits

The formal affine input, already specialized in L077, is
Halbeisen–Hungerbuehler, *Optimal bounds for the length of rational
Collatz cycles*, Acta Arithmetica 78 (1997), 227–239,
DOI 10.4064/aa-78-3-227-239,
[section 2, equations (2)–(4), Lemma 2, pp. 228–229](https://www.math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
Integer rows define finite nonempty formal words; positive Lambda in
(3) supplies the nonzero fixed-point denominator. Import only formal
real affine composition, with no parity-realization converse. The
positive-real log/exp inputs are the assessed
[DLMF 4.5.1](https://dlmf.nist.gov/4.5.E1),
[4.6.4](https://dlmf.nist.gov/4.6.E4) and
[4.2.19](https://dlmf.nist.gov/4.2.E19).
Their bounds and amplified errors are imported from audited L084;
general coding and analytic bounds are not reproved. The only proof
specialization is removal of the unnecessary reduction for these two
roots specified in advance.

Exact rational applicability arithmetic, all 25 changed pairs, both
complete tail lists, full reciprocal inputs, operands and differences
for 19 successful checks are saved in
`scripts/postspell-word-count/d5-literal-survivor-h-applicability-certificate.json`.
This checks (3)'s totals and the finite arithmetic (5), (6), (9), not
an independent re-audit of the imported analytic/all-factor evidence.
The written argument (4)–(9) supplies the strict mathematical bound;
neither a certificate preview nor a stored success flag is its proof.

The d=5 failed S datum and Attempt 032 remain intact. Neither the full
C077a conjunction nor L083's all-order conclusion is invoked. L086
and L087 are downstream motivation only and are not assembled here.
The d=1 L081/L082 exclusions are different roots, not premises for
this verdict. Both original d=0 witnesses remain valid. Order reduction,
other allocations, actual-word transfer and universal eventual descent
remain unresolved by this result.

### Independent critical audit — 2026-10-20, step 357

The prior SPECIALIZE assessment
`drafts/literature/2026-10-20-d5-literal-survivor-h-critical-audit.md`
licenses this RESEARCH/REPRODUCTION proof audit. No defect was found
in the stated two-root scope. This establishes audited reliability of
the existing local input, not another exclusion or a new mechanism
beyond the cited sources. No allocation/order assembly is performed.

**Independent endpoint applicability.** The separately transcribed table
matches all 25 canonical L055 pairs before exactly the two H changes.
Its J values are strictly increasing and at least 8; every H is at
least 3. Both full tail lists give K=397573379, N=630138897 and total
tail 166504460. Positive Lambda therefore makes the full multiplier
3^K/2^N less than one and the cyclic affine map have a unique real
fixed point. Subtracting kappa in (1) gives precisely
n_(i+1)=c_i(n_i+eta_i). Composing all 25 edges gives (4), including
the closing tail. All coefficients and eta_i are positive rationals.
The latter follow from J_i,H_i>0 and
(16/27)^J_i(12/11+(2/3)^H_i)<23/11.

The exact eta_0 computation gives eta_0>2. The verified comparisons
J_24>=J_0,H_24>=H_0 imply eta_24>=eta_0 because each subtracted
positive factor decreases in its corresponding exponent. Thus L077
(3) holds independently of its guard and boundary tests. For i<=23,
the incoming unchanged tail-2 prefixes are at least one, so (4)
gives n_i>=n_0>eta_0/D>2(1-lambda_+)/lambda_+>47. At input24,
L077 (10) instead gives n_24>eta_24/D>47; no growth of a varying
row or minimum location is assumed. Closure also covers input25.
This checks uniqueness, rationality and every positive log argument.

**Restricted cap and strict margin.** Only L083's early proof cases
(6)–(9) are specialized. Its full theorem requires the full O/S
conjunction, which fails here. Since t=0 or 1 is fixed in the hypotheses,
no C077a reduction is needed to place it in 0<=t<=1. The exact
row0 multiplier exceeds w=1600000000/81>1. Each incoming factor
at rows1–23 has J>=15,H>=72 and tail at most 20, so the weaker
tail-38 bound 3^117/2^170>2 applies. The audit also encloses each
actual factor's log(c_i/2) separately for both full allocations,
retaining its entire numerator and denominator exponents; every lower
endpoint is positive. Multiplication proves all 25 incoming lower
bounds, with L_0=1 and actual L_*=1. No assertion C_25>=1 is made.

All 25 reciprocal terms are reconstructed, giving exactly Q and R_H
in (6), with R_H<20000000000. This independently checks the d=5
cap rather than importing the d<=4 displayed bound of L084 (7).
The complete sum S(t) and every proper partial sum are strictly
below Q because eta_i<kappa. Together with D>lambda_- and
C_i>=L_i, this proves the strict normalized inequality (7) without
any J/H guard, minimum, seed or realization premise.

For inputs0–23 the denominator prefix is independent of t; input24
has D_24(t)=D_24(0)+18t. Therefore t=1 gives the lower incoming
prefixes, while t=0 gives the larger H upper expression. These
directions are different and both are needed. The audit checks all
incoming exponents in both lists, the tail pairs
(2,166504412) and (20,166504394), and both closing exponents N.
Row18's own pair is (693015,3295208), with incoming exponents
(6078919,6862836). Thus its coefficients are exactly
P=8157964,R=12930104, both positive, and (9) follows with the
stated strict negative bound. The H guard requires a positive margin;
one failure suffices, without a verdict on the other guards.

**Complete finite evidence and analytic errors.** Run
`python3 scripts/postspell-word-count/audit_d5_survivor_h.py`.
The script independently reconstructs every mathematical field of the
applicability certificate, including all 19 named comparisons and their
operands, differences and verdicts. It imports or executes no constructor
or family-audit script. All 362 leaf comparisons and 522 additional
checks pass with zero mismatches; these counts include bookkeeping and
are not counts of distinct mathematical claims. Full evidence is saved
in `scripts/postspell-word-count/d5-literal-survivor-h-audit-certificate.json`.
The earlier applicability certificate is preserved unchanged.

Using the assessed positive-real remainder formula cited above, the
audit independently regenerates all 100 terms for each of log2 and
log3, with z=1/3 and 1/2 and positive upper remainder
2z^201/[201(1-z^2)]. Positive omitted terms give strict lower bounds.
If these intervals are (l2,h2) and (l3,h3), the Lambda enclosure is
(N*l2-K*h3,N*h2-K*l3); both amplified errors are retained, and
its endpoints lie strictly between lambda_- and lambda_+.
The ell<l2 and h3<u comparisons also pass. The independently
regenerated degree-40 positive exponential sum is
202750314819830504045671593478515759301/7661655986496068058455078125,
strictly above 20000000000 and strictly below exp(24).

For the row18 rounding, the excess of P*u-R*ell over
P*log3-R*log2 lies strictly between
P*(u-h3)+R*(l2-ell) and P*(u-l3)+R*(h2-ell).
Both exact endpoints and their positive sign/order are checked and
stored. Thus the strict negative bound is an outward upper bound,
not a numerical approximation to the root or an unamplified log error.
The complete selected Lambda/error intervals, exponential sum and
failure list were inspected; previews and stored success flags do
not replace this reconstruction or the written applicability argument.

Attempt 032 still stops the full conjunction at d=5. L081/L082
concern different d=1 roots; both original d=0 witnesses are unaffected.
No L086/L087 assembly, cyclic-order reduction or actual-word transfer
has been imported into this audit. The direct inputs remain exactly
L055,L077,L083,L084. The argument and DAG are unchanged, so PROOF.md
and DAG.md are not edited for audit status alone; this canonical audit
supersedes their earlier pending-audit wording for L088. Universal
eventual descent remains unresolved, with no complete candidate.

## Mathlib

Full matching coverage for this fixed-root applicability result has
not been checked. Supporting affine, finite-sum and log/exp facts do
not constitute a matching theorem. Unknown coverage is not absence;
no Lean verification is claimed.
