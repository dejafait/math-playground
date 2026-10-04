# L017 — Conditional mixed seventh-power reducible-character traces

## Hypotheses

Let F=Q(sqrt(5)), O_F=Z[epsilon], epsilon=(1+sqrt(5))/2, and let G_F be the absolute Galois group. Write chi_7 for the mod-7 cyclotomic character. Let

\[
rho:G_F\longrightarrow GL_2(\overline{F}_7)
\]

be continuous for the discrete coefficient topology and reducible over the indicated algebraic closure. Assume:

1. det(rho)=chi_7, in the weight-two normalization.
2. rho is unramified at every finite prime outside the primes over 3,5,7.
3. At lambda_3=(3) and lambda_5=(sqrt(5)), its Artin-conductor exponents satisfy a_lambda(rho)<=3.
4. At p=(7), rho is finite flat: after descent to a finite coefficient field, its underlying F_7 representation is the generic fibre of a finite flat commutative group scheme killed by 7 over O_(F_p). In particular Raynaud's finite-flat Jordan–Hölder inertia theorem applies. No inertia digit list is assumed separately.

Set q=(29,sqrt(5)-11). Frobenius means arithmetic Frobenius; geometric Frobenius gives the same conclusion here. The hypotheses are conditional. This lemma does not establish that every original Diophantine solution supplies such a representation or this prime's four curve parameters.

## Conclusion

After possibly interchanging its two constituents, rho has semisimplification

\[
rho^{ss}=psi\oplus chi_7 psi^{-1},
\]

where psi is unramified at p and its finite conductor divides 3(sqrt(5)). Either real place may still occur in its conductor. For every such representation,

\[
psi(Frob_q)^2=1,\qquad
tr(rho(Frob_q))\in\{2,-2\}=\{2,5\}\subset F_7.
\]

