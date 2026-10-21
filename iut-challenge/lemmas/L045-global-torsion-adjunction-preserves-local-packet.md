# L045 — Global torsion adjunction preserving the embedded local packet

## Hypotheses

Retain L044's fixed algebraic closure Omega of Q_3 and primitive
zeta_60. Let H=Q_3(zeta_60), k=Q(zeta_60), and
N=Q_3(zeta_420,3^(1/7)) be the embedded fields from that result.
Fix any one of L044's existential curves E_0/Q, and put E'=E_0 over k.
Thus all geometric 30-torsion over H is H-rational and
H(E'_H[7])=N inside Omega. Choose an embedded algebraic closure
Q-bar of Q in Omega containing zeta_60. Every torsion coordinate
field below uses both affine coordinates of every geometric torsion
point; the identity point contributes no coordinates.

Define F=k(E'[30]) in Q-bar, E_F=E_0 over F, and D=F(E_F[7]).
Let u and w be the places of F and D induced by the fixed 3-adic
embedding, with w restricting to u. Completions are identified with
the closures of these embedded fields in the corresponding finite
extensions of Q_3 inside Omega.

## Conclusion

F/Q is finite Galois and

[F:Q] divides 2^14 * 3^3 * 5 = 2,211,840.

In particular 7 does not divide [F:Q]. The full geometric 30-torsion
is F-rational, and the induced embedded completions satisfy

F_u=H and D_w=N.

The separate 2026-10-11 critical audit below validates this unchanged
known-method specialization. It is neither sufficient initial theta
data nor a demonstration of an essential IUT flaw or finite B>=A
failure. No explicit coefficient tuple or exact global degree is claimed.

## Proof

### Imported inputs

Reuse the inspected primary inputs in
`drafts/literature/2026-10-11-global-torsion-adjunction-preserving-completion.md`.
Sutherland, MIT 18.786, [Lecture 20, 1 May 2024](https://math.mit.edu/classes/18.786/2024/LectureNotes20.pdf),
section 20.1, pp.1–2, gives the continuous full-torsion representation
into GL_2(Z/mZ). Yvon, [arXiv:2407.14370v1](https://arxiv.org/pdf/2407.14370v1),
19 July 2024, Introduction, pp.1–2, identifies its kernel with the
pointwise fixing group of the full coordinate division field. No
surjectivity or linear disjointness assertion is imported.

Milne, [Elliptic Curves, second edition (2021)](https://www.jmilne.org/math/Books/EC2.pdf),
II, Proposition 6.3, pp.70–71, gives geometric n-torsion free of
rank two over Z/nZ when n is prime to field characteristic. All
fields here have characteristic zero, including Q_3 and H; the
residue characteristic 3 imposes no restriction on n=30.

Milne, [Fields and Galois Theory, v5.10 (September 2022)](https://www.jmilne.org/math/CourseNotes/FT.pdf),
Theorem 3.17 and Propositions 3.19–3.21, pp.39–42, provide the
Galois correspondence and the injective product representation for
Galois composita; 5.8–5.10, pp.64–66, give cyclotomic Galoisness
and degree phi(n); Theorem 8.1, p.105, supplies the CRT. Use also
Lagrange's theorem for finite groups. Cooper,
[The Conjugacy Classes of GL(2,Fq)](https://math.mit.edu/~dav/gl2conj.pdf),
section 1, equation (1.2), p.1, states
|GL_2(F_q)|=q(q+1)(q-1)^2, including q=2. These are general
known results, not new division-field theorems.

Milne, [Algebraic Number Theory, v3.08 (19 July 2020)](https://www.jmilne.org/math/CourseNotes/ANT.pdf),
section 8 immediately before Proposition 8.1, pp.135–136,
identifies the completion of an embedded finite extension K[alpha]
at its induced place with K-hat[alpha]. Characteristic zero gives
separability, so a finite coordinate list is covered by the primitive
element theorem. Apply this embedded statement, not just an abstract
isomorphism or a comparison of degrees. No imported theorem needs reproof.

### Agreement of the entire global and local torsion sets

Such an embedded Q-bar exists by extending Q's inclusion in the
algebraically closed Omega; its image contains all roots of each
polynomial over Q, hence contains the chosen zeta_60. Equivalently
it is the subfield of elements of Omega algebraic over Q.
For n=30 and n=7, base change along this embedding injects
E_0(Q-bar)[n] into E_0(Omega)[n]: points with equal coordinates
remain equal, and the group law and multiplication by n are defined
over Q. Each set has exactly n^2 elements by Milne II.6.3, applied
over the two characteristic-zero algebraic closures. Therefore the
injection is onto. The same sets serve E', E'_H and E_F after base
change. Thus every local geometric torsion coordinate in L044 occurs
in the global coordinate list, and conversely.
It does not identify E_0 with the original Tate curve.

### Galoisness and the degree bound

Put M_30=Q(E_0[30]). The finite representation
rho_30:G_Q -> GL_2(Z/30Z) has kernel exactly the subgroup fixing
M_30, since fixing both coordinates is equivalent to fixing every
torsion point. Its kernel is open and normal. The Galois
correspondence thus gives a finite Galois M_30/Q and a faithful
embedding of its Galois group into GL_2(Z/30Z).

By the CRT, Z/30Z is the product of F_2, F_3 and F_5. A matrix over
that product is invertible exactly when each component is invertible,
so the corresponding general linear group is their product. The
cited order formula gives respectively 6, 48 and 480. Hence

|GL_2(Z/30Z)|=6*48*480=2^10*3^3*5=138,240.

The cyclotomic extension k/Q is Galois of degree
phi(60)=60(1-1/2)(1-1/3)(1-1/5)=16. Agreement of the torsion
sets above gives F=k M_30. The Galois-compositum theorem makes
F/Q Galois. Restricting an automorphism to k and M_30 is injective,
because these fields generate F; it realizes Gal(F/Q) as a subgroup
of Gal(k/Q) times Gal(M_30/Q). Lagrange's theorem twice gives

[F:Q] divides 16*|Gal(M_30/Q)|,
16*|Gal(M_30/Q)| divides 16*138,240=2^14*3^3*5.

Thus 7 cannot divide [F:Q]. An upper bound alone would not give
this prime exclusion; the asserted divisibility is essential.
No intersection, disjointness or full-image hypothesis has been used.
By definition of F and agreement of the full torsion sets, every
geometric 30-torsion point of E_F is F-rational.

### Both induced embedded completions

L044 puts every coordinate in the global 30-torsion list inside H.
Since k is also inside H, F is a subfield of H. The closure of k in
H is H, as proved in L044: it contains Q_3 and zeta_60, and is
contained in H. Since k subset F subset H, the closure of F in H
is likewise H. Completeness of the finite extension H/Q_3, or the
cited embedded-completion theorem applied to the torsion list,
therefore identifies the induced F_u with exactly H.

Let S_7 be the finite list of both coordinates of all 7-torsion
points, using the agreed global/local set. Then D=F(S_7).
L044 says H(S_7)=N, so D is contained in the complete finite
extension N/Q_3. Its closure in N contains the closure H of F
and contains S_7, hence contains H(S_7)=N. Conversely the
closure is contained in N. It is thus N, and the induced completion
is D_w=N as an embedded field. This is also precisely the
specialization D_w=F_u(S_7) of the cited completion theorem.
Both directions are established; local degree matching alone is
not the argument.

### Qualifications

All four requested properties pass for this existential choice of
E_0. The result supplies field prerequisites only. It leaves global
mod-7 image, geometric-parameter and bad-place hypotheses, the
remaining selected initial data, native equivalence, actual inputs
and permitted actions, marked pilot transport and essentiality
unproved. In particular nothing here bounds the original B or
compares it with A. The exact-curve stop ATTEMPTS/027 remains
intact; the distinct-field stops ATTEMPTS/022,025,026 are not reopened.

### Separate critical audit — 2026-10-11

**Verdict and scope.** The stated result passes under the unchanged
SPECIALIZE assessment
`drafts/literature/2026-10-11-global-torsion-adjunction-critical-audit.md`.
Reuse its inspected primary coverage and the separate audit of L044;
no new source theorem, curve construction or stronger conclusion is
needed. The audit found no mathematical error or missing direct lemma
input. The direct input remains L044, which supplies the needed local
statements with its audited L042 input.

**Full torsion and pointwise kernels.** Omega is algebraically closed
of characteristic zero, as is the embedded Q-bar. The inclusion of
points concerns the same equation E_0 over Q on both sides, not E_0
and the Tate curve. It is injective on affine coordinate pairs and
on the point at infinity, and it commutes with multiplication by n.
Milne II.6.3 therefore makes it a bijection at n=30 and n=7: the
respective cardinalities are 900 and 49 in both closures. This is
valid also for the 3-primary part because field characteristic, not
residue characteristic, is the theorem's condition. Consequently
there are no additional local torsion coordinates outside the global
list. Changing the base among k, H and F changes rationality, not
these full geometric point sets.

For rho_30, an element fixes every point if and only if it fixes
every coordinate generating M_30. This is a pointwise condition;
setwise preservation alone would hold for every Galois element and
would not suffice. The finitely many coordinates are algebraic over
Q, so M_30 is finite, and the kernel is an open normal subgroup.
The quotient identifies Gal(M_30/Q) with the image of rho_30, not
necessarily the whole GL_2. The same coordinate convention is used
at level 7 in L044's actual restricted G_H-kernel identity. No
surjectivity or passage from local rationality to k-rationality has
entered the argument. Global 30-torsion becomes rational only after
adjoining that entire list to form F.

**Divisibility, including possible intersections.** CRT and the cited
order formula give 6=2*3, 48=2^4*3, and 480=2^5*3*5. Thus their
product is 2^10*3^3*5=138,240. The cyclotomic degree is phi(60)=16,
so the displayed final integer is 2^14*3^3*5=2,211,840. Since k/Q
and M_30/Q are finite Galois, their compositum is Galois. The
restriction homomorphism from Gal(F/Q) to the product of their
Galois groups has trivial kernel: fixing both generating fields fixes
F. Lagrange gives divisibility by 16*[M_30:Q], and the faithful
torsion action gives [M_30:Q] dividing 138,240. Combining these
divisibilities proves the claimed divisor, hence exclusion of 7.
Any intersection k intersect M_30 can shrink this subgroup and
does not invalidate the divisibility. Neither equality of degrees
nor disjointness is needed.

**Both embedded closures.** By full-set agreement and L044, every
30-torsion coordinate used in F lies in H; also k lies in H.
Thus k subset F subset H in the fixed embedding. The closure of k
in H contains the closure Q_3 of Q and the element zeta_60, hence
contains H=Q_3(zeta_60). It is contained in H, so it equals H.
The same two inclusions force the closure of F in H to be H.
As H is a complete finite extension of Q_3, this is exactly the
completion for the restricted absolute value u.

The level-7 coordinate list S_7 is finite and identical globally and
locally, and L044 gives H(S_7)=N inside Omega. Therefore D=F(S_7)
is contained in N. Its closure C in the complete finite extension
N is a field: field addition and multiplication are continuous and
inversion is continuous away from zero. It contains H, since the
closure of F in N is H (H is complete and therefore closed in N,
and F is dense in H). It also contains every element of S_7.
Hence N=H(S_7) subset C subset N. Thus C=N, identifying D_w=N
for the induced place w, whose absolute value restricts to u on F.
This verifies both inclusions in each embedded equality. It neither
assumes completeness of Omega nor replaces embeddings by a degree
comparison. The closure check is an applicability verification of
the cited completion theorem, not a new completion theorem.

The audit validates field prerequisites only. Global mod-7 image,
geometric-parameter and remaining initial-data conditions, native
equivalence, actual input/action, marked pilot transport, essentiality
and original finite B>=A remain open. The existing exact-curve and
other-field stops are unchanged. No mathematical script or numerical
certificate is needed for these finite cardinality and closure
checks; full matching Mathlib coverage remains unchecked.

## Mathlib

Full matching coverage of this torsion-adjunction and embedded
completion result has not been checked in Mathlib. No absence claim
is made. The proof is a specialization of the cited finite-torsion,
Galois, cyclotomic, finite-group and completion results, with no
claimed discovery beyond the sources checked.
