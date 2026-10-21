# L081 — Everywhere semistability over the exact auxiliary Legendre field

## Hypotheses

Retain precisely L078's auxiliary witness and choices D,s,t,iota,
its nonsingular pointed curve

    E_L: V^2=X(X-1)(X-t),
    G=Q(t)(iota,E_L[15]), M=G(E_L[7]),

and the induced places u_G,w_M. Division fields include both affine
coordinates of every geometric torsion point. L078 proves that G is
a number field, all geometric 15-torsion is G-rational, and the
embedded completions are G_(u_G)=H and M_(w_M)=N. No normality of
G/Q, equality G=F', or additional initial-data condition is assumed.

## Conclusion

E_L has semistable reduction at every finite place of this exact G.
The curve, field, embeddings and L078's two completion equalities are
unchanged. Semistability allows nonsplit multiplicative reduction;
everywhere split or everywhere good reduction is not asserted.

This is an application of known results, validated by the separate
step321 critical audit below. It supplies only a reduction prerequisite, not sufficient native
initial data, an essential IUT flaw, or the original finite B>=A.

## Proof

### Imported results

Reuse the invocation-start IMPORT assessment
`drafts/literature/2026-10-18-exact-legendre-everywhere-semistability.md`.
A. Silverberg and Yu. G. Zarhin, *Semistable reduction and torsion
subgroups of abelian varieties*, Ann. Inst. Fourier 45(2) (1995),
403–420, [Theorem 3.5, p.406](https://www.numdam.org/article/AIF_1995__45_2_403_0.pdf#page=5),
gives Raynaud's criterion: an abelian variety over a discretely
valued field has semistable reduction if its full geometric n-torsion
is defined over an unramified extension, for n>=3 prime to the
residue characteristic. The equality endpoint n=3 is included;
the [publisher's abstract](https://aif.centre-mersenne.org/item/AIF_1995__45_2_403_0/)
explicitly confirms it. The cited original is SGA7 I, Lecture Notes
in Mathematics 288 (1972), Expose IX, Proposition 4.7. No original
scan access or reproof is claimed. Definition 3.1, p.405, of the
published paper defines semistability by a semiabelian identity
component of the Neron special fiber; the torus need not split.

Use also J. S. Milne, *Elliptic Curves*, second edition (2021),
[II Proposition 6.3, pp.70–71](https://www.jmilne.org/math/Books/EC2.pdf):
in characteristic zero, the geometric n-torsion has n^2 points.
L049 records the same source method for a different curve/field;
its level-30 result is not a premise about the present E_L/G.
Only the following applicability argument is needed, not a new
reduction theorem.

### Complete geometric torsion at each completion

Let v be any finite place of G. Put K=G_v and let p be its residue
characteristic. This is a complete discretely valued field of
characteristic zero with finite residue field; E_L base changed to
K is an elliptic curve and hence an abelian variety.

For n=3 and n=5, n divides 15. Every global geometric n-torsion
point is consequently killed by 15, so L078 places both its
coordinates in G (and its origin is rational). Choose an embedding
of an algebraic closure of G into an algebraic closure of K extending
the completion map G -> K. Such an embedding exists by algebraic
closedness. It induces an injection on geometric n-torsion, since
it preserves the equation, identity and multiplication map. The
global and local geometric torsion sets both have n^2 points by
the cited Milne proposition, since both fields have characteristic
zero. The injection is therefore onto. Each point in its image is
K-rational because its original coordinates lie in G. Thus all
geometric E_L[n] over K is K-rational, for each of n=3,5.

This argument is applied independently to every v; it does not
identify every place with L078's chosen 3-adic embedding. In
particular characteristic zero, rather than the residue
characteristic, controls the torsion cardinality used here.

### All finite residue-characteristic cases

If p!=5, choose n=5. Then n>=3 and gcd(n,p)=1, including p=2
and p=3. If p=5, choose n=3. Again n>=3 and gcd(n,p)=1, using
the explicitly covered equality endpoint of the criterion. In each
case the complete geometric n-torsion is already K-rational by the
previous paragraph. Take the unramified extension to be K/K itself:
its ramification index is one and its residue-field extension is
the identity. Every hypothesis of the cited criterion is satisfied,
so E_L/K has semistable reduction. Reduction at v is reduction over
this completion. Since v was arbitrary, this proves the conclusion.

The test passes without a missing residue-characteristic case or a
field enlargement. No use of level 15 at its residue divisors is
made. Nothing in this application requires normality of G/Q.

### Retention and relevance

No equation, generator, place or embedding has changed, so L078's
embedded H,N equalities remain true. This closes the semistability
part of the proposed exact-field reduction test using known results;
it is not progress beyond the cited theorem. A subsequent pointed
stable-model argument would need its own approved scope. Independent
normality/mixed radical-torsion information, other initial data,
actual native input/action, marked all-image factorization, pilot
transport, essentiality and the original finite B>=A remain open.
The retained original E_0,F,K_glob,q_0 are not replaced by this
auxiliary curve. ATTEMPTS/027,028,031,032,033,034 are unaffected.

### Separate critical audit — 2026-10-18, step321

The invocation-start IMPORT assessment
`drafts/literature/2026-10-18-exact-legendre-semistability-critical-audit.md`
covers this exact audit. The whole proof above and L078's hypotheses,
construction and separate audit were checked. The imported statements
were reopened at the cited locations: Silverberg–Zarhin Definition 3.1
and Theorem 3.5, its publisher's explicit n>=3 endpoint, and Milne
II.6.3 with its characteristic-zero proof case. No original SGA7 scan
or new proof of Raynaud's criterion is claimed. The PDF text extraction
still obscures the inequality; the publisher's English and French
abstracts both include equality at 3, as the approved coverage records.

**Actual base and complete torsion.** L078 defines G using both
coordinates of every geometric 15-torsion point of this very E_L.
Its construction establishes t!=0,1 and G/Q finite before this
application; thus E_L/G is nonsingular. For any finite v, G_v has
characteristic zero and a discrete valuation with finite residue
field. The algebraic-closure embedding extending G -> G_v is an
algebraic field embedding, not an assertion about a continuous
identification of closures or about the selected place above 3.
It preserves distinct points and the multiplication maps. For n=3,5,
the relation [15]=[15/n] composed with [n] places every global
n-torsion point in the full rational 15-torsion. Milne II.6.3 gives
exactly 9 and 25 points respectively on both geometric sides; the
injections therefore exhaust the local torsion. Both coordinates
of each image lie in G_v. The origin is rational separately.
Neither reduction of torsion modulo v nor preservation of its order
under reduction is used. In particular, local field characteristic
zero is not confused with residue characteristic.

**Criterion and exhaustive place split.** At p!=5 choose level 5,
which includes p=2 and p=3. At p=5 choose level 3; the endpoint
is covered and 3 is prime to 5. These two disjoint cases exhaust
finite places. Each selected level is at least 3 and prime to p,
and all its geometric points are defined over G_v itself. The
identity extension is unramified (also in the finite-etale valuation
ring sense). The exceptional n=2 clause, with its extra hypotheses,
is never invoked. Raynaud's conclusion is semistability at the
valuation in question; Definition 3.1 permits a nonsplit torus.
No polarization or isotropic-subgroup variant is substituted for
the full-torsion theorem.

**Verdict and retention.** Every applicability check passes without
a correction or an added hypothesis. No base extension, equation
change or reselection occurs, so L078's actual G_(u_G)=H and
G(E_L[7])_(w_M)=N persist with their original places. Normality of
G/Q and L049's different level-30 curve play no role. The sole
direct local input remains L078. This audit verifies the known-result
application; it establishes no new reduction theorem or original
finite B>=A comparison. A stable one-pointed model, independent
initial data and the transport/essentiality gaps remain outside
its conclusion. The proof and DAG are unchanged; this canonical
verdict supersedes the overview's pending-audit wording.

## Mathlib

Full matching and supporting Mathlib coverage for this exact-field
application and Raynaud's criterion has not been checked. No absence
or formal verification claim is made. The general inputs are the
precisely cited published theorems above, with L078 as the sole direct
local mathematical input. No calculation certificate is needed.
