# L023 — Exact coefficient corrections retain high degree

## Hypotheses

Work in the free noncommutative polynomial ring over F₂. Each original variable and each independent placeholder has degree one; degree means degree of the formal polynomial after cancellation, before substituting any axioms. Circuits are division-free with binary addition and ordered multiplication, and sharing is allowed.

Let B(x) consist of the original Boolean polynomials x_i²+x_i and pair-once commutators x_i x_j+x_j x_i. Write b for their placeholders. An **exact coefficient correction** for an x-only polynomial P and a proposed x-only representative r is a polynomial E(x,b) satisfying

E(x,0)=0,                    E(x,B(x))=P(x)+r(x).                 (1)

Allow arbitrary placeholder degree. For multiplication, suppose E,G satisfy (1) for P,r and Q,s respectively, and a supplied local witness H satisfies H(x,0)=0 and H(x,B)=rs+u for the proposed product representative u. These are formal identities, not only equalities on Boolean assignments.

For the application, use the coefficient R_m in L022's projection rho(C_m)=t_1 R_m of the actual L021 output. Its degree is

e_m=Fib_(m+3)+Fib_(m+1)-5,

and the supplied ER binary length is T_m=Theta(m log(m+2)). The original variables are x,y, so B=(x²+x,y²+y,xy+yx). Consider any x-only representative r_m of degree at most T_m^c for a fixed c, whenever an exact correction exists.

## Conclusion

The formally valid multiplication update is

K=E s+r G+E G+H.                                                 (2)

It has K(x,0)=0 and K(x,B)=PQ+u, and adds at most six arithmetic gates to shared input roots. If E,G,r,s,H have degree bounds d_E,d_G,d_r,d_s,d_H, its degree is at most

max(d_E+d_s, d_r+d_G, d_E+d_G, d_H).                              (3)

But whenever deg(P+r)=D, **every** correction satisfying (1) has degree at least ceil(D/2). Thus, for all sufficiently large m, every exact correction for R_m,r_m has degree at least ceil(e_m/2), exceeding every fixed polynomial in T_m. Allowing nonlinear placeholders or arbitrary circuit reorganization does not avoid this bound. Even if all original clause placeholders are admitted in an exact correction, axiom degree at most three gives the still superpolynomial bound ceil(e_m/3).

The degree obstruction is already sharp on the one-variable repeated-square test P_k=x^(2^k), r_k=x: there are O(k)-gate corrections of degree exactly 2^(k-1) for k>=1, and none of smaller degree. The reduced representative has degree one throughout.

This stops the invariant requiring independently polynomial-degree exact corrections for the unreduced coefficients. It does not lower-bound a final certificate after cancellations between its sectors, or every different certificate for the original CNF. In particular it does not exclude a direct invariant on reduced clause polynomials, which need not retain (1). L019's constant alternative certificate remains available. No ER lower bound, arbitrary-circuit identity test or decision separation follows. This is an informative negative test under the saved EXPLORE assessment, potentially beyond its checked full-statement comparison, with no originality claim.

## Proof

**Ordered multiplication and size.** After substitution, E=P+r and G=Q+s. Expanding the first three summands of (2) in their written order gives

(P+r)s+r(Q+s)+(P+r)(Q+s)=PQ+rs.

Indeed Ps, rQ and each extra rs cancel in pairs, leaving PQ+rs. Adding H(B)=rs+u leaves PQ+u. Every summand in (2) contains a zero-at-b=0 witness, so K(x,0)=0. No commutation of r,s,E,G is used. The three products and three binary additions add six gates; all operands are shared roots. With S total input-DAG nodes this costs O(S+1) gates and O((S+1)log(S+2)) bits for densely numbered references, plus the supplied labels. The degree inequalities for addition and multiplication give (3). In particular the E G term cannot be silently discarded: its substituted residual would be (P+r)(Q+s), which need not vanish as a formal polynomial.

**Transport into an IPS certificate.** Let A be the full original clause/Boolean/commutator list and C the certificate from L021, or any supplied C satisfying C(x,0)=0 and C(x,A)=1. If an occurrence is a left coefficient P t_j, replace it by

r t_j+E(x,b) A_j(x),                                             (4)

or by r t_j+E(x,b)t_j. Both replacements vanish at zero placeholders, and both evaluate to P A_j after the full substitution. For a right coefficient t_j P, the corresponding replacements are t_j r+A_j E or t_j r+t_j E. The order matters. Fixed surrounding x-only factors can be retained in the same positions. Replacing that additive contribution in C therefore preserves both IPS identities, while generally changing its formal polynomial. The first version retains no clause placeholder in its new correction, and the second allows nonlinear placeholder dependence as permitted by the assessment. Neither silently discards the correction.

This applicability statement is conditional on an exact witness E. It does not assert that every occurrence can be enumerated efficiently in a shared circuit. The local multiplication construction above works on shared roots without that enumeration.

