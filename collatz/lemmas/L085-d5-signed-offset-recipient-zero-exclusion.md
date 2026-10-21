# L085 — d=5 literal recipient-zero exclusion with the signed offset

## Hypotheses

Take L055's 25 indexed pairs, changing only H_0=35 and
H_24=32670626. In particular J_0=8,J_1=15, and every J is
unchanged. Let b_i be nonnegative integers with sum b_i=9250245,
and put a_i=2+18b_i. Use literal indexed order throughout. Set

\[
\kappa=23/11,\quad G_i=(27/16)^{J_i}(3/2)^{H_i},\quad
Q_i=(12/11)(3/2)^{H_i}+1.
\]

Suppose real junctions s_0,...,s_25 satisfy s_25=s_0,
s_i>=540/11 and, for every 0<=i<25,

\[
s_{i+1}=2^{-a_i}(G_i s_i-Q_i)+\kappa,\qquad
4J_i\log2\le\log s_i+\log(11/4).
\tag{1}
\]

These are only C077a's endpoint/domain/non-strict own-input J
conditions, including closure. No conclusion of C077a is assumed.
No minimum, seed, H guard, integer junction, parity, valuation,
actual-word or primitive-count premise is imposed.

## Conclusion

Every such tuple has b_0=0. More precisely, b_0>=1 would force
s_1<2000000000000, whereas its own-input J guard requires
s_1>=4611686018427387904/11>400000000000000000.

This is a local REPRODUCTION under the prior SPECIALIZE assessment
`drafts/literature/2026-10-19-d5-signed-offset-recipient-zero.md`.
It extends the usable comparison at this one recipient beyond L084's
failed negative-offset test, without changing that test. It gives no
other-recipient or order reduction, last-pair conclusion, feasibility,
integer/actual-cycle exclusion or universal eventual descent. The separate
critical audit below found no defect within this precise scope; no
originality beyond the sources checked is asserted.

## Proof

### Imported inputs and applicability

The opposite changes in H leave the totals in L055 unchanged:

\[
K=\sum_i(3J_i+H_i)=397573379,\quad
N=\sum_i(4J_i+H_i)+50+18\cdot9250245=630138897.
\]

The full product retains every allocated tail, including row24's
closing tail. Import the certified analytic enclosure L055 (2), also
independently checked for this table in L084 (2):

\[
0<\lambda:=10584/10^{14}<\Lambda:=N\log2-K\log3
<10585/10^{14}.
\tag{2}
\]

Use only L076's audited guard-conditioned cap subargument, equations
(6)–(7), whose proof precedes and does not use its negative-offset
hypothesis. Do not apply L076's full support conclusion or C077a's
reduction. The following details check every condition needed for that
subargument here.

