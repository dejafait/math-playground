# Root-eliminating reciprocal residual — source-review nomination

TARGET: Compare the proposed r=k+1 root-eliminating reciprocal-tail congruence with classical Bezoutian/Hankel identities and determine whether it offers an independent actual-Xi sign input.
CHECKED: 2026-11-05
DECISION: EXPLORE
SEARCH_EVIDENCE: Step456 searched rational Bezoutian/Hankel inversion, Loewner/confluent transformations, reciprocal Taylor coefficients and Xi Hankel signs; inspected primary statements and essential proof cases below, and reused step443/448/452/454 scope and failure evidence. No exact analytic residual theorem was identified; no novelty inference.
SOURCE_EVIDENCE: Heinig-Rost, Bezoutians, Chemnitz preprint2008-09, Sections7.1/7.3-7.6 pp.39-46 and9.1 pp.54-55, especially Proposition7.15/proof, Proposition7.18/proof, Theorem7.19 and Proposition9.1/proof; Jouve-Rodriguez-Villegas, arXiv:1004.4208v3 (12 September2013), Theorem2.1/proof pp.2-3, Proposition2.4, Lemmas2.5-2.6, Theorem2.7 and Remark2.8 pp.5-6; Vavrin, Czech. Math. J.44 (1994),571-575, Definition3 and Theorem5/proof pp.573-574. Direct links and qualifications below.
COMPARISON: Known rational congruences eliminate evaluation coordinates but retain coefficient-form inertia, residue orientation and nullity. Their expansion is at infinity and their size follows a polynomial denominator; they do not themselves identify the prescribed analytic residual with a particular local reciprocal block. No independent actual-Xi sign estimate was found in the inspected sources.
GAP: The exact residual-to-local-coefficient map, block indexing, invertibility and singular cases remain unproved. Even a successful map would leave actual-Xi coefficient signs, all-degree grouping and global coverage unpaid; no new equivalent criterion is asserted.
REASON: The new primary-source comparison parks automatic root-elimination-to-sign inference. It supports at most one separately approved symbolic coefficient-interface attempt, whose utility is removing root isolation from a future sign test, not obtaining a sign from a congruence.
LITERATURE_REASON: The invocation-start REVIEW_REQUIRED target changes from a fixed atomic calculation to a general root-eliminating congruence; existing ready assessments contain no primary Bezoutian/Hankel theorem for that interface.
SCOPE: Completed literature-only step456 for the nominated even k>=2,r=k+1 analytic grouping scope. Only cited rational/confluent interfaces are imported as source coverage; no general residual identity, new lemma, calculation, mathematical script or Xi sign is derived.

The main gap remains actual-Xi all-degree mixed positivity. The proposed
intermediate target is an exact congruence eliminating the selected root
locations from the residual inertia question in favor of a specified
finite block of local reciprocal coefficients. Its possible downstream
use is to expose a sign condition that actual-theta identities could
estimate directly. That independent sign payment is not currently known.
No general formula is asserted by this nomination.

For source matching, fix an even integer k>=2, r=k+1 and sigma>1.
Let g be real analytic on a complex neighborhood of the closed sigma
disk, with g(0)>0 and exactly k simple distinct negative nonzero zeros
alpha_i inside the unit disk, and no other zeros in the sigma disk.
Set P=product_i(z-alpha_i), F=g/P, p=z^-k P, b=p/F and c=F/p.
Use complete Laurent coefficients beta of b, residues
d_i=alpha_i^k F(alpha_i)/P'(alpha_i), h_r(z)=sum_(n>=0)
beta_(r+1+n)z^(n+1), and its divided-difference matrix K at the roots.
The candidate residual is J+E K E, where J=diag(sign(d_i)) and
E_ii=sqrt(|d_i| |alpha_i|^r). The source question is whether an
explicit invertible congruence identifies this residual with a finite
Hankel block of the local Taylor coefficients u_n of 1/g at0, and what
exact block, restrictions and
signature information the theorem supplies. These are target definitions,
not a claimed generalization of L784. All root/grouping hypotheses remain
conditional for actual Xi outside already certified instances.

Use L784 equations(6)–(8) and its independent audit as the fixed-case
motivation. L777/L782 are convention comparisons requiring narrow reads
if needed, not general premises. L781's optional generalized Nevanlinna
test uses -beta_(4+i+j), not coefficients of 1/g, and is closed.
L783 and the automatic-class, linked-factor and local-premise stops
exclude obtaining the missing index solely from reciprocity or an
unpaid completion. Preserve their evidence. No cross-notebook input.

Read primary Bezoutian/Hermite/reciprocal-Hankel theorem hypotheses and
essential proof cases, searching exact statements and stronger results.
Compare with existing determinant criteria before proposing a reproof.
An identity covered by a source should be imported with its applicability
argument, not presented as a new sign mechanism. Sources or all-degree
signature assumptions equivalent to real-rootedness do not close the gap.