**Degree under axiom substitution.** A word of length d in x,b maps under b -> B(x) to a polynomial of degree at most 2d: every x contributes one letter and every Boolean/commutator placeholder contributes at most two. Therefore, for every nonzero E,

deg E(x,B(x)) <= 2 deg E(x,b).                                   (5)

Cancellation can only reduce the substituted degree. This argument permits any number of placeholders in a word and applies to the polynomial computed by any circuit, independently of its syntactic degree. Equation (1) and deg(P+r)=D imply deg E>=ceil(D/2). With the full original width-at-most-three axiom list, the identical argument replaces 2 by 3.

L022 establishes e_m and its exponential growth for the actual clause coefficient R_m. For fixed c, eventually e_m>T_m^c>=deg r_m. Its top-degree words cannot cancel with those of r_m, so deg(R_m+r_m)=e_m. Applying (5) gives the stated lower bound for every exact correction, not merely the recurrence (2). Exponential Fibonacci growth in m exceeds every fixed polynomial in T_m=Theta(m log(m+2)); this is the required comparison, not an inference from a finite table.

This application is not vacuous: expand the finite polynomial R_m, sort each word into x's followed by y's using adjacent swaps, and remove repeated adjacent letters. A swap changes a word by L(xy+yx)R; a deletion changes it by L(x²+x)R or L(y²+y)R. Replace that one displayed axiom by its placeholder and sum all these witnesses. Telescoping gives (1) for a representative in the span of 1,x,y,xy, of degree at most two. This only establishes finite existence; the expansion has no polynomial size bound and (5) forces high correction degree even for this low-degree representative.

**Sharp multiplication test with the full correction retained.** Take one original variable x and B=x²+x with placeholder b. Put E_1=b and use (2) with r=s=u=x, E=G=E_k and H=b:

E_(k+1)=E_k x+x E_k+E_k²+b.                                     (6)

Since x²+x=B, the multiplication proof shows inductively that E_k(x,0)=0 and E_k(x,x²+x)=x^(2^k)+x. At each stage (6) uses at most six new gates and only references the preceding correction. Hence the common DAG has O(k) gates and O(k log(k+2)) bits. All free inputs and all correction sectors are included.

Its degree is at most 2^(k-1). At k=1 this is one. If d_k<=2^(k-1), the next degree is at most max(d_k+1,2d_k,1)<=2^k. Equation (5), applied to the nonzero degree-2^k polynomial x^(2^k)+x, supplies the matching lower bound d_k>=2^(k-1). This establishes exact formal degree without confusing syntactic growth with surviving words. In particular the square E_k² creates exponential degree despite constant reduced operands and linear shared size; omitting it violates the formal identity. More generally any reduced r_k of degree less than 2^k still forces the same lower bound by (5).

For the right-coefficient form relevant to t_1 R_m, the isolated replacements t_1 r_m+A_1 E_m and t_1 r_m+t_1 E_m themselves retain high degree: here A_1=1+x, so deg((1+x)E_m)=deg E_m+1. Its words contain a Boolean/commutator placeholder and no t_1; those of t_1 r_m do not, so they cannot cancel. In the second version, words of t_1 E_m contain a Boolean/commutator placeholder while words of t_1 r_m do not. This does not exclude cancellation against the **other** parts of the full certificate. It is precisely why the stop is restricted to independently bounded coefficient corrections and cannot be promoted to a lower bound on alternative output certificates.

**Verification scope.** `PYTHONDONTWRITEBYTECODE=1 python3 scripts/coefficient-reduction/check_correction_update.py` checks the ordered universal identity, detects omission of E G and a reversed factor, expands (6) in the free alphabet x,b through k=4, and checks both substitutions and the exact degree independently. It checks coefficient transport in both orientations and both permitted correction placements. The saved diagnostic is `scripts/coefficient-reduction/correction-results.json`. These finite checks support the identities; (5) and the all-m argument, rather than numerical growth, prove the asymptotic obstruction.

## Mathlib

Coverage: **not checked** for this full correction-update statement, its degree obstruction or binary accounting. The elementary substitution-degree bound and ordered identities are proved above. Forbes–Shpilka–Tzameret–Wigderson, [*Proof Complexity Lower Bounds from Algebraic Circuit Complexity*, Theory of Computing 17(10), 2021, §4.2, Propositions 4.5–4.6 and Lemma 4.9](https://toc.cs.uchicago.edu/articles/v017a010/v017a010.pdf), gives supporting commutative correction constructions under restricted representation/degree hypotheses. Li–Tzameret–Wang, [*Characterizing Propositional Proofs as Non-Commutative Formulas*, arXiv:1412.8746v4, Lemmas 3.6–3.7](https://arxiv.org/pdf/1412.8746v4), gives supporting formal formula-commutation witnesses. Neither inspected statement is a full match for this exact-lift audit on L022's shared coefficient. The rederivation addresses ordered multiplication, nonlinear correction placeholders and complete correction degree; it does not reprove generic multilinearization or claim a new general hardness theorem. The prior assessment's Hrubeš comparison remains conditional and is not used as a premise here.
