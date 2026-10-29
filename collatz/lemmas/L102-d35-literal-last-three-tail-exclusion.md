# L102 — Literal d35 last-three-tail exclusion

## Hypotheses

Take all 25 indexed pairs from L055, changing only H_0=5 and
H_24=32670656. Use literal indexed order and set B=9250245,
kappa=23/11. Let u,v be integers with u>=1,v>=0,u+v<=B and set

\[
a_i=2\ (0\le i\le21),\quad a_{22}=2+18u,\quad
a_{23}=2+18v,\quad a_{24}=2+18(B-u-v).
\tag{1}
\]

Define G_i=(27/16)^{J_i}(3/2)^{H_i} and
Q_i=(12/11)(3/2)^{H_i}+1. Suppose real s_0,...,s_25 satisfy
s_25=s_0, s_i>=540/11 for 0<=i<25, and all endpoints and
non-strict own-input J guards

\[
s_{i+1}=2^{-a_i}(G_i s_i-Q_i)+\kappa,\qquad
4J_i\log2\le\log s_i+\log(11/4)\quad(0\le i<25).
\tag{2}
\]

Logarithms are natural. The i=24 endpoint is required even when
a_24=2. No H guard, minimum, seed, junction integrality, parity,
valuation, realization or primitive-count premise is imposed.

## Conclusion

There is no such real tuple on the whole stated integer parameter
domain. More precisely, any hypothetical tuple would satisfy

\[
4J_{23}\log2-\log s_{23}-\log(11/4)
>\frac{6362519491371}{250000000000}>25>0,
\tag{3}
\]

contradicting its own-input J guard. Therefore the approved system,
which additionally requires every strict own-input H guard
H_i log2<log s_i+J_i log(27/16), is also infeasible.

This is local RESEARCH/REPRODUCTION under the prior SPECIALIZE
assessment `drafts/literature/2026-10-25-d35-last-three-tail-feasibility.md`.
It specializes inspected affine/analytic machinery, with no originality
claim beyond checked sources. Construction and exact data checks are
complete; the separate critical audit below found no defect. Other early
supports, orders, entry, unrestricted cycles, divergence and universal
eventual descent remain open. No complete Collatz candidate is claimed.

## Proof

### Imported data and precise source scope

Only L055's indexed table is imported, not its original-table witness,
minimum or seed. The opposite H changes preserve sum H=199390205,
sum J=66061058. The tails in (1) have sum 50+18B=166504460, so

\[
K=\sum_i(3J_i+H_i)=397573379,\quad
N=\sum_i(4J_i+H_i+a_i)=630138897.
\tag{4}
\]

L084 (2) and its completed independent all-member audit supply,
at d=35 and independently of the failed full O/S/C conjunction,

\[
0<\lambda:=10584/10^{14}<\Lambda:=N\log2-K\log3,
\quad \ell:=693147180559/10^{12}<\log2,
\]
\[
\log3<q:=1098612288669/10^{12},\qquad
\log(11/4)<w:=1011600911679/10^{12}.
\tag{5}
\]

The cap argument is the independently applicable proof (6)–(7) of
L076, not its conclusion under failed sufficient tests. Its required
data and its applicability at H_0=5 are justified below. L099's d34
comparison is a method precedent only; no d34 assertion is applied.
C101a/L100/L101 fix a22=2 and are not inputs here. Attempt032's
row0 tail20 and other full-package failures remain unchanged. No
failed conjunction supplies any implication.

