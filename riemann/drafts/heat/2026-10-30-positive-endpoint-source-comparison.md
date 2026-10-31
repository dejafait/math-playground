# Positive-endpoint inverse-gap source comparison

2026-10-30. Literature only; supplied overview/DAG read first. Existing
notebook changes preserved. No mathematical calculation, new theorem,
lemma write or script write. Main gap: actual-Xi all-degree mixed positivity.
The reviewed intermediate target was uniform integrability of the inverse
square separation of a finite-height pair above a possible positive collision.
Its possible use was a later actual-theta collision-exclusion test; no such
criterion or exclusion has been established here.

## Inspected primary source and applicability

Brad Rodgers and Terence Tao, *The De Bruijn–Newman constant is non-negative*,
[arXiv:1801.05914v3, 6 March 2020](https://arxiv.org/html/1801.05914v3).
Read Introduction (1)–(4), Section 1.2 standing hypothesis, Theorem 4.1
and proof reference, Lemma 4.2 statements and convergence/finite-Hamiltonian
proof, Proposition 5.1 and its Lemma 5.2 proof, Proposition 6.1 with its
complete cutoff argument. Section 7 definitions (62)–(69), Lemma 7.1 and
Theorem 7.2 statement were inspected; the whole proof of Theorem 7.2 was
not audited. No full manuscript audit is claimed.

Normalization is a necessary source comparison, not a new heat-flow result:
L019's displayed kernel satisfies K(2u)=4 Phi(u). Substitution in L058's
defining integral therefore identifies F(lambda,z)=8 H_(4lambda)(2z).
Thus source time t=4lambda and source zero coordinate x=2z. Positivity
of an endpoint and convergence of the proposed integral are unaffected
by this fixed positive scaling. This does not move a positive endpoint
into the source's nonpositive time interval.

The source assumes Lambda<0 throughout Sections 2 onward. Theorem 4.1
is stated on Lambda<t<=0 with principal-value motion and real simple
zeros. Its proof cites CSV Lemma 2.4 and Lemma 2.1 for continuity; the
older proof is not reproduced. Lemma 4.2(i) gives the gap equation;
its difference sum is absolutely convergent using (43)/(50).

Write E_jk=|x_j-x_k|^(-2) and H_jk=log(1/|x_j-x_k|), as in (57)/(58).
The load-bearing finite identity in Lemma 4.2(v) retains the environment:

    d/dt sum_(k,k' in K; k!=k') H_kk'
      = -4 sum_(k,k' in K; k!=k') E_kk'
        +2 sum_(j notin K; k,k' in K; k!=k')
             1/((x_j-x_k)(x_j-x_k')).

The proof cancels only the internal triple sum by antisymmetrization.
It does not cancel the displayed exterior sum. Lemma 4.2(ii) is a weak
cross-energy inequality, justified by finite cutoffs, symmetrization of
the two internal cases and the sign of the exterior case, then monotone
convergence. It is not a theorem controlling an endpoint collision.

Proposition 5.1 supplies a logarithmic inverse-gap bound on
[Lambda/2,0]. Its Lemma 5.2 uses a backward time interval staying above
Lambda; the constants are not asserted uniform as that margin vanishes.
The HTML has sign/prime typographical inconsistencies in this proof
(including a displayed min with Lambda/2 although Lambda<0); no corrected
endpoint theorem is inferred from them. The stated interval alone is
enough to distinguish the proposition from the requested target.

Proposition 6.1 bounds the integral of sum_(J<=j<k<=2J) E_jk from
Lambda/2 to 0 by J^2 times a power of log_+ J. Its proof chooses enlarged
index intervals by pigeonhole, integrates the finite identity above,
and explicitly bounds the Hamiltonian endpoint difference using
Proposition 5.1. Far exterior interactions use (52); near exterior
interactions are absorbed using Q_K'-Q_K <= J^(-0.1) Q_K. Accordingly,
an endpoint limit cannot be obtained by discarding cutoff errors or
by retaining only the sign of the internal energy. At a postulated
vanishing pair gap the lower-endpoint logarithm is precisely an
uncontrolled term. No rate of divergence, impossibility of integrability,
or extension to positive t is proved by this observation.

Theorem 7.2 improves a renormalized energy integral on [Lambda/4,0],
not an interval touching Lambda. Its potential is
V(r)=|r|^(-2)-1+2(|r|-1); each pair is scaled by the squared reference
spacing as in (63). Lemma 7.1 records the finite-interval correction;
(66)/(67) introduce spatial weights. These are not the formal infinite
unweighted energy. Neither renormalization nor spatial localization
states the missing time-endpoint uniformity. The theorem's full proof
was unnecessary for, and is not claimed in, this applicability rejection.

## Older essential source: exact identification, incomplete access

G. Csordas, W. Smith and R. S. Varga, *Lehmer pairs of zeros, the
de Bruijn–Newman constant Lambda, and the Riemann hypothesis*,
Constructive Approximation **10** (1994), 107–129,
[DOI 10.1007/BF01205170](https://doi.org/10.1007/BF01205170).
The reference is Rodgers–Tao [11], not the separate four-page proceedings
note *Lehmer pairs of zeros and the Riemann xi-function*.

Located [author-hosted scan](https://www.math.kent.edu/~varga/pub/paper_206.pdf)
and [author-uploaded mirror](https://www.researchgate.net/profile/Richard-Varga-3/publication/226697760_Lehmer_pairs_of_zeros_the_de_Bruijn-Newman_constant_L_and_the_Riemann_Hypothesis/links/558405c208aefa35fe329da7/Lehmer-pairs-of-zeros-the-de-Bruijn-Newman-constant-L-and-the-Riemann-Hypothesis.pdf).
Both open as 23-page PDFs with zero readable lines. Screenshot requests
return only image placeholders in this interface. The shell download
failed DNS resolution; no local PDF/text was produced. The publisher
PDF address redirects to the article landing page. No access controls,
credentials or paid access were used.

Queries included “Csordas Smith Varga 1994 Lehmer pairs theorem zeros
de Bruijn Newman pdf”, the exact title with Lemma 2.1, Lemma 2.4,
Corollary 1 and 2.11, and Csordas Lemma 2.2 coalescence.
Indexed primary excerpts locate Lemma 2.4 on p.115 and Lemma 2.5 on
p.116, suggesting that their dynamics use t>Lambda without t<=0.
The p.116 excerpt mentions the collision case in Lemma 2.2 and a
cross-energy rational bound whose denominator can vanish. These are
UNINSPECTED LEADS, not adequate primary proof coverage. In particular,
do not repeat the overbroad claim that CSV itself excludes positive
times. Its exact local collision cases, convergence proof and endpoint
dependence remain unread. Rodgers–Tao's simplicity citation also differs
from the numbered corollary shown in one indexed introductory excerpt;
resolve from complete primary pages before any import.

## Decision and remaining limits

New source-level negative evidence: the inspected integrated-energy proof
uses an endpoint gap/Hamiltonian bound with a time margin, so the direct
Rodgers–Tao citation fails the specified uniform-endpoint test. Essential
CSV coverage remains SOURCE_BLOCKED. No claim that the proposed bound
is false is justified. Park this direct application rather than repeating
access attempts. No lemma is approved and no novel mathematics is claimed.

L058/L018 and L019 were checked for convention; L126/L128 and the
September heat-route failure retain the infinite-height limitation.
L487's generic energy obstruction is a contrast, not an input to the
source theorem. Full Mathlib matching coverage is unchecked.

A distinct unread lead is Rodgers–Tao Remark 1.2's reference to
Ki–Kim–Lee Theorem 1.14 on positive-time high zeros. Its possible use is
height-uniform localization, independently of finite-height pair
integrability. A separate REVIEW_REQUIRED nomination asks only whether
it yields a common real/simple high-zero tail on compact positive-time
intervals. Average spacing, pointwise-in-time statements and an assumption
that t>Lambda would not settle that target. Finite collisions, t=0 and
all-degree signs remain unresolved even if that source question succeeds.
