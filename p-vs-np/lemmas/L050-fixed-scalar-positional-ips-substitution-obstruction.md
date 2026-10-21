# L050 — Fixed scalar positional substitution fails on valid IPS certificates

## Hypotheses

Use L048's occurring-variable width-at-most-three CNF convention, full ordered original axiom/placeholder package and explicitly encoded acyclic affine-F₂ ABPs. The two certificate identities are formal identities in the free associative algebra, not merely identities on Boolean assignments.

Fix the single formula F=(x) AND (NOT x), with the positive unit written first. Its complete occurring original dictionary is (x). Its ordered axiom list and independent placeholder dictionary are exactly

    A₁=1+x,     A₂=x,     A₃=xx+x;
    (t₁,t₂,t₃).

Here A₁,A₂ are the two clause falsity polynomials and A₃ is the sole Boolean axiom. There are no commutator positions because there is only one original variable. Names t_a use L048's distinct namespace and dense A-position convention. The unused t₃ and its axiom remain in every complete certificate package.

Import the scalar F-linear positional map φ of Forbes–Shpilka, Construction 4.1: φ(1)=1 and a word z_i₁…z_i_d maps to the commuting product z_i₁,₁…z_i_d,d. Apply it to the whole independent alphabet z=(x,t₁,t₂,t₃). Fix the same degree bound D=2 for every certificate below; retain the full positional dictionary

    x₁,x₂, t₁,₁,t₁,₂, t₂,₁,t₂,₂, t₃,₁,t₃,₂.

The subscripts on x denote word positions, not different original variables. They are independent commuting indeterminates.

The receiving ring is R=F₂[x₁,x₂,q₁,…,q_r], with any fixed finite r≥0 and independent auxiliary scalar indeterminates q_j. No quotient identifying x₁ and x₂ is imposed. A proposed scalar axiom substitution ρ fixes all original positional symbols x_k and assigns an arbitrary polynomial b_a,k∈R to each t_a,k. Its assignments are shared by every certificate for this fixed F and D: they may depend on the axiom position a and positional index k (and this fixed F,D), but not on a containing word, path or certificate. Polynomial degree and description size of the b_a,k are unrestricted. The zero substitution ρ₀ fixes x₁,x₂ and sends all t_a,k to zero.

The tested universal interface would require, for every valid certificate C on this package,

    ρ₀(φ(C))=φ(C(x,0))=0,
    ρ(φ(C))=φ(C(x,A(x)))=1.

This specifies a scalar polynomial-substitution interface for the unchanged positional encoding. It is not matrix evaluation, a certificate-dependent substitution, a quotient of the positional original alphabet or a new component assembly rule.

## Conclusion

There is **no** such fixed scalar substitution preserving the second identity for every valid L048 certificate, even on this one formula and D=2. A family of three explicit affine ABPs, with at most four vertices and five edges each and complete constant-size input packages, suffices. Each satisfies both original free-ring IPS identities and its encoded first identity. For any receiving images b_a,k, at least one of these three valid certificates fails the encoded second identity.

In particular, if the first two certificates are preserved, the third has receiving value 1+x₁+x₂, whereas encoding after original axiom substitution gives 1. This stops the specified universal fixed scalar interface without any complexity-bound assumption. It does not assert that every encoding, matrix system, changed axiom system or certificate-selection method fails. It establishes neither certificate hardness nor a SAT decision/separation. This is POTENTIALLY_NEW only in the policy's sense that the reused bounded literature assessment did not establish coverage; certified originality is not claimed. The separate critical audit on 2026-10-11 (step 148), recorded below, found no substantive error within this fixed scalar scope.

## Proof