The formal affine source is Halbeisen–Hungerbuehler, *Optimal bounds
for the length of rational Collatz cycles*, Acta Arithmetica 78 (1997),
227–239, DOI 10.4064/aa-78-3-227-239,
[section2 equations(2)–(4), Lemma2, pp.228–229](https://www.math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
Only finite real affine algebra is used, without integer realization.
The analytic inputs are [NIST DLMF4.5.1](https://dlmf.nist.gov/4.5.E1),
log(1+x)<x for x>0, and the audited positive-real applications of
[4.6.4](https://dlmf.nist.gov/4.6.E4) and
[4.2.19](https://dlmf.nist.gov/4.2.E19) at 2,3,11/4 and 24.
The ready assessment inspected the primary hypotheses and needed
proof cases; the general coding and series results need no reproof.
The algebra below verifies only the changed-support applicability.

### Guard-conditioned cyclic cap at d35

Put n_i=s_i-kappa>=47 and

\[
\eta_i=\kappa-(16/27)^{J_i}\bigl(12/11+(2/3)^{H_i}\bigr),
\qquad c_i=2^{-a_i}G_i.
\]

All J_i>=2,H_i>=3. Each subtracted power lies in (0,1), and
the positive subtracted sum is less than 12/11+1=kappa. Thus
0<eta_i<kappa. Direct substitution in (2) gives
n_(i+1)=c_i(n_i+eta_i), with every term positive.
Multiply all 25 ratios, using n_25=n_0 and (4); taking logarithms
gives exactly

\[
\Lambda=\sum_{i=0}^{24}\log(1+\eta_i/n_i).
\tag{6}
\]

For i>=1 the own-input J guard implies
n_i>=(4*2^{4J_i}-23)/11. The strictly increasing indexed J data
have J_1=15, so the sum of those 24 summands is strictly below

\[
E=\frac{23\cdot24}{4\cdot2^{60}-23}
=\frac{552}{4611686018427387881}.
\]

Here log(1+x)<x is applied only at positive x, and eta_i<kappa.
The remaining summand is strictly below kappa/n_0. Consequently
lambda<Lambda<kappa/n_0+E. The exact data give lambda-E>0 and

\[
s_0<R:=\frac{\kappa}{\lambda-E}+\kappa
=\frac{1325859730438202850942226985830949}{67113790726173775832193}
<U:=20000000000.
\tag{7}
\]

Every inversion uses positive quantities. The imported positive
exponential partial sum, also recomputed in the certificate, is

\[
U<\sum_{k=0}^{40}\frac{24^k}{k!}
=\frac{202750314819830504045671593478515759301}
       {7661655986496068058455078125}<e^{24}.
\tag{8}
\]

Thus log s_0<24. This cap uses every actual endpoint and tail through
(6); neither v nor B-u-v is discarded. It imposes no minimum or
growth premise on later rows. H_0=5>=3 suffices for its positivity.

### Fixed tail2 prefix and the distinct recipient offset

For each preceding row i=0,...,21, H_i>=5. Its tail2 affine offset is

\[
\kappa-Q_i/4=81/44-(3/11)(3/2)^{H_i}
\le81/44-(3/11)(3/2)^5=-81/352<0.
\tag{9}
\]

This proves the needed sign at row0 without imposing its failed
tail20 offset test. At the recipient row22, H_22=41522114>=72,
so monotonicity of the positive integer power gives instead

\[
Q_{22}\ge\frac{12}{11}(3/2)^{72}+1
=\frac{67585198634830509743348335148655587}
       {12986507827891524337664}
>\frac{24117248}{11}=\kappa2^{20}.
\tag{10}
\]

At each actual input,
G_i s_i-Q_i=G_i(n_i+eta_i)>0. As u>=1 is integral, a22>=20,
and increasing that tail decreases its endpoint at that input.
Equations (9)–(10) now give

\[
s_{i+1}<(G_i/4)s_i\quad(0\le i\le21),\qquad
s_{23}\le2^{-20}(G_{22}s_{22}-Q_{22})+\kappa
<2^{-20}G_{22}s_{22}.
\tag{11}
\]

Both subtractions remain inside tail division and kappa outside until
these offset signs are established. All actual junctions and the
multipliers being combined are positive. The comparison endpoint
need not be an auxiliary trajectory.

### Exact next-input rejection and full-domain coverage

The complete tail2 prefix through row22 has exponents

\[
A=\sum_{i=0}^{22}(3J_i+H_i)=144318677,\qquad
D=\sum_{i=0}^{22}(4J_i+H_i+2)=162928754.
\tag{12}
\]

Multiplying (11), then using (7)–(8), yields
log s_23<24+A log3-(D+18)log2. The extra 18 occurs only at
the recipient; larger u can only strengthen this upper comparison.
The next indexed J is J_23=16452748. Hence, using (5) with the
positive coefficients A and C:=D+18+4J_23=228739764,

\[
\begin{split}
4J_{23}\log2-\log s_{23}-\log(11/4)
&>C\log2-24-\log(11/4)-A\log3\\
&>C\ell-24-w-Aq\\
&=\frac{25450077965484}{10^{12}}
=\frac{6362519491371}{250000000000}>25.
\end{split}
\tag{13}
\]

The grid replacements retain all amplified errors: the exact
expression exceeds the grid expression by
C(log2-ell)+A(q-log3)+(w-log(11/4))>0. Thus rounding cannot
reverse the rejection. The required non-strict J guard at precisely
s_23 would make the left side <=0, a contradiction.

No enumeration or monotonicity in v is assumed. For every stated
u,v, all tails are at least2, their full sum is (4), the prefix tails
are2 and the recipient tail is at least20. Those facts establish
(6)–(13) uniformly. The boundary v=0 merely sets a23=2; the
boundary u+v=B sets the closing a24=2, whose equation remains in
(6). Their intersection u=B,v=0 is also covered. No H inequality
was used, so adjoining every strict own-input H guard cannot restore
feasibility. This is the exact approved target's exclusion, without
extending to other early supports or changing the literal cut.

### Finite evidence and limitations

Run `python3 scripts/postspell-word-count/certify_d35_last_three.py`.
The full certificate is
`scripts/postspell-word-count/d35-last-three-certificate.json`.
It preserves the canonical table/hash, the changed table, all exact cap
operands, all 41 exponential terms, all 22 preceding offset enclosures,
the recipient bound, full prefix/margin operands and all 196 comparison
records. There are zero failed comparisons and zero parameter samples.
The load-bearing cap constants, recipient comparison, prefix exponents
and margin were inspected in full. The script also matches these data
to the independent subsets of L084's audited d35 table, while retaining
the failed row0 tail20 datum as a failure of the old sufficient package.
The quantified proof above supplies full-domain coverage; a stored pass
flag or a numerical preview alone would not do so.

The construction evidence is distinct from the independent audit below.
No actual integer word is inferred from a real tuple, no repetition is excluded
by assumption, and no order/support exhaustion or universal descent
claim follows. Both d0 witnesses and unfinished work remain preserved.

### Independent critical audit — 2026-10-25, step470

This RESEARCH/REPRODUCTION audit used the unchanged prior SPECIALIZE
assessment `drafts/literature/2026-10-25-d35-last-three-critical-audit.md`.
It found no defect in the stated exclusion or its exact margin. This
secures an existing restricted input; it establishes no larger exclusion,
new source theorem, actual-word application or Collatz resolution.

**Independent finite reconstruction.** Run
`python3 scripts/postspell-word-count/audit_d35_last_three.py`.
The script neither imports nor executes the construction program. A
separate transcription of all 25 pairs is matched against L055's actual
table, then only H0 and H24 are changed by -35 and +35. It reconstructs
the sums, all cap constants, all 41 exponential terms, all 23 offset
records (22 prefix rows and the recipient), the recipient comparison
and the complete row23 margin. Every mathematical field in the original
certificate is compared; all 196 named comparisons are rebuilt with
both operands, relation, difference and verdict. Exact name/key sets
reject missing or duplicate comparisons. L084's selected d35 data and
both source hashes are also checked, without relying on its failed
full-package verdict. The original certificate is left unchanged.

The complete independent evidence is
`scripts/postspell-word-count/d35-last-three-audit-certificate.json`:
196 reconstructed comparisons, 1864 recursive leaf comparisons and
23 additional arithmetic/report checks, with zero mismatches or failed
checks and no parameter sampling. These counts include metadata and
repeated values; they are not counts of distinct mathematical claims.

**Analytic hypotheses and outward errors.** The assessed positive-real
logarithm series is independently evaluated with 120 terms for
2,3,11/4,3/2, with z respectively 1/3,1/2,7/15,1/5. Its remainder
is bounded above by 2z^241/[241(1-z^2)]; the positive omitted terms
give strict lower bounds. All four arguments and z values satisfy
the imported series hypotheses. The complete terms, remainders and
rational endpoints are saved. If [l_x,u_x] denotes one such strict
enclosure, the audit verifies

\[
\lambda<N l_2-K u_3<\Lambda<N u_2-K l_3<10585/10^{14}.
\]

Independently evaluating
(N-K)log2-K log(3/2), with N-K=232565518>0, places Lambda
between the same grid bounds. The audit also checks ell<l_2,
u_3<q and u_(11/4)<w. Thus the exact margin in (13) exceeds its
printed grid value by a quantity bounded below by

\[
C(l_2-\ell)+A(q-u_3)+(w-u_{11/4})>0.
\]

Every coefficient is retained before rational comparison. No decimal
rounding or stored pass flag establishes a sign. The independent
exponential recurrence t0=1, t_k=24*t_(k-1)/k reproduces (8);
positive omitted terms justify its strict relation to exp24. These
are uses of the cited analytic inputs, not new general series proofs.

**Cap independence and full-domain reasoning.** The shift gives
n_i>=47, and G_i*eta_i=kappa*G_i-Q_i exactly. Positivity of both
subtracted powers yields 0<eta_i<kappa at every row, including
H0=5 and the closing row. Hence multiplication and logarithms in
(6) are legitimate. The full product contains all 25 endpoints and
all tails; summing them gives (4) even when either later tail equals2.
For i>=1 the J guard gives n_i>=(4*2^(4J_i)-23)/11, with J_i>=15.
This alone gives E; no relative height, minimum, H guard or support
offset is used. The positive residual lambda-E permits the inversion
in (7), whose exact printed R and exponential threshold are verified.

The preceding rows0--21 all have tail2 and H>=5, so (9), including
the exact row0 offset -81/352, supplies precisely their needed signs.
Row0's tail20 offset is positive, as independently retained in the
certificate; it is never used as a negative offset. Only row22 needs
(10), which passes with its actual H>=72. At its actual input,
G22*s22-Q22>0, so a22>=20 gives the non-strict comparison to
tail20; the negative offset then makes (11) strict. No auxiliary
trajectory or later-tail monotonicity is asserted. The positive
multipliers give A=144318677, D=162928754 and C=228739764 at
precisely the next input s23. Its non-strict own-input J guard is
therefore incompatible with (13).

For every integer u>=1,v>=0,u+v<=B, the preceding tails stay2,
the recipient tail is at least20, all tails are at least2, and their
sum stays 50+18B. These are the only allocation facts used. In
particular v=0 retains the row23 equation at tail2; u+v=B retains
the closing row24 equation at tail2; and their intersection u=B,v=0
retains both. Thus the audit verifies the universal implication rather
than a collection of sampled allocations. Adjoining strict H guards
cannot restore an already excluded J-only tuple.

The direct mathematical inputs remain L055's table, L076's separately
applicable cap/first-recipient proof and L084's independent analytic/data
enclosures. No DAG edge or mathematical assembly changes. This verdict
supersedes the older pending-audit wording for L102 in the overview;
PROOF.md is not edited for audit status alone. Attempt032, both d0
witnesses and unfinished work are preserved. Other recipients/orders,
entry, actual-word transfer, unrestricted cycles and divergence remain
unresolved; full matching Mathlib coverage remains unchecked.

## Mathlib

Full matching coverage is unchecked, not known absent. Supporting
affine, logarithm, exponential and rational arithmetic results would
not themselves be a matching theorem for this restricted system. No
Lean verification is claimed.