The discriminating test is source-level: identify both a precise
root-eliminating interface and any genuinely independent actual-Xi sign
estimate, or document that the available reduction merely repackages the
unpaid mixed-minor condition. In the latter case park it as a sign route;
do not start a chain of model calculations or repeated congruence audits.
Missing theorem coverage remains REVIEW_REQUIRED or SOURCE_BLOCKED,
never permission for an uncovered derivation. A useful narrower identity
may be imported, but its independent sign and global-grouping gaps must
remain explicit. Full matching Mathlib coverage is unchecked.

No creative proof attempt is yet nominated: finite-jet elimination alone
has no independently paid sign. This review prepares or rejects that
possibility before another mathematical target is selected.

## Completed source comparison — step456

The main gap remains actual-Xi all-degree mixed positivity. The reviewed
intermediate target is elimination of selected roots from the reciprocal
residual's inertia test. A coefficient-only interface could remove root
isolation from a later signed test, but an identity cannot supply that
test's inequality. The proposed all-degree analytic identity has not
been proved here. No calculation or new mathematical result is reported.

### Exact rational interfaces

Georg Heinig and Karla Rost, *Bezoutians*,
[Chemnitz preprint2008-09](https://www.tu-chemnitz.de/mathematik/preprint/2008/PREPRINT_09.pdf),
Section7.1, printed p.39, defines a proper rational function a(t)/q(t)
by its expansion h_0+sum_(j>=1)h_j t^-j at infinity, and
H_n=(h_(i+j-1))_(i,j=1)^n. The constant h_0 is excluded.
This is not the local convention u_j=the Taylor coefficient of z^j in 1/g.

Section7.5, Proposition7.15/(7.11), printed p.45, assumes deg(q)=n
and deg(a)<=n, and states

    Bez_H(q,a)=B(q) H_n(a/q) B(q).

Here B(q)=Bez_H(q,1) is the coefficient matrix defined in(2.2).
For this n-by-n case the transformation is invertible, and over the
reals this is a congruence. The displayed proof expands the divided
difference of a/q, multiplies by q in both variables and compares
coefficients. It does not assume that the Bezoutian is positive or
that a,q are coprime. Proposition7.18 and its proof, pp.45-46,
also discuss unreduced fractions and inertia after the stated padding.
For the present assessment use only the n-by-n identity; no larger
padded matrix is identified with our k-by-k residual.

Theorem7.19, p.46, is a different interface: with coprime q,a of
the stated degree bounds and polynomial solution q*s+a*t=1,
the inverse Bez_H(q,a)^-1 is H_n(t/q). Its numerator t is a modular
inverse. It is not the ordinary analytic reciprocal of a/q, and the
coprimality/inverse hypothesis cannot be used to dispose of an unknown
residual nullspace. Read the preceding(7.13), the theorem and the
Bezout-equation construction; no residual inverse is imported.

Section9.1, Proposition9.1/(9.3)-(9.4) and its complete proof,
p.54, assumes q,a of degrees at most n with deg(q)=n and
q-lambda*a having n distinct roots t_i. Evaluation by the square
Vandermonde gives diagonal entries q'(t_i)a(t_i)-q(t_i)a'(t_i).
Real roots give a real congruence. Corollary9.4, p.55, accounts for
conjugate nonreal pairs by Hermitian two-by-two blocks. These results
do not turn an arbitrary divided-difference matrix into a k-dimensional
coefficient Hankel matrix without identifying its polynomial pair,
degree and change of basis.

For sign information, Section7.3, Corollaries7.11-7.12, p.43,
requires a reduced real rational function of degree n with simple
poles and their residues. Its signature formula counts signed real
residues; nonreal conjugate poles contribute paired blocks. In particular
its positive-definiteness conclusion explicitly needs real poles and
positive residues. Proposition7.13 and its proof, p.44, treats the
Cauchy index including multiple poles, retaining their types and
nondegeneracy. None of these hypotheses estimates Xi's inverse jets.

Two source qualifications matter. Corollary7.16 prints the reciprocal
ratio relative to(7.11); this assessment uses the explicit formula and
proof of Proposition7.15, not that shorthand. Corollary7.14's bare
interlacing formulation omits the residue orientation stated in7.12;
no unsigned interlacing-to-positivity import is made. The source's
larger-size rank discussion is unnecessary for the n-by-n interface.
These are reading qualifications, not new counterexample lemmas.

Florent Jouve and Fernando Rodriguez-Villegas, *On the bilinear structure
associated to Bezoutians*,
[arXiv:1004.4208v3](https://arxiv.org/pdf/1004.4208v3),
12 September2013, supplies an independent convention check.
Theorem2.1 and complete proof, pp.2-3, starts with a finite-dimensional
monogenic Frobenius algebra, or equivalently a reduced strictly proper
rational function a/q, q monic, deg(q)=d and deg(a)<d. Its Hankel
form is nondegenerate, not assumed positive. Proposition2.4 and
Lemmas2.5-2.6, p.5 through the top of p.6, give the multiplication
matrix and coefficient-matrix interfaces. Lemma2.5's coefficient proof
was read; Lemma2.6 is stated with proof left to the reader by the source.
Theorem2.7, p.6, uses the polynomial inverse of a modulo q.
Remark2.8 explicitly states

    Q^T H(a/q) Q = -B(a,q), Q_(i,j)=q_(i+j-1).

The minus sign and polynomial order are essential. This agrees with
the first source's explicit convention after reversing the order of
the Bezoutian arguments. It does not identify either source's form
with J+E K E, or identify local u_j with rational coefficients at infinity.
Do not transfer a rational finite-rank or nondegeneracy statement to the
full analytic tail merely because finite jets occur in L784.

### Confluent case and unread leads

Zdenek Vavrin, *A remark on confluent Cauchy and confluent Loewner
matrices*, Czech. Math. J.44 (1994),571-575,
[primary DML PDF](https://dml.cz/bitstream/handle/10338.dmlcz/128473/CzechMathJ_44-1994-3_14.pdf),
Definition3, p.573, permits coincident row and column nodes in the
divided-difference definition. Theorem5 and its complete proof,
pp.573-574, identify a specially constructed rational Loewner matrix
with a confluent Cauchy matrix when the two node sets are disjoint.
Our matrix has matching row/column nodes, including derivative entries;
that theorem's disjoint-set hypothesis does not apply. The definition
matches the diagonal convention but supplies no inertia theorem.

M. Fiedler, *Hankel and Loewner matrices*, LAA58 (1984),75-95,
DOI10.1016/0024-3795(84)90205-2, and Z. Vavrin, *A unified approach
to Loewner and Hankel matrices*, LAA143 (1991),171-222,
DOI10.1016/0024-3795(91)90011-K, remain unread full-text leads:
publisher access returned403. Fuhrmann's *Remarks on the Inversion
of Hankel Matrices*, LAA81 (1986),89-104, author PDF timed out.
The primary substitutes above provide the rational interfaces actually
used; no result from these unread works is asserted. A search-returned
2026 reciprocal-Xi/Thorin preprint likewise had inaccessible full text
and supplies no theorem here. Search-returned modern RH moment-criterion
claims are not treated as inspected results or independent sign estimates.
No source absence or novelty is inferred from these access results.

### Applicability, overlap and bounded decision

L784(6)-(8) proves exact finite-jet cancellation for its single model.
Its nodes are still present in the resulting entries. The new proposed
general congruence needs a precise polynomial/rational pair, correct
origin-to-infinity coefficient conversion, exact Hankel shift and size,
an invertible *real congruence* and treatment of possible zero eigenvalues.
The source formulas do not by themselves identify these objects.
No such identification, nor any k-independent extension of L784, is
derived or certified by this literature turn.

The known rational transformations preserve a form's signs; their
signature theorems require signed residues or equivalent input. Thus the
immediate-import test fails: no inspected theorem gives both the proposed
root-free residual interface and independently paid actual-Xi signs.
Park automatic root-elimination-to-sign inference. This is source-scope
evidence, not a proof that a useful congruence or sign estimate cannot
exist, and not a proof that the proposed finite reciprocal block is
RH-equivalent. L030-L032/C032a concern a different power-sum Hankel
tower; they do not already establish an identity for these u_j.

Checked the exact L784 tail evaluation, step455 audit history, step443
class assessment, step448 linked-factor review, step444 Taylor stop,
L783's statement and its local-premise stop. L781's tested coefficients
are those of a different tail; neither its result nor L773 is retested.
The automatic-index and linked-factor stops remain intact. No new model
experiment, audit replay or growing-order test is nominated.

A useful smaller algebraic question remains: for arbitrary admissible
k=2,r=3 data, can the finite inverse jet remove node locations from
the *coefficient form*, with an explicit change of basis? A single
symbolic attempt would test that interface without claiming a sign;
success could make a later actual-theta inequality testable without
root isolation. The new separate assessment names this target and its
stop test; it must receive separate approval before mathematics.
It does not reopen the parked automatic sign route. It is known-method
development, not a creative central sign mechanism. Such creative work
is blocked by the absence of an independently motivated theta sign
input, not by the historical stops or a scheduling quota.

Queries included `Bezoutian Hankel matrix Laurent expansion rational
function congruence inverse theorem`; `Bezoutian divided difference
matrix analytic function Hankel reciprocal Taylor coefficients`;
`Loewner Hankel congruence rational interpolation divided differences
theorem Fiedler Vavrin`; `Riemann xi reciprocal Taylor coefficients
Hankel determinants positivity Bezoutian`; `Bezoutian reciprocal Taylor`;
`Hankel Bezoutian residue bilinear form local algebra power series
coefficient polynomial quotient`; and the exact Fiedler/Vavrin titles.
Local searches were restricted to this notebook. The initial combined
local search was too broad and its output truncated; it establishes no
exhaustive failure/duplicate check. The relevant specific files were
then read directly as listed above. No cross-notebook input was used.

Full matching Mathlib coverage is unchecked. This is local literature
progress and a sign-route stop, with no mathematical advance beyond the
inspected sources. No lemma, mathematical script, DAG or main argument
was changed. Exploration calculation budget used: zero; no counter is
reset by this literature result. Preserve all unfinished notebook work.