Consequently the two linear polynomials T-2 and T-5 cover the entire reducible sector under these hypotheses. This reproduces the conditional character claim in [Chocian, arXiv:2609.26996v1, Section 6.2, equations (36)–(37) and the paragraph following (39)](https://arxiv.org/html/2609.26996v1#S6.SS2). It is not an exclusion of a Beal signature or a proof of the irreducible modular-packet list.

## Proof

**Conductor away from 7.** Continuity and compactness give finite image, so all constituents are defined over a finite coefficient field. Reducibility and the determinant give the displayed form of rho^ss. At lambda not dividing 7 the cyclotomic character is unramified, and inversion does not change the Artin conductor of a character. Thus both constituents have conductor exponent a_lambda(psi).

For residual characteristic 7 at these primes, Swan conductor is additive on constituents because the wild inertia groups have order prime to 7. The dimension of inertia invariants cannot decrease on passage to semisimplification: the dimensions of invariants of a submodule and quotient bound the dimension for an extension from above. The tame conductor therefore cannot increase on semisimplification. Consequently

\[
2a_lambda(psi)=a_lambda(rho^{ss})\leq a_lambda(rho)\leq3
\]

at lambda_3 and lambda_5. The exponents are nonnegative integers, so a_lambda(psi)<=1. At all other finite primes away from 7, psi is unramified. The same facts hold for the other constituent. Equivalently, each character is trivial on principal local units at lambda_3 and lambda_5.

**All finite-flat scalar inertia types.** The polynomial X^2-X-1 has no root modulo 7. Thus p=(7) is inert, F_p/Q_7 is unramified of degree two, its residue field has order 49, and its absolute ramification index is e=1.

A finite-image scalar character with values in characteristic 7 has trivial wild inertia, since a finite 7-group cannot map nontrivially into the multiplicative group of a finite field of characteristic 7. For a tame inertia generator tau and a local Frobenius phi, the relation is phi tau phi^(-1)=tau^49 in the tame quotient. A scalar character of the full local Galois group is unchanged by this conjugation. Its value at tau therefore has order dividing 49-1=48.

Pass to the strict henselization of O_(F_p). This replaces the local Galois group by inertia without changing e=1 or finite flatness. Apply [Raynaud, *Schémas en groupes de type (p,...,p)*, Bull. Soc. Math. France 102 (1974), Theorem 3.4.3 and Corollary 3.4.4, printed p. 270](https://www.numdam.org/article/BSMF_1974__102__241_0.pdf#page=31) to the underlying F_7 Jordan–Hölder factors. Every scalar constituent over the algebraic closure is an embedding of one of these factors. Its minimal field of inertia values lies in F_49 by the order bound, so its degree n over F_7 is one or two. Raynaud's digits lie between 0 and e, hence are 0 or 1.

Let omega_2 be a level-two fundamental character, with omega_2^8=chi_7 on inertia. For n=1, the level-one character is omega_2^8, giving exponents 0 or 8. For n=2 the digit expression gives exponents r0+7r1 with r0,r1 in {0,1}. Together these are exactly the possible list

\[
psi|_{I_p}=omega_2^a,\qquad a\in\{0,1,7,8\}.
\]

The two embeddings of F_49 exchange exponents 1 and 7 and preserve the list. In particular this argument has not restricted the coefficient field to F_7 or discarded the mixed types.

**A global unit excludes the mixed types.** Using epsilon^2=epsilon+1 gives

\[
u=epsilon^8=13+21epsilon.
\]

It is a global unit and is positive at both real embeddings. Modulo (3), its residue is 1. Modulo (sqrt(5)), epsilon=3 in F_5 and its residue is 13+21*3=1 modulo 5. These two ideals are coprime, so u=1 modulo 3(sqrt(5)). At p its residue is -1.

Use local-global compatibility and the product formula on the principal idele u: [Milne, *Class Field Theory*, v4.03 (6 August 2020), Chapter V, Proposition 5.2 and Theorem 5.3, printed pp. 178–179](https://www.jmilne.org/math/CourseNotes/CFT.pdf#page=186). Every local character value away from p is 1. At lambda_3 and lambda_5 this follows from the conductor bounds and the congruence; at every other finite place u is a unit and the character is unramified. At both real places u is positive, regardless of the character's signs. Therefore

\[
psi(rec_p(u))=1.
\]

Tame local reciprocity identifies residue units with the corresponding abelian tame inertia quotient. The residue -1 is its element of order two, so omega_2(rec_p(u))=-1. Choosing the inverse reciprocity convention or the other residue embedding preserves this value. For a=r0+7r1 the preceding equality becomes (-1)^(r0+r1)=1. It eliminates a=1 and a=7; the only surviving types are a=0 and a=8.

If a=0, psi is unramified at p. If a=8, chi_7 psi^(-1) is unramified there. Choose the unramified constituent and call it psi. Its finite conductor now divides 3(sqrt(5)). Include both real places in the ray modulus

\[
m=3(sqrt(5))\,infty_1\,infty_2.
\]

This includes every possible real-place sign; no total-evenness assumption was made.

**A positive ray relation at q.** Put alpha=6-epsilon. Its norm is

\[
N(alpha)=(6-epsilon)(6-epsilon')=36-6-1=29.
\]

Modulo q, epsilon=(1+11)/2=6, so alpha lies in q. Its ideal norm is 29, hence (alpha)=q. Both real embeddings of alpha are positive.

Since epsilon^(-2)=2-epsilon, direct ring multiplication gives

\[
beta=alpha^2/epsilon^2=85-48epsilon
     =1+3sqrt(5)(8epsilon-12).
\]

Thus beta is positive at both embeddings, (beta)=q^2, and beta=1 modulo 3(sqrt(5)). It is a valid positive principal ray relation for m, proving that the ray class of q has order dividing two. The ray-class interpretation is the standard one in [Milne, Chapter V, Theorems 1.7 and 3.5, printed pp. 150 and 158](https://www.jmilne.org/math/CourseNotes/CFT.pdf#page=158). Neither the full ray-group structure nor a proof that this class is nontrivial is needed for the upper trace restriction.

Equivalently apply the same principal-idele product formula directly to beta and the selected psi. At q, psi is unramified and v_q(beta)=2, so its local value is psi(Frob_q)^2. At every other finite place beta is a unit; at the possibly ramified lambda_3 and lambda_5 its residue is 1. The other finite local values are 1 because psi is unramified there, including at p. The real local values are 1 because beta is totally positive. The product formula consequently gives psi(Frob_q)^2=1. This direct argument also shows explicitly that all eligible characters are covered, without enumerating a ray group.

Finally chi_7(Frob_q)=N(q)=29=1 in F_7. The trace of an extension equals the trace of its semisimplification, so

\[
tr(rho(Frob_q))=psi(Frob_q)+psi(Frob_q)^{-1}=\pm2.
\]

Geometric Frobenius inverts the two eigenvalues; here the determinant is 1 and both constituents at q are ±1, so it gives the same trace.

**Exact arithmetic check and scope.** Run `python3 scripts/mixed-seventh-certificate/check_characters.py --output scripts/mixed-seventh-certificate/character-results.json`. The [reproducer](../scripts/mixed-seventh-certificate/check_characters.py) checks the ring identities, all relevant residues, inertness, both norms, the four digit types and their survivors. Its [exact output](../scripts/mixed-seventh-certificate/character-results.json) also certifies positivity at both embeddings using rational bounds whose squares bracket 5. Raynaud's theorem and reciprocity are cited inputs, not claims established by this program. The audit uses the ready SPECIALIZE assessment as a reproduction of an existing conditional claim. It supplies the character component of the comparison family while leaving irreducible packets, four-parameter applicability and the global descent unresolved. The required main threshold remains zero positive primitive solutions for every residual signature.

## Mathlib

Coverage of the full conditional trace restriction: **not checked**. Supporting finite-flat, Artin-conductor, reciprocity and ray-class results: **not checked**. The precise Raynaud and Milne references above are supporting named inputs. [Chocian, arXiv:2609.26996v1, Section 6.2](https://arxiv.org/html/2609.26996v1#S6.SS2) matches the conditional character claim; its original-solution applicability and irreducible-packet exhaustion are not imported. No matching Mathlib theorem, formal verification or result beyond the checked literature is claimed.
