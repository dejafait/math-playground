# L049 — Everywhere semistability after full torsion adjunction

## Hypotheses

Fix the same reselected elliptic curve E_0/Q of L048, at its fixed
precision M>=max(M_tors,31). Retain its embedded algebraic closure
Omega of Q_3, H=Q_3(zeta_60), N=Q_3(zeta_420,3^(1/7)), and absolute
valuation v_3(3)=1. Set F=Q(zeta_60,E_0[30]) and D=F(E_0[7]),
using both coordinates of every geometric torsion point as in L045.
Let E_F be E_0 base changed to F; u and w are the unchanged places
induced by the fixed embedding, with w over u.

## Conclusion

E_F has semistable reduction at every finite place of F.
No curve or field enlargement is required. In particular the same
curve still has the embedded completions F_u=H and D_w=N, full
F-rational 30-torsion, and its geometric Tate parameter q_0 over Q_3
has v_3(q_0)=30. All other conclusions of L048 are retained.

This known-result import passes the separate 2026-10-11 critical audit below.
It asserts neither everywhere split reduction nor sufficient initial
theta data, and gives no original finite B>=A comparison or IUT flaw.

## Proof

### Precise imported criterion

Reuse the approved IMPORT assessment
`drafts/literature/2026-10-11-global-semistability-after-torsion-adjunction.md`.
A. Silverberg and Yu. G. Zarhin, *Semistable reduction and torsion
subgroups of abelian varieties*, Annales de l'Institut Fourier 45(2)
(1995), 403–420, [Theorem 3.5, p.406](https://www.numdam.org/article/AIF_1995__45_2_403_0.pdf#page=5),
states Raynaud's criterion: for an abelian variety X over a field K
with a discrete valuation v, if n>=3 is prime to the residue
characteristic and every point of X[n] is defined over an extension
unramified over v, then X has semistable reduction at v. Its cited
original source is Grothendieck, *Modeles de Neron et monodromie*,
SGA7 I, Lecture Notes in Mathematics 288 (1972), Expose IX,
Proposition 4.7. The published theorem is the inspected usable
statement; no original scanned-source access is claimed here.
The exceptional n=2 branch is unused. No reproof is needed.

Semistability has Definition 3.1, p.405, of the same paper's meaning:
the identity component of the Neron special fiber is an extension
of an abelian variety by a torus. It does not require that torus
to split. For an elliptic curve this is good or multiplicative
reduction, allowing nonsplit multiplicative reduction.

### Local applicability at every finite place

By L045, applied to precisely the L048 curve, F is a number field
and all geometric 30-torsion of E_F is F-rational. Let v be any
finite place of F, put K=F_v, and let p be its residue characteristic.
K is a characteristic-zero local field with a discrete valuation;
its valuation ring is complete and hence henselian, though the
criterion's n>=3 branch does not impose the exceptional n=2
henselian/separably-closed-residue hypotheses. E_F base changed to K
is an elliptic curve, hence an abelian variety over K.

For n=5 or n=6, n divides 30, so every geometric n-torsion point
is killed by 30. Thus E_F[n] is a subset of E_F[30], and all its
points are F-rational. To check that completion creates no extra
geometric torsion points, choose an embedding of an algebraic closure
of F into an algebraic closure of K extending F -> K. Base change
injects the global geometric n-torsion into the local geometric
n-torsion, respecting coordinates, the identity, and multiplication
by n. Both sets have n^2 points in characteristic zero by the
standard geometric torsion theorem cited in L045 (Milne, *Elliptic
Curves*, second edition, II, Proposition 6.3, pp.70–71).
The injection is therefore onto. Consequently every geometric
n-torsion point over K is K-rational. This applies separately for
each v and does not assume that the fixed 3-adic embedding represents
all places.

If p!=5, use n=5: it is at least 3 and prime to p, including p=2
and p=3. If p=5, use n=6: it is at least 3 and prime to 5.
In either case every n-torsion point is already defined over K.
Take the extension in Raynaud's criterion to be K/K itself; it is
unramified (ramification index one and identical residue field).
The cited theorem gives semistable reduction of E_K at its discrete
valuation. Reduction of E_F at v is precisely reduction after this
completion, so E_F is semistable at v. Since v was arbitrary, the
assertion holds at every finite place. In particular no application
of n=30 at primes dividing 30 is made.

### Retention and limitations

This argument changes neither E_0 nor F nor their embeddings.
L048 and L045 therefore still give F_u=H, D_w=N and v_3(q_0)=30,
as well as their other conclusions, for this same curve. The
parameter is q_0, not an assertion q_0=3^30. There is no second
curve selection, extra precision requirement, disjointness assumption
or field enlargement.

Every finite residue-characteristic case passes the approved test.
This supplies a consequence of the retained full-torsion prerequisite
by a known theorem, not progress beyond that theorem. Everywhere
semistability over F does not prove multiplicative reduction for
selected models over Q(j_E), their parameter-order restrictions,
sufficient global/selected initial data, native equivalence, actual
input/action realization, marked pilot transport or essentiality.
The original finite B>=A gap remains open. ATTEMPTS/022,025,026,027
are unchanged: their excluded fields or exact Tate curve are not
used as new realizations.

### Separate critical audit — 2026-10-11

**Verdict and scope.** The unchanged conclusion passes under the prior
SPECIALIZE assessment
`drafts/literature/2026-10-11-global-semistability-critical-audit.md`.
This is an independent check of the application, reusing the inspected
Silverberg–Zarhin Theorem 3.5 and Milne II.6.3 and the audited L045/L048
inputs. No new reduction criterion or stronger conclusion is asserted.

**Quantifiers and complete torsion.** Fix an arbitrary finite place v
of the one number field F, and let K=F_v. The inclusion F -> K
extends to an embedding F-bar -> K-bar because K-bar is algebraically
closed; no compatibility between choices for different v is required.
The equation and pointed group law of E_0 are the same under this
embedding. For n=5 and n=6, a point killed by n is killed by 30,
so all n^2 global geometric n-torsion points have coordinates in F
by L045. Distinct points remain distinct after embedding (including
the point at infinity). The local geometric n-torsion also has
exactly n^2 points by Milne II.6.3, since char(K)=0. Thus those
embedded points exhaust it and all lie in E_0(K). In particular
neither a cyclic subgroup nor only the torsion visible under the
fixed 3-adic embedding has been substituted for full local torsion.
Residue characteristic is irrelevant to this cardinality argument.

**Criterion at all finite places.** The residue characteristic p of K
is a positive prime. For p other than 5, choose n=5; for p=5, choose
n=6. These cases exhaust the finite places, and in both n>3 and
gcd(n,p)=1. In particular the p=2 and p=3 cases use 5, never 6 or
30. K is discretely valued, and E_0 over K is an abelian variety.
The identity extension K/K has ramification index one and unchanged,
hence separable, residue extension; it is unramified. The complete
n-torsion just checked is rational over that extension. These are
all the hypotheses of the used branch of Theorem 3.5, whether its
threshold is read as n>=3 or the extraction's n>3. No n=2 branch
or separably closed residue-field hypothesis is invoked. The
conclusion is semistability at v, understood after completion as
in the statement. Since v was arbitrary, every finite place is
covered. Definition 3.1 supplies a torus, not necessarily a split
torus; no everywhere-split or everywhere-good conclusion follows.

**Simultaneous retention.** L048 first fixes M>=max(M_tors,31),
then selects one E_0 satisfying the complete local 210-module and
global mod-7 conclusions. This audit applies the criterion to that
already selected E_0 over its already defined F. There is no further
existential curve choice or extension of F. Hence D=F(E_0[7]), the
fixed embeddings and the induced places u,w are literally unchanged.
L045's closure identities still give F_u=H and D_w=N inside Omega.
L048's split reduction over Q_3 and absolute v_3(q_0)=30, its global
GL_2(F_7) image, and its retained SL_2(F_7) containment over F all
concern this same curve. Nothing in the criterion changes q_0 or
identifies it with 3^30; in particular its absolute valuation is
not replaced by an integer-normalized H-valuation. The direct
mathematical inputs remain L045 and L048, with earlier inputs used
through them. No DAG change is needed.

No mathematical repair was required. This validates the local
application of known results, not progress beyond those results.
The distinct stops ATTEMPTS/022,025,026,027 remain intact. In
particular semistability after passage to F says nothing here about
every selected model over Q(j_E); sufficient initial data, actual
input/action realization, marked pilot transport, essentiality and
the original finite B>=A remain unresolved. No numerical evidence
or mathematical script is used in this audit.

## Mathlib

Full matching Mathlib coverage of Raynaud's criterion and this
same-curve everywhere-semistability application has not been checked.
No absence claim is made. The proof imports the named published
criterion and the standard geometric torsion theorem cited above;
it needs no mathematical script or numerical evidence.