The formal affine composition is covered by Halbeisen–Hungerbuehler,
*Optimal bounds for the length of rational Collatz cycles*, Acta
Arithmetica 78 (1997), 227–239, DOI 10.4064/aa-78-3-227-239,
[section 2, equations (2)–(4), Lemma 2, pp. 228–229](https://www.math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
Only real finite-word algebra is used; no realization converse is
needed. The positive-real inequality log(1+x)<x for x>0 is
[DLMF 4.5.1](https://dlmf.nist.gov/4.5.E1). These are the precisely
assessed inputs reused from L076/L084, not new analytic assertions.

### Cap without the failed offset hypothesis

Put n_i=s_i-kappa>=47 and

\[
\eta_i=\kappa-\frac{12}{11}(16/27)^{J_i}
                    -(16/27)^{J_i}(2/3)^{H_i},\qquad
c_i=2^{-a_i}G_i.
\]

All J_i>=2 and H_i>=3. Each subtracted term is positive; their
sum is less than 12/11+1=kappa because both bases are in (0,1).
Hence 0<eta_i<kappa. Directly rewriting (1) gives
n_(i+1)=c_i(n_i+eta_i). All quantities are positive. Multiply all
25 ratios, using n_25=n_0 and prod c_i=3^K/2^N, then take logs:

\[
\Lambda=\sum_{i=0}^{24}\log(1+\eta_i/n_i).
\tag{3}
\]

The J guards and increasing J give, for every i>=1,

\[
n_i\ge\frac{4\cdot2^{4J_i}-23}{11}
\ge\frac{4\cdot2^{60}-23}{11}>0.
\]

Apply the cited logarithm inequality to every term of (3). With

\[
E=\frac{552}{4\cdot2^{60}-23}
  =\frac{552}{4611686018427387881},
\]

the last 24 terms sum to less than E, and the first is less than
kappa/n_0. Thus lambda<Lambda<kappa/n_0+E. Exact rational
arithmetic gives

\[
\lambda-E=
\frac{6101253702379434166563}{57646075230342348512500000000000}>0,
\]
\[
s_0<\frac{\kappa}{\lambda-E}+\kappa
=\frac{1325859730438202850942226985830949}{67113790726173775832193}
<U:=20000000000.
\tag{4}
\]

Every inversion has positive denominator. This bound uses all the
retained guards and endpoints, with no minimum location or assumption
on which later tails grow. It is uniform over the entire allocation
simplex.

### Full signed row-zero endpoint and strict row-one rejection

Assume b_0>=1. Its integrality implies a_0>=20. At the actual
input s_0, the pre-tail bracket is strictly positive:

\[
G_0s_0-Q_0=G_0(n_0+\eta_0)>0.
\]

Consequently increasing the tail can only decrease the endpoint at
this actual input. The tail-20 comparison map is strictly increasing
in its input, since its slope G_0/2^20 is positive. By (4),

\[
s_1\le 2^{-20}(G_0s_0-Q_0)+\kappa
<2^{-20}(G_0U-Q_0)+\kappa.
\tag{5}
\]

Here the full signed offset is positive and is retained exactly:

\[
G_0=3^{59}/2^{67},\quad
Q_0=150094729786279633/94489280512,
\]
\[
\kappa-2^{-20}Q_0
=57070853072763183/99079191802150912>0.
\tag{6}
\]

In particular Q_0<kappa*2^20, precisely L084's failed support
datum. It is not being repaired or assumed. Substitution into (5)
gives the complete rational bound

\[
s_1<
\frac{1517912568448975615643685444656909889}
     {831136500985057557610496}
<2000000000000.
\tag{7}
\]

Both comparisons in (4) and (7) follow by cross-multiplying positive
integer denominators. On the other hand row1's own guard in (1),
with J_1=15, exponentiates to

\[
s_1\ge\frac4{11}2^{60}
=\frac{4611686018427387904}{11}
>400000000000000000.
\tag{8}
\]

Equations (7)–(8) contradict each other strictly. Nonnegativity of
b_0 therefore gives b_0=0. The proof does not compare a newly
constructed trajectory or sample allocations; (5) compares at the
actual input of an assumed solution, while (3) retains every remaining
allocation and closure.

### Exact finite verification and qualifications

Run `python3 scripts/postspell-word-count/certify_d5_signed_recipient_zero.py`.
The full evidence is
`scripts/postspell-word-count/d5-signed-recipient-zero-certificate.json`.
It stores the complete changed table, invariant totals, residual, cap,
positive signed offset, endpoint, threshold and every cross-multiplication
comparison. All 12 checks pass; the complete check records and selected
signed values were inspected. The analytic Lambda enclosure is explicitly
imported from L055/L084, not newly certified by this script. The written
proof supplies the quantified implication; the script verifies only its
finite rational arithmetic. This construction-time check is not an
independent critical audit.

L055/L065's original-table witnesses and Attempts 026–032 remain
unchanged. In particular Attempt 032 still correctly stops the old
sufficient test at d=4. This lemma addresses only literal recipient
zero at d=5 and leaves every other required reduction independent.

### Independent critical audit — 2026-10-19, step 345

The unchanged SPECIALIZE assessment
`drafts/literature/2026-10-19-d5-signed-recipient-zero-critical-audit.md`
licenses this RESEARCH/REPRODUCTION proof audit. No defect was found.
This establishes the existing result as an independently checked local
input; it adds no exclusion, stronger bound or progress beyond the
inspected source machinery. The construction certificate is unchanged.

**Cap independence and quantifiers.** All 25 pairs match L055 after
exactly the opposite H changes stated above. Their sums remain
sum J=66061058 and sum H=199390205. For every admitted allocation,
sum a=166504460, giving the same K,N in (2), including the closing
tail even when it equals 2. Subtracting kappa in each endpoint gives
the positive n recurrence used in (3); eta depends only on J,H and
lies in (0,kappa) for every row. Therefore all 25 positive ratios
telescope, with n_25=n_0, to exactly (3). No sampled root, growth
assumption or minimum location occurs here.

For every i=1,...,24, J_i>=J_1=15. Exponentiating that occurrence's
non-strict guard yields n_i>=(4*2^60-23)/11. The positive-real
hypothesis eta_i/n_i>0 matches the cited DLMF inequality, so the
sum of those 24 logarithms is strictly below E; the remaining term
is strictly below kappa/n_0. Positive lambda-E then gives (4),
with its strict sign preserved even if some guards hold at equality.
These steps use neither L076's offset test nor any conclusion of
C077a. L084's failed support datum therefore does not invalidate the
cap. L055's rational witness and its minimum are not invoked.

**Signed endpoint and own-input contradiction.** If b_0>=1, its integer
hypothesis gives a_0>=20. Positivity of G_0(n_0+eta_0) is established
at the actual input before replacing the tail. The comparison map has
positive slope, so s_0<U makes (5) strict even at a_0=20. Its offset
is the positive number in (6), not zero or a negative surrogate. Both
coordinate shifts remain present. The complete expression in (7) is
strictly below 2*10^12, whereas the outgoing row1 guard requires its
own input s_1>=2^62/11>4*10^17. Thus one retained necessary guard
fails strictly, independently of how the other budget entries are
distributed. No comparison trajectory or realization premise is needed.

**Independent arithmetic.** Run
`python3 scripts/postspell-word-count/audit_d5_signed_recipient_zero.py`.
The program neither imports nor executes the constructor. It separately
transcribes all 25 pairs and checks them against L055 and the complete
construction table; reconstructs every numerical field; and compares
all 12 original records, including operands, relation, difference and
verdict. Integer cross products independently determine every sign.
Separate shifted/unshifted endpoint evaluations agree. All 41 audit
checks pass, with zero failures; these count verification checks, not
distinct mathematical advances.

For an independent verification of the imported Lambda interval, the
program uses the already assessed [DLMF 4.6.4](https://dlmf.nist.gov/4.6.E4)
positive-real specialization. For t=2,3 and x=(t-1)/(t+1) in (0,1),
put P=2 sum_(m=0)^95 x^(2m+1)/(2m+1). The positive omitted terms
give P<log t; replacing their denominators by 193 bounds the tail
strictly above by 2x^193/[193(1-x^2)]. This is the same assessed
remainder bound used in the prior audits, not a new analytic result.
Opposite endpoints for N log2-K log3 give a full rational enclosure
inside the outward grid

\[
105843488/10^{18}<\Lambda<105843489/10^{18},
\]

which lies strictly between the two imported bounds in (2). All
amplified errors are retained. The full evidence is
`scripts/postspell-word-count/d5-signed-recipient-zero-audit-certificate.json`:
the source hash, complete table and numerical operands, all reconstructed
comparisons, all 192 logarithm terms, both remainders and the complete
Lambda interval. The complete comparison, operand, check and decisive
grid records were inspected; the program and symbolic remainder argument
verify the full analytic calculation rather than a decimal preview.

Attempt 032's failed offset test and both original-table witnesses remain
valid. Other recipients, arbitrary orders, last-pair analysis and integer
or actual-word applications remain unproved for this table by L085.
Universal eventual descent remains unresolved. The direct mathematical
inputs and argument are unchanged, so DAG.md and PROOF.md are unchanged;
this canonical audit supersedes their older pending-audit wording for L085.

## Mathlib

Full matching coverage is unchecked, not absent. Supporting real-log,
affine and rational-arithmetic facts do not by themselves formalize this
complete table specialization. No Lean proof is claimed.