**Source, scope and purpose of the extra argument.** The pre-invocation EXPLORE assessment `drafts/literature/2026-10-10-position-encoding-ips-substitution.md` covers this scalar compatibility test. Import only Michael A. Forbes and Amir Shpilka, *Quasipolynomial-time Identity Testing of Non-Commutative and Read-Once Oblivious Algebraic Branching Programs*, [arXiv:1209.2408v2, Construction 4.1, printed p.22](https://arxiv.org/pdf/1209.2408v2), for the definition of φ. The assessment inspected Construction 4.1 and the full relevant proofs of Lemmas 4.2–4.5 and Theorem 4.6, printed pp.22–25. The map is defined over an arbitrary field, so F₂ is allowed; the large-field hitting-set hypothesis of Corollary 4.7 is not used. No normalization, hitting-set or full-bit theorem from those sources is reproved or imported. The calculation below is needed because their zero-test/representation conclusions do not establish substitution compatibility on valid IPS certificates. L048 supplies the exact receiving input convention, not either of its unproved polynomial-bound premises. L049 is downstream context only; L033/L034 and Attempts 018/020/021/022 are contrasts and historical stops, not mathematical inputs.

**Three explicit complete certificate packages.** Write u=t₁+t₂, an allowed affine edge label, and set

    C⁽⁰⁾=u,
    C⁽¹⁾=uu,
    C⁽²⁾=u+ux+xu.

The superscripts are labels for the three certificates, not exponents. Realize C⁽⁰⁾ by vertices s,z with the single edge s→z labelled u. Realize C⁽¹⁾ by vertices s,v,z and edges s→v and v→z, both labelled u. Realize C⁽²⁾ by vertices s,v,w,z with edges

    s→z : u;
    s→v : u;    v→z : x;
    s→w : x;    w→z : u.

The designated entrance and exit are s,z in each graph. The displayed order s,v,w,z is topological for the last graph; the other orders are also topological. The first has one accepting path, the second one accepting path, and the third exactly the three displayed paths of lengths one, two and two. Expanding the affine labels gives exactly the three polynomials stated, with no additional empty accepting path since s≠z. Every edge label lists its coefficient-one symbols explicitly; its constant coefficient is zero. Each graph package carries F, its original dictionary (x), all three independent placeholder names, the entire ordered A word list, endpoint records, counts and framing. No graph uses t₃, but it remains permitted and paid for. There are no additional original variables or extension variables. With the fixed names and formula these are complete constant-bit-size packages, not just node counts. The positional dictionary has exactly the eight symbols displayed above; all names and positions are fixed. No asymptotic graph conversion or path unfolding is needed for this example. The unequal degrees of C⁽²⁾ and the two-placeholder path of C⁽¹⁾ are allowed by L048.

**Original formal identities.** Simultaneously setting all three independent placeholders to zero makes u=0, so each C⁽ⁱ⁾(x,0)=0 in the free algebra. Under the full original axiom substitution,

    u(x,A)=(1+x)+x=1.

Consequently C⁽⁰⁾(x,A)=1, C⁽¹⁾(x,A)=1·1=1, and

    C⁽²⁾(x,A)=1+1·x+x·1=1+x+x=1.

These equalities use only characteristic two and the multiplicative unit, with factor order retained. No Boolean quotient, commutativity of the free ring, semantic UNSAT test or assumption about short certificates is used. The formula is UNSAT because its two units require opposite values of its sole variable.

**Full scalar encoding, including constants and unequal degrees.** In the commuting positional ring put U₁=t₁,₁+t₂,₁ and U₂=t₁,₂+t₂,₂. Construction 4.1's word rule and linearity give the complete encoded polynomials

    φ(C⁽⁰⁾)=U₁,
    φ(C⁽¹⁾)=U₁U₂,
    φ(C⁽²⁾)=U₁+U₁x₂+x₁U₂.                 (1)

For the second formula the four ordered free words t₁t₁,t₁t₂,t₂t₁,t₂t₂ map respectively to the four terms of U₁U₂. For the third, ux puts the placeholder at position one and x at position two, while xu puts x at position one and the placeholder at position two. The degree-one term still starts at position one. There is no shifting a word because of a containing path, and no multiplication-preservation assumption about φ. Since each original substituted polynomial is the constant 1, its encoding is φ(1)=1, including degree zero. Applying ρ₀ to (1) gives zero in every case, agreeing with encoding after zero substitution.

**All arbitrary fixed receiving images.** Let B₁=b₁,₁+b₂,₁ and B₂=b₁,₂+b₂,₂ in R. Images of t₃,₁ and t₃,₂ are irrelevant because those symbols never occur in (1); thus their images are fully covered without restriction. If ρ preserves C⁽⁰⁾, the first formula in (1) forces B₁=1 as a polynomial identity in R. If it also preserves C⁽¹⁾, the second then forces B₂=1, since B₁B₂=1 and B₁=1. The receiving value of the third is therefore

    B₁+B₁x₂+x₁B₂=1+x₂+x₁.

It differs from 1: the monomials x₁ and x₂ are distinct in the polynomial ring R, and each has coefficient one. This remains so with any of the permitted auxiliary indeterminates. In explicit quantifier order, for every fixed assignment of all six receiving images, either B₁≠1 and C⁽⁰⁾ fails, or B₁=1 and B₂≠1 and C⁽¹⁾ fails, or B₁=B₂=1 and C⁽²⁾ fails. Hence no fixed assignment preserves all valid certificates. This proves impossibility for arbitrary polynomial images, not just a guessed encoding of each axiom. The three certificates all use the same F, full positional dictionary and chosen D=2, so a map's dependence on F or D cannot evade the argument.

For an explicit usual clause-image choice b₁,k=1+x_k and b₂,k=x_k for k=1,2, B₁=B₂=1. Then the first two pass and the displayed C⁽²⁾ fails, regardless of the Boolean-placeholder images. This is an illustrative instance of the general argument, not its premise.

**Qualifications and downstream threshold.** The achieved obstruction excludes even unbounded-degree, unbounded-size fixed polynomial images, so in particular it excludes a polynomial-complete-length substitution of this specified universal form. It does not rule out translating a selected certificate differently, identifying original positions, using matrices, adding new axioms or changing how homogeneous components are combined. A component package reconstructed by summing its degree pieces with this same scalar substitution inherits (1) and the obstruction; arbitrary other assembly rules are outside the hypotheses. The source's matrix/component PIT correspondence is therefore not refuted. No preservation theorem for another receiving system is inferred. This family has easy constant-size certificates and refutations; it is not a hard UNSAT family. Independent F₂ every-certificate hardness, class-preserving CNF reductions, arbitrary ER-to-ABP data and unrestricted SAT transfer remain unproved. The separate step-148 audit below verifies this exact scope informally; it does not verify another receiving system.

**Separate critical audit — 2026-10-11, step 148.** The prior EXPLORE assessment `drafts/literature/2026-10-10-fixed-scalar-positional-obstruction-audit.md` approves exactly this audit. Reuse the inspected primary definition cited above; neither a further source theorem nor a normalization theorem is needed. The following checks verify the finite obstruction rather than assume its conclusion.

1. **Input validity and complete paths.** L048's literal-falsity convention assigns 1+x to the positive unit and x to the negative unit. Its one occurring original variable contributes exactly the additional Boolean position xx+x, and the i<k commutator list is empty. Thus the stated three-position package is exact. All displayed labels are affine over the four-symbol free alphabet. For the third graph, the only edges out of s go to z, v and w; the only edges out of v and w go to z, and z has no outgoing edge. Its path list is therefore exhaustive. In particular, there is no v-to-w path or empty accepting path. The first two graphs similarly have exactly their one listed path. The full permitted alphabet is present in each encoding even when a symbol is unused. No polynomial-bound assertion of L048 is invoked.

2. **Independent word-level identity check.** The second polynomial has the four words t₁t₁+t₁t₂+t₂t₁+t₂t₂. Its substituted expansion is (1+x)(1+x)+(1+x)x+x(1+x)+xx. The constant term occurs once, x occurs four times and xx occurs four times, giving 1 formally over F₂. The third polynomial has the six words t₁+t₂+t₁x+t₂x+xt₁+xt₂. After substitution it is (1+x)+x+(1+x)x+xx+x(1+x)+xx: again the constant occurs once, x four times and xx four times. The first is (1+x)+x=1. Each word before substitution contains a placeholder, so setting all placeholders to zero gives zero for all three. These checks require no evaluation at Boolean x and no axiom quotient.

3. **Degree and alphabet check.** Before substitution the maximum word lengths are 1, 2 and 2, respectively. A common upper bound D=2 is legitimate; D is not required to be the minimal degree of each certificate. The four free symbols give exactly eight positional symbols. The unused x₂ in the first encoding and both t₃ positions remain in the common dictionary. There is no homogenization, padding word or path-dependent shift: the two length-one words in the third certificate occupy position one. Encoding the above complete word lists gives exactly (1). Although a general axiom substitution can increase degree, here the substituted polynomial is exactly the constant 1; applying φ to it is legitimate without assuming a false degree-preservation theorem. The construction is linear, not multiplicative, and no step factors φ across arbitrary unequal-degree products.

4. **Universal receiving-image check.** Fix r and all six images before choosing which certificate fails. If b₁,₁+b₂,₁ is not the constant polynomial 1, the first certificate fails immediately. Otherwise the second receiving value is precisely b₁,₂+b₂,₂, so preserving it forces that sum to be 1 as well. This deduction uses multiplication by 1, not cancellation of an arbitrary polynomial or a domain assumption. With those two necessary identities imposed, subtracting 1 from the third receiving value gives x₁+x₂. The coefficient of the monomial x₁ (with zero exponents on x₂ and every q_j) is 1, so this is nonzero in every stated R. Arbitrary degrees, auxiliary variables and t₃ images cannot alter this coefficient after the two identities are imposed. This proves for every permitted fixed substitution that some member of the same three-certificate family fails. It makes no claim that one member defeats all substitutions independently of the other two tests.

5. **Scope and route decision.** The first encoded identity passes for all three certificates and all use the same F,D, so the counterexample is inside the claimed universal domain. Dependence of the map on the particular certificate would change that domain; identifying x₁ and x₂ would change the receiving ring. Matrices or a changed component assembly would change the tested operation. None is a loophole in the stated theorem, and none is ruled out by it. In particular the primary matrix/component PIT result is not an IPS simulation being contradicted. The necessary threshold for stopping this interface is failure on valid certificates for every fixed scalar image assignment, with no resource bound; the audit verifies precisely that threshold. No narrowing, repair, new complexity lower bound or certified novelty claim results. Retain Attempt 023's stop as informally critically verified. This does not advance a candidate solution of P versus NP.

The sole direct local mathematical input remains L048's package convention. The primary positional definition is cited above. The DAG therefore remains unchanged; L049 and the earlier stopped conversions are contextual comparisons, not hidden dependencies. This is a separate symbolic proof audit, not machine verification or additional theorem discovery.

## Mathlib

Full matching coverage for this scalar IPS-interface obstruction is **not checked**. No absence or Lean verification is claimed. Supporting free-algebra substitution and polynomial monomial independence would not themselves constitute a full matching theorem. The proof is a complete finite symbolic argument on the explicitly stated input packages, rather than numerical evidence or a PIT answer.
